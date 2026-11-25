#!/usr/bin/env python3
"""Local video inspection; requires ffmpeg and ffprobe. No upload or approval."""
import argparse
import json
from pathlib import Path
import subprocess

def run(args):
    return subprocess.run(args, check=True, text=True, capture_output=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("video", type=Path)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--fps", type=float, default=2)
    p.add_argument("--beat", type=float, action="append", default=[])
    a = p.parse_args()
    if not a.video.is_file() or not 0 < a.fps <= 12 or any(t < 0 for t in a.beat):
        p.error("Existing video, 0 < fps <= 12 and nonnegative beats required.")
    a.out.mkdir(parents=True, exist_ok=True)
    v = str(a.video.resolve())
    meta = json.loads(run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",v]).stdout)
    (a.out/"probe.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    stream = next(s for s in meta["streams"] if s["codec_type"]=="video")
    rate = stream.get("avg_frame_rate","30/1").split("/")
    fps = float(rate[0])/float(rate[1]) if float(rate[1]) and float(rate[0]) else 30
    duration = float(meta.get("format",{}).get("duration") or 0)
    base = ["ffmpeg","-hide_banner","-nostdin","-y"]
    run(base+["-loglevel","error","-i",v,"-vf",f"fps={a.fps},scale=240:-2,tile=4x5:padding=6:margin=6","-an","-q:v","3",str(a.out/"sheet-%03d.jpg")])
    for i,t in enumerate(a.beat):
        for tag,offset in [("pre",-2/fps),("at",0),("post",2/fps),("after",.3)]:
            at = max(0,t+offset)
            if duration and at >= duration:
                continue
            run(base+["-loglevel","error","-ss",str(at),"-i",v,"-frames:v","1","-q:v","3",str(a.out/f"beat-{i:03d}-{tag}.jpg")])
    scan = run(base+["-i",v,"-vf","blackdetect=d=0.15:pix_th=0.10,freezedetect=n=-50dB:d=0.5","-an","-f","null","-"])
    (a.out/"visual-scan.log").write_text(scan.stderr,encoding="utf-8")
    if any(s["codec_type"]=="audio" for s in meta["streams"]):
        scan = run(base+["-i",v,"-vn","-af","ebur128=peak=true","-f","null","-"])
        (a.out/"audio-scan.log").write_text(scan.stderr,encoding="utf-8")
    print("Inspection evidence:",a.out,"— manual review required.")

if __name__=="__main__":
    main()

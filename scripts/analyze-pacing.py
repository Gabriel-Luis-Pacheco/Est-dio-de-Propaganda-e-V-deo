#!/usr/bin/env python3
"""Sample RGB frame differences. Diagnostic only: cannot measure editorial quality."""
import argparse
import hashlib
import json
import math
import subprocess
import tempfile
from pathlib import Path

def analyze(frames, fps, threshold=8, fraction=.001, beats=()):
    import numpy as np
    previous = None
    changes = []
    for frame in frames:
        current = np.asarray(frame, dtype=np.int16)
        if previous is not None:
            changes.append(float(np.mean(np.max(np.abs(current-previous), axis=-1)>threshold)))
        previous = current
    low = [v < fraction for v in changes]
    def summary(indices):
        n=len(indices)
        count=sum(low[i] for i in indices)
        return {"comparisons":n,"low_seconds":count/fps,"low_fraction":count/n if n else None}
    intervals=[]
    start=None
    for i,flag in enumerate(low+[False]):
        if flag and start is None: start=i
        if not flag and start is not None:
            intervals.append({"start":start/fps,"end":i/fps,"seconds":(i-start)/fps})
            start=None
    result={"sampled_frames":len(changes)+int(previous is not None),"compared_seconds":len(changes)/fps,
            "overall":summary(list(range(len(changes)))),"low_intervals":intervals,
            "per_second":[{"start":s,"end":min(s+1,len(changes)/fps),**summary(list(range(s*fps,min((s+1)*fps,len(changes)))))} for s in range(math.ceil(len(changes)/fps))],
            "beats":[]}
    for beat in beats:
        ids=[i for i in range(len(changes)) if beat["start"] <= (i+.5)/fps < beat["end"]]
        result["beats"].append({"id":beat["id"],"start":beat["start"],"end":beat["end"],**summary(ids)})
    return result

def decode(path,fps,w,h):
    import numpy as np
    cmd=["ffmpeg","-nostdin","-v","error","-i",str(path),"-map","0:v:0","-an","-sn",
         "-vf",f"fps={fps},scale={w}:{h}","-pix_fmt","rgb24","-f","rawvideo","pipe:1"]
    size=w*h*3
    with tempfile.TemporaryFile() as err:
        p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=err)
        try:
            while True:
                raw=p.stdout.read(size)
                if not raw: break
                if len(raw)!=size: raise RuntimeError("incomplete RGB frame")
                yield np.frombuffer(raw,dtype=np.uint8).reshape(h,w,3)
            if p.wait()!=0:
                err.seek(0)
                raise RuntimeError(err.read().decode(errors="replace"))
        finally:
            if p.poll() is None: p.kill();p.wait()
            p.stdout.close()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("video",type=Path)
    p.add_argument("--timeline",type=Path)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--fps",type=int,default=30,help="resampling rate, not necessarily native")
    p.add_argument("--width",type=int,default=320)
    p.add_argument("--height",type=int,default=180)
    p.add_argument("--threshold",type=int,default=8)
    p.add_argument("--fraction",type=float,default=.001)
    a=p.parse_args()
    if min(a.fps,a.width,a.height)<1 or not 0<=a.threshold<=255 or not 0<a.fraction<=1:
        p.error("invalid sampling parameters")
    beats=json.loads(a.timeline.read_text(encoding="utf-8"))["beats"] if a.timeline else []
    report=analyze(decode(a.video,a.fps,a.width,a.height),a.fps,a.threshold,a.fraction,beats)
    if report["sampled_frames"]<2: p.error("at least two sampled frames required")
    report["method"]={"fps":a.fps,"width":a.width,"height":a.height,"rgb_max_delta_gt":a.threshold,
                      "low_changed_pixel_fraction_lt":a.fraction,
                      "note":"Adjacent resampled RGB frame pairs; interval i represents i/fps to (i+1)/fps. Last frame has no following comparison. VFR and different scaling/fps can change results. Low activity is not dead time or an automatic failure."}
    def sha(path):
        h=hashlib.sha256()
        with path.open("rb") as f:
            for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
        return h.hexdigest()
    report["master_sha256"]=sha(a.video)
    report["timeline_sha256"]=sha(a.timeline) if a.timeline else None
    report["review_windows"]=[] # fill after actual editorial inspection
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(f"Wrote {a.out}; editorial review required.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

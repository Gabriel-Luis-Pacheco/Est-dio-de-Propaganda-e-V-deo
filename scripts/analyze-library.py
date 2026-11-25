#!/usr/bin/env python3
"""Inspect local authorized MP4s, without executing or uploading them. Requires Pillow, FFmpeg and FFprobe."""
import argparse, concurrent.futures, hashlib, io, json, math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw


def inspect(video, out, samples):
    meta = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(video)]))
    stream = next(s for s in meta['streams'] if s['codec_type']=='video')
    duration = float(meta['format']['duration'])
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError(f'Invalid duration: {video}')
    sheet = Image.new('RGB',(960,math.ceil(samples/4)*164),'#222222')
    draw = ImageDraw.Draw(sheet)
    times, missing = [], []
    for i in range(samples):
        t = min(max(0,duration-.08), i*duration/samples)
        r = subprocess.run(['ffmpeg','-v','error','-threads','1','-ss',str(t),'-i',str(video),'-frames:v','1','-vf','scale=236:142:force_original_aspect_ratio=decrease','-threads','1','-f','image2pipe','-vcodec','mjpeg','-'],capture_output=True)
        x,y = i%4*240,i//4*164
        if r.returncode or not r.stdout:
            missing.append(round(t,3)); draw.text((x+4,y+40),'MISSING FRAME',fill='white')
        else:
            im = Image.open(io.BytesIO(r.stdout)).convert('RGB')
            sheet.paste(im,(x+(240-im.width)//2,y)); times.append(round(t,3))
        draw.text((x+4,y+145),f'{t:.2f}s',fill='white')
    name = f'{video.stem}.jpg'
    sheet.save(out/name,quality=85)
    return {'filename':video.name,'duration':round(duration,3),'width':stream['width'],'height':stream['height'],'fps':stream['avg_frame_rate'],'sha256':hashlib.file_digest(video.open('rb'),'sha256').hexdigest(),'audio':any(s['codec_type']=='audio' for s in meta['streams']),'sheet':name,'requested_samples':samples,'timestamps':times,'missing':missing,'visual_review':'pending'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory',type=Path)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--samples',type=int,default=12)
    p.add_argument('--jobs',type=int,default=4)
    p.add_argument('--expect',type=int)
    a = p.parse_args()
    if not a.directory.is_dir() or not 1 <= a.samples <= 60 or not 1 <= a.jobs <= 8:
        p.error('Valid directory, 1–60 samples and 1–8 jobs required.')
    videos = sorted(a.directory.glob('*.mp4'))
    if not videos or (a.expect is not None and len(videos)!=a.expect):
        p.error(f'Found {len(videos)} videos, expected {a.expect or "at least one"}.')
    a.out.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as pool:
        data=list(pool.map(lambda v:inspect(v,a.out,a.samples),videos))
    (a.out/'manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    failures=sum(len(r['missing']) for r in data)
    print(f'{len(data)} videos, {sum(len(r["timestamps"]) for r in data)} frames, {failures} missing; manual visual review pending.')
    return 1 if failures else 0

if __name__=='__main__':
    raise SystemExit(main())

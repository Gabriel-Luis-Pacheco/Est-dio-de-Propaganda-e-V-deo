"""Render actual SVG studies to MP4 (local CairoSVG + Node + FFmpeg). Do not certify taste."""
import argparse,subprocess,tempfile
from pathlib import Path
import cairosvg
ROOT=Path(__file__).resolve().parents[1]
def render(id,out,fps,seconds):
    with tempfile.TemporaryDirectory() as d:
        d=Path(d)
        subprocess.run(['node',str(ROOT/'arsenal/motion/render.mjs'),id,str(d),str(seconds),str(fps)],check=True)
        frames=sorted(d.glob('*.svg'))
        if not frames:raise ValueError('no frames')
        for s in frames:cairosvg.svg2png(url=str(s),write_to=str(s.with_suffix('.png')),output_width=640,output_height=360)
        out.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run(['ffmpeg','-y','-v','error','-framerate',str(fps),'-i',str(d/'%05d.png'),'-c:v','libx264','-pix_fmt','yuv420p',str(out)],check=True)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('id');p.add_argument('--out',type=Path,required=True);p.add_argument('--fps',type=int,default=24);p.add_argument('--seconds',type=float,default=2);a=p.parse_args();render(a.id,a.out,a.fps,a.seconds)

import argparse,json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import cv2,numpy as np

def analyze(path,fps=8):
    w,h=160,90
    cmd=['ffmpeg','-v','error','-threads','1','-i',str(path),'-an','-vf',f'fps={fps},scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2','-pix_fmt','gray','-f','rawvideo','-threads','1','-']
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    prev=None; flow=[]; cuts=[]; idx=0
    while True:
        b=p.stdout.read(w*h)
        if len(b)!=w*h:break
        cur=np.frombuffer(b,np.uint8).reshape(h,w)
        if prev is not None:
            d=float(np.abs(cur.astype('float32')-prev).mean())/255
            hist1=cv2.calcHist([prev],[0],None,[32],[0,256]);hist2=cv2.calcHist([cur],[0],None,[32],[0,256]);cv2.normalize(hist1,hist1,alpha=1,norm_type=cv2.NORM_L1);cv2.normalize(hist2,hist2,alpha=1,norm_type=cv2.NORM_L1)
            dist=cv2.compareHist(hist1,hist2,cv2.HISTCMP_BHATTACHARYYA)
            if d>.18 and dist>.26:cuts.append(round(idx/fps,3))
            else:
                v=cv2.calcOpticalFlowFarneback(prev,cur,None,.5,2,13,2,5,1.1,0)
                mag=np.linalg.norm(v,axis=2);flow.append([round(idx/fps,3),round(float(np.quantile(mag,.9))*fps,3)])
        prev=cur;idx+=1
    if p.wait()!=0 or idx<2:raise ValueError('decode failed')
    vals=[x[1] for x in flow];dur=idx/fps
    audio=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-map','0:a:0','-ac','1','-ar','8000','-f','f32le','-'],capture_output=True)
    onsets=[];rms=None
    if audio.returncode==0 and len(audio.stdout)>=800:
        a=np.frombuffer(audio.stdout,dtype='<f4');a=a[:len(a)//80*80].reshape(-1,80)
        rms=np.sqrt(np.mean(a*a,axis=1));db=20*np.log10(np.maximum(rms,1e-8));jump=np.diff(db,prepend=db[0]);threshold=max(6,float(np.quantile(jump,.95)));last=-100
        for i in np.flatnonzero((jump>=threshold)&(db>-45)):
            if i-last>=12:onsets.append(round(i*.01,3));last=i
    return {'file':path.name,'sample_fps':fps,'sample_size':[w,h],'duration_est':round(dur,3),'cut_candidates':cuts,'flow_p90_px_per_s_quantiles':[round(float(np.quantile(vals,q)),2) for q in [.1,.5,.9]] if vals else [],'audio_attack_candidates':onsets,'audio_present':rms is not None,'cut_near_attack_100ms':sum(any(abs(c-a)<=.1 for a in onsets) for c in cuts),'note':'Proxy motion and onset candidates only; cuts, beats and taste require human review.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('--out',type=Path,required=True);p.add_argument('--fps',type=int,default=8);a=p.parse_args()
    if not 2<=a.fps<=30:p.error('fps must be 2–30')
    paths=sorted(a.input.glob('*.mp4')) if a.input.is_dir() else [a.input]
    if not paths:p.error('no videos')
    cv2.setNumThreads(1)
    with ThreadPoolExecutor(max_workers=4) as ex:data=list(ex.map(lambda path:analyze(path,a.fps),paths))
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(data,indent=2),encoding='utf-8');print(f'{len(data)} videos analyzed')
if __name__=='__main__':main()

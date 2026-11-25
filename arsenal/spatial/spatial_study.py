import argparse,math,subprocess,tempfile
from pathlib import Path
import vtk

def ease(t):
    t=max(0,min(1,t));return t*t*(3-2*t)
def actor(src,color,metal=.0,rough=.4):
    mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(src.GetOutputPort())
    a=vtk.vtkActor();a.SetMapper(mapper);p=a.GetProperty();p.SetColor(*color);p.SetInterpolationToPBR();p.SetMetallic(metal);p.SetRoughness(rough);return a

def run(preset,out,fps=24,seconds=2):
    ren=vtk.vtkRenderer();ren.SetBackground(.07,.11,.12);ren.SetUseShadows(False)
    win=vtk.vtkEGLRenderWindow();win.SetOffScreenRendering(1);win.SetSize(640,360);win.SetMultiSamples(4);win.AddRenderer(ren)
    colors=[(.96,.57,.20),(.82,.88,.78),(.25,.57,.52)]
    actors=[]
    for i in range(12):
        if preset=='orbit':
            src=vtk.vtkSphereSource();src.SetRadius(.22);src.SetThetaResolution(32);src.SetPhiResolution(24)
        else:
            src=vtk.vtkCylinderSource();src.SetRadius(.65);src.SetHeight(.13);src.SetResolution(64)
        a=actor(src,colors[i%3],.15,.32);ren.AddActor(a);actors.append(a)
    for pos,col,intensity in [((4,-5,7),(1,.87,.72),1.3),((-5,-1,3),(.62,.83,1),.9),((2,6,5),(1,1,1),1.1)]:
        l=vtk.vtkLight();l.SetLightTypeToSceneLight();l.SetPosition(*pos);l.SetFocalPoint(0,0,0);l.SetColor(*col);l.SetIntensity(intensity);ren.AddLight(l)
    cam=ren.GetActiveCamera();cam.SetViewUp(0,0,1);cam.SetFocalPoint(0,0,0);cam.ParallelProjectionOn();cam.SetParallelScale(2.6)
    grab=vtk.vtkWindowToImageFilter();grab.SetInput(win);grab.ReadFrontBufferOff();writer=vtk.vtkPNGWriter();writer.SetInputConnection(grab.GetOutputPort())
    with tempfile.TemporaryDirectory() as d:
        n=round(fps*seconds)
        for i in range(n):
            t=i/max(1,n-1);e=ease(t);angle=-.7+1.15*e
            cam.SetPosition(6*math.cos(angle),6*math.sin(angle),3.3)
            for j,a in enumerate(actors):
                if preset=='orbit':
                    k=j*math.tau/12+2.4*(1-e);r=2.05-1.1*e;a.SetPosition(r*math.cos(k),r*math.sin(k),.65*math.sin(k*2)*(1-e));a.SetScale(1,1,1)
                else:
                    k=j-5.5;a.SetOrientation(90,0,12*k*(1-e));a.SetPosition(.35*math.sin(j)*(1-e),.3*math.cos(j)*(1-e),k*(.34-.19*e));a.SetScale(1,1,1)
            ren.ResetCameraClippingRange();win.Render();grab.Modified();grab.Update();writer.SetFileName(str(Path(d)/f'{i:05d}.png'));writer.Write()
        subprocess.run(['ffmpeg','-y','-v','error','-framerate',str(fps),'-i',str(Path(d)/'%05d.png'),'-c:v','libx264','-pix_fmt','yuv420p',str(out)],check=True)
    win.Finalize()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('preset',choices=['orbit','stack']);p.add_argument('--out',type=Path,required=True);p.add_argument('--fps',type=int,default=24);p.add_argument('--seconds',type=float,default=2);a=p.parse_args()
    if not 1<=a.fps<=60 or not .2<=a.seconds<=10:p.error('invalid fps or duration')
    a.out.parent.mkdir(parents=True,exist_ok=True);run(a.preset,a.out,a.fps,a.seconds)

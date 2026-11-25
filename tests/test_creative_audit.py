"""Fixtures validate contract plumbing, never creative quality."""
import copy,importlib.util,json,subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("audit",ROOT/"scripts/creative-audit.py")
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
S="Synthetic fixture sentence only not a creative assessment"
class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.job=Path(self.tmp.name);self.m={"stages":{}}
        for k in a.STAGES:self.m["stages"][k]={"checks":{}}
        self.records={}
        def fake(name):return self.write(name,"fixture "+name)
        self.fake=fake
        self.put("G1","five_concepts",{"concepts":[dict(id=str(i),premise=S,visual_mechanism=S+str(i),brand_specificity=S,payoff=S,reason=S,decision="selected" if i==0 else "rejected") for i in range(5)]})
        roles=["LOOK"]*5+["MOVES"]*3+["SOUND"]*3
        self.put("G1","reference_calibration",{"requested_minimum":0,"references":[dict(id=str(i),role=r,url="https://example.invalid/"+str(i),timestamp="0s",observed=True,mechanism=S,transfer=S,avoid=S,rights="synthetic",media=fake("ref"+str(i))) for i,r in enumerate(roles)]})
        self.put("G2","styleframes",{"frames":[dict(id=str(i),role=r,decision="accepted" if i<3 else "rejected",score=4,observation=S,comparison=S,reason=S,media=fake("frame"+str(i))) for i,r in enumerate(["opening","hero","signature","other"])]})
        self.put("G3","canonical_timeline",{"fps":24,"duration":2,"beats":[dict(id="b1",start=0,end=2,**{k:S for k in a.BEAT_FIELDS})]})
        self.put("G3","audio_directions",{"directions":[dict(id=str(i),decision="selected" if i==0 else "rejected",auditioned=True,intent=S,heard_observation=S,reason=S,rights="synthetic",media=fake("audio"+str(i))) for i in range(3)]})
        self.put("G5","regression_review",{"regressions":[dict(id=i,decision="passed",timestamp="0s",observation=S,reason=S,evidence=fake(i)) for i in a.REGRESSIONS],"beats":[dict(id="b1",dimensions={k:dict(score=4,observation=S,comparison=S) for k in a.BEAT_DIMENSIONS},evidence=fake("beat"))]})
    def tearDown(self):self.tmp.cleanup()
    def write(self,name,content):
        p=self.job/name;p.write_text(content);return {"path":name,"sha256":a.sha(p)}
    def put(self,g,k,data):
        self.records[g,k]=data
        self.m["stages"][g]["checks"][k]={"evidence":self.write(g+k+".json",json.dumps(data))}
    def change(self,g,k,fn):
        d=copy.deepcopy(self.records[g,k]);fn(d);self.put(g,k,d)
    def errors(self,through="G5",probe=False):return a.audit(self.job,self.m,through,probe)
    def check(self,part,through="G5",probe=False):self.assertTrue(any(part in e for e in self.errors(through,probe)),self.errors(through,probe))
    def test_positive_structure(self):self.assertEqual(self.errors(),[])
    def test_four_concepts(self):
        self.change("G1","five_concepts",lambda d:d["concepts"].pop());self.check("five distinct concepts")
    def test_duplicate_concept(self):
        self.change("G1","five_concepts",lambda d:d["concepts"][1].update(visual_mechanism=d["concepts"][0]["visual_mechanism"]));self.check("duplicate mechanism")
    def test_requested_twenty(self):
        self.change("G1","reference_calibration",lambda d:d.update(requested_minimum=20));self.check("requested source count")
    def test_missing_hero_frame(self):
        self.change("G2","styleframes",lambda d:d["frames"][1].update(role="other"));self.check("hero and signature not covered")
    def test_unheard_audio(self):
        self.change("G3","audio_directions",lambda d:d["directions"][0].update(auditioned=False));self.check("missing audition")
    def test_noncausal_beat(self):
        self.change("G3","canonical_timeline",lambda d:d["beats"][0].update(consequence=""));self.check("beat b1: missing concrete")
    def test_missing_regression(self):
        self.change("G5","regression_review",lambda d:d["regressions"].pop());self.check("all 18")
    def test_missing_beat(self):
        self.change("G5","regression_review",lambda d:d.update(beats=[]));self.check("exact timeline beat IDs")
    def test_bad_motion_not_masked(self):
        self.change("G5","regression_review",lambda d:d["beats"][0]["dimensions"]["motion"].update(score=2));self.check("motion below reference")
    def test_reused_nested_media(self):
        self.change("G2","styleframes",lambda d:d["frames"][1].update(media=d["frames"][0]["media"]));self.check("duplicate underlying evidence")
    def test_remux_not_second_animatic(self):
        p=self.job/"a.mp4";q=self.job/"b.mkv"
        subprocess.run(["ffmpeg","-nostdin","-v","error","-f","lavfi","-i","testsrc2=size=160x90:rate=10","-t","1","-c:v","libx264","-threads","1",str(p)],check=True)
        subprocess.run(["ffmpeg","-nostdin","-v","error","-i",str(p),"-c","copy",str(q)],check=True)
        for k,x in [("animatic_a",p),("animatic_b",q)]:self.m["stages"]["G3"]["checks"][k]={"evidence":{"path":x.name,"sha256":a.sha(x)}}
        self.check("same decoded visual sequence","G3",True)
if __name__=="__main__":unittest.main()

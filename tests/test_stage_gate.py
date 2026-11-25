import copy, importlib.util, json, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("stage",ROOT/"scripts/stage-gate.py")
stage=importlib.util.module_from_spec(spec);spec.loader.exec_module(stage)
class StageTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.job=Path(self.tmp.name)
        self.m={"stages":{}};prev=""
        for name,keys in stage.STAGES.items():
            s={"previous_sha256":prev,"decision":"pass","reviewer":"SYNTHETIC ONLY","review_mode":"self_adversarial","checks":{},"issues":[]}
            for key in keys:
                f=self.job/(name+"-"+key+".txt");f.write_text("fixture "+name+key)
                s["checks"][key]={"decision":"pass","observation":"test","comparison":"test","reason":"test","evidence":{"path":f.name,"sha256":stage.digest(f)}}
            if name=="G5": s["master_sha256"]=s["checks"]["draft_playback"]["evidence"]["sha256"]
            self.m["stages"][name]=s;prev=stage.stage_digest(s)
    def tearDown(self): self.tmp.cleanup()
    def errors(self,through="G5",master=None,probe=False): return stage.evaluate(self.job,self.m,through,master,probe)
    def assertError(self,fragment,**kw): self.assertTrue(any(fragment in x for x in self.errors(**kw)),fragment)
    def test_complete_structural_fixture(self): self.assertEqual(self.errors(),[])
    def test_template_fails(self):
        self.m=json.loads((ROOT/"templates/stage-manifest.json").read_text());self.assertError("G0: stage not passed")
    def test_predecessor_missing(self):
        del self.m["stages"]["G2"];self.assertError("G2: missing stage")
    def test_upstream_change_invalidates(self):
        self.m["stages"]["G1"]["reviewer"]="changed";self.assertError("G2: stale")
    def test_early_stop(self):
        del self.m["stages"]["G4"];self.assertEqual(self.errors(through="G3"),[])
    def test_missing_hero(self):
        del self.m["stages"]["G4"]["checks"]["hero_test"];self.assertError("G4/hero_test")
    def test_fake_video_rejected(self): self.assertError("G3/animatic_a: invalid audiovisual",probe=True)
    def test_reused_evidence(self):
        c=self.m["stages"]["G3"]["checks"];c["animatic_b"]["evidence"]=c["animatic_a"]["evidence"];self.assertError("animatic_b: reused")
    def test_stale_file(self):
        (self.job/"G2-styleframes.txt").write_text("changed");self.assertError("styleframes: stale")
    def test_p1_open(self):
        self.m["stages"]["G1"]["issues"]=[{"id":"generic","severity":"P1","cause":"concept","description":"generic","status":"open"}];self.assertError("unresolved blocker generic")
    def test_no_master_match(self): self.assertError("G5: stale master binding",master="0"*64)
    def test_review_mode_required(self):
        self.m["stages"]["G0"]["review_mode"]="fake_agents";self.assertError("G0: reviewer/mode missing")
    def test_path_escape(self):
        self.m["stages"]["G0"]["checks"]["capacity"]["evidence"]["path"]="../missing";self.assertError("capacity: missing/empty/outside")
if __name__=="__main__":unittest.main()

"""Synthetic fixtures test structure, never artistic approval."""
import copy, importlib.util, json, subprocess, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('gate',ROOT/'scripts/release-gate.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
class HardenedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();cls.job=Path(cls.tmp.name)
        def record(name,content):
            p=cls.job/name;p.write_text(content);return cls.ref(name)
        def video(name,source):
            subprocess.run(['ffmpeg','-nostdin','-v','error','-f','lavfi','-i',source+'=size=160x90:rate=10','-f','lavfi','-i','sine=frequency=440:sample_rate=48000','-t','2','-c:v','libx264','-threads','1','-pix_fmt','yuv420p','-c:a','aac',str(cls.job/name)],check=True)
            return cls.ref(name)
        m={'master':video('master.mp4','testsrc2'),'artifacts':{},'references':[],'review':{'reviewer':'SYNTHETIC TEST ONLY','human_independent_review':True,'dimensions':{},'issues':[]}}
        for k in gate.REQUIRED:m['artifacts'][k]=record(k+'.txt','Synthetic fixture '+k)
        for k,s in [('animatic_a','testsrc'),('animatic_b','smptebars'),('shot_test','rgbtestsrc')]:m['artifacts'][k]=video(k+'.mp4',s)
        m['artifacts']['timeline']=record('timeline.json',json.dumps({'fps':10,'width':160,'height':90,'duration':2,'beats':[{'id':'b','start':0,'end':2}],'audio':[],'captions':[]}))
        subprocess.run(['python',str(ROOT/'scripts/analyze-pacing.py'),str(cls.job/'master.mp4'),'--timeline',str(cls.job/'timeline.json'),'--fps','10','--fraction','.01','--out',str(cls.job/'pacing.json')],check=True)
        p=cls.job/'pacing.json';data=json.loads(p.read_text());data['review_windows']=[{'start':0,'end':2,'decision':'intentional_hold','reason':'synthetic test only','evidence':record('window.txt','synthetic window')}];p.write_text(json.dumps(data));m['artifacts']['pacing_report']=cls.ref('pacing.json')
        for role,n in [('LOOK',5),('MOVES',3),('SOUND',3)]:
            for i in range(n):m['references'].append({'url':f'https://example.invalid/{role}/{i}','timestamp':'0s','mechanism':'synthetic','observed':True,'roles':[role],'evidence':record(f'{role}{i}.txt',f'Synthetic ref {role}{i}')})
        for k in ['visual_playback_reviewed','audio_auditioned','brand_assets_verified','claims_verified','hero_test_passed']:m[k]=True
        r=m['review'];r['master_sha256']=m['master']['sha256']
        for k in ['signed_review','playback_record','audio_audition_record','hero_review_record','blind_comparison_record']:r[k]=record(k+'.txt','Synthetic '+k)
        for k in gate.DIMENSIONS:r['dimensions'][k]={'score':4,'timestamp':'0s','comparison':'synthetic','reason':'synthetic','evidence':record('review_'+k+'.txt','Synthetic review '+k)}
        cls.manifest=m
    @classmethod
    def ref(cls,name):return {'path':name,'sha256':gate.digest(cls.job/name)}
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def check(self,m,fragment):self.assertTrue(any(fragment in e for e in gate.evaluate(self.job,m)),fragment)
    def test_complete_synthetic_fixture(self):self.assertEqual(gate.evaluate(self.job,self.manifest),[])
    def test_text_animatic(self):
        m=copy.deepcopy(self.manifest);m['artifacts']['animatic_a']=m['artifacts']['brief'];self.check(m,'animatic_a: invalid or undecodable')
    def test_duplicate_evidence(self):
        m=copy.deepcopy(self.manifest);m['artifacts']['styleframes']=m['artifacts']['brief'];self.check(m,'styleframes: duplicates evidence')
    def test_wrong_timeline(self):
        m=copy.deepcopy(self.manifest);p=self.job/'wrong.json';d=json.loads((self.job/'timeline.json').read_text());d['width']=162;p.write_text(json.dumps(d));m['artifacts']['timeline']=self.ref('wrong.json');self.check(m,'master differs from canonical timeline')
    def test_fabricated_pacing(self):
        m=copy.deepcopy(self.manifest);p=self.job/'fake.json';d=json.loads((self.job/'pacing.json').read_text());d['sampled_frames']=999;p.write_text(json.dumps(d));m['artifacts']['pacing_report']=self.ref('fake.json');self.check(m,'pacing measurement mismatch')
    def test_review_missing(self):
        m=copy.deepcopy(self.manifest);m['review']['dimensions']['motion'].pop('evidence');self.check(m,'motion review evidence: missing')
    def test_stale_review(self):
        m=copy.deepcopy(self.manifest);m['review']['master_sha256']='0'*64;self.check(m,'review does not match current master')
    def test_unresolved_issue(self):
        m=copy.deepcopy(self.manifest);m['review']['issues']=[{'id':'pacing','severity':'P1','status':'open'}];self.check(m,'unresolved blocker')
    def test_low_score(self):
        m=copy.deepcopy(self.manifest);m['review']['dimensions']['motion']['score']=2;self.check(m,'motion: missing or below')
    def test_duplicate_reference(self):
        m=copy.deepcopy(self.manifest);m['references'][1]['evidence']=m['references'][0]['evidence'];self.check(m,'LOOK: 4/5')
if __name__=='__main__':unittest.main()

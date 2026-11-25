import importlib.util
from pathlib import Path
import unittest
import numpy as np

spec=importlib.util.spec_from_file_location("pacing",Path(__file__).resolve().parents[1]/"scripts"/"analyze-pacing.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class PacingTests(unittest.TestCase):
    def test_static(self):
        a=np.zeros((4,4,3),dtype=np.uint8)
        r=m.analyze([a]*4,2)
        self.assertEqual(r["overall"]["low_fraction"],1)
        self.assertEqual(r["low_intervals"],[{"start":0,"end":1.5,"seconds":1.5}])
    def test_change_and_beats(self):
        a=np.zeros((4,4,3),dtype=np.uint8)
        b=a.copy();b[0,0,1]=255
        r=m.analyze([a,a,b,b],2,beats=[{"id":"a","start":0,"end":1},{"id":"b","start":1,"end":1.5}])
        self.assertAlmostEqual(r["overall"]["low_fraction"],2/3)
        self.assertEqual(r["beats"][0]["low_fraction"],.5)
        self.assertEqual(r["beats"][1]["low_fraction"],1)
    def test_unsigned_wrap_and_threshold(self):
        a=np.full((2,2,3),255,dtype=np.uint8)
        b=np.zeros_like(a)
        c=np.full_like(a,8)
        r=m.analyze([a,b,c],2)
        self.assertEqual(r["overall"]["low_fraction"],.5)
    def test_empty(self):
        r=m.analyze([],30)
        self.assertIsNone(r["overall"]["low_fraction"])
        self.assertEqual(r["sampled_frames"],0)

if __name__=="__main__": unittest.main()

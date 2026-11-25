#!/usr/bin/env python3
"""Offline regressions for structural timeline validation."""
import copy,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('timeline',ROOT/'scripts/validate-timeline.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
BASE=json.loads((ROOT/'templates/timeline.json').read_text(encoding='utf-8'))
class TimelineTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(module.validate(BASE),[])
    def invalid(self,modify):
        d=copy.deepcopy(BASE);modify(d);self.assertTrue(module.validate(d))
    def test_gap(self): self.invalid(lambda x:x['beats'][1].update(start=2.5))
    def test_overlap(self): self.invalid(lambda x:x['beats'][1].update(start=1))
    def test_fractional_frames(self): self.invalid(lambda x:x.update(duration=20.01))
    def test_duplicate_id(self): self.invalid(lambda x:x['beats'][1].update(id='hook'))
    def test_odd_dimension(self): self.invalid(lambda x:x.update(width=1079))
    def test_out_of_range(self): self.invalid(lambda x:x['beats'][-1].update(end=21))
    def test_missing_track(self): self.invalid(lambda x:x.pop('audio'))
if __name__=='__main__': unittest.main()

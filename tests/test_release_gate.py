import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("release_gate", root/"scripts"/"release-gate.py")
gate=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class ReleaseGateTests(unittest.TestCase):
    def test_empty_job_fails(self):
        with tempfile.TemporaryDirectory() as d:
            errors=gate.evaluate(Path(d), {})
            self.assertTrue(errors)
            self.assertIn("audio not auditioned",errors)
            self.assertIn("independent human review missing",errors)
    def test_template_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            m=json.loads((root/"templates"/"release-manifest.json").read_text())
            self.assertTrue(gate.evaluate(Path(d),m))
    def test_stale_artifact_and_identical_animatics(self):
        with tempfile.TemporaryDirectory() as d:
            job=Path(d)
            f=job/"proxy.txt";f.write_text("one")
            e={"path":"proxy.txt","sha256":gate.digest(f)}
            stale={"path":"proxy.txt","sha256":"0"*64}
            errors=gate.evaluate(job,{"artifacts":{"animatic_a":e,"animatic_b":e,"brief":stale}})
            self.assertIn("A/B animatics are identical",errors)
            self.assertIn("brief: missing or stale sha256",errors)
    def test_no_average_or_self_review(self):
        with tempfile.TemporaryDirectory() as d:
            dimensions={k:{"score":5,"timestamp":"0s","comparison":"test","reason":"synthetic"} for k in gate.DIMENSIONS}
            dimensions["motion"]["score"]=2
            errors=gate.evaluate(Path(d),{"review":{"dimensions":dimensions,"issues":[{"id":"slide","severity":"P1","status":"open"}]}})
            self.assertIn("motion: missing or below 4/5",errors)
            self.assertIn("unresolved blocker: slide",errors)
            self.assertIn("independent human review missing",errors)

if __name__=="__main__":unittest.main()

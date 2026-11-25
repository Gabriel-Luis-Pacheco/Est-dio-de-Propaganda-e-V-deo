#!/usr/bin/env python3
"""Supported full-render launcher: validates G0-G4 before starting a renderer. Not a sandbox."""
import argparse, subprocess, sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("job",type=Path);p.add_argument("command",nargs=argparse.REMAINDER);a=p.parse_args()
    job=a.job.resolve();cmd=a.command
    if cmd and cmd[0]=="--":cmd=cmd[1:]
    if not cmd:p.error("provide renderer command after --")
    code=subprocess.run([sys.executable,str(Path(__file__).with_name("stage-gate.py")),str(job),"--through","G4"]).returncode
    if code:print("FULL_RENDER_BLOCKED: repair earliest failed stage",file=sys.stderr);return code
    return subprocess.run(cmd,cwd=job).returncode
if __name__=="__main__":sys.exit(main())

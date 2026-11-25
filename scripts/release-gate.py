#!/usr/bin/env python3
"""Fail-closed evidence gate. Does not judge artistic merit or authenticate reviewers."""
import argparse, hashlib, json, math, subprocess, sys
from pathlib import Path

REQUIRED = ("brief", "claim_ledger", "brand_ledger", "reference_manifest", "styleframes",
            "animatic_a", "animatic_b", "shot_test", "timeline", "cue_sheet",
            "audio_stems", "pacing_report", "shot_review", "comparison_report",
            "revision_log", "technical_report")
DIMENSIONS = ("concept", "art_direction", "typography", "brand", "copy", "storytelling",
              "motion", "pacing", "continuity", "camera", "material", "compositing",
              "sound_design", "music", "sync", "commercial_clarity")
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""): h.update(b)
    return h.hexdigest()

def evaluate(job, manifest):
    errors=[]
    def fail(msg): errors.append(msg)
    def evidence(item, name):
        if not isinstance(item,dict): fail(name+": missing evidence"); return None
        path=item.get("path","")
        if not isinstance(path,str) or not path: fail(name+": empty path"); return None
        p=(job/path).resolve()
        if not p.is_relative_to(job.resolve()) or not p.is_file() or not p.stat().st_size:
            fail(name+": missing/empty/outside job"); return None
        if item.get("sha256") != digest(p): fail(name+": missing or stale sha256")
        return p
    if not isinstance(manifest,dict): return ["manifest is not an object"]
    master=evidence(manifest.get("master"),"master")
    artifacts=manifest.get("artifacts",{})
    if not isinstance(artifacts,dict): artifacts={}
    paths={k:evidence(artifacts.get(k),k) for k in REQUIRED}
    if paths["animatic_a"] and paths["animatic_b"] and digest(paths["animatic_a"])==digest(paths["animatic_b"]):
        fail("A/B animatics are identical")
    if master:
        try:
            probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(master)],stderr=subprocess.STDOUT))
            streams=probe["streams"]
            if not any(s["codec_type"]=="video" for s in streams): fail("no video stream")
            if not any(s["codec_type"]=="audio" for s in streams): fail("no audio stream")
            duration=float(probe["format"]["duration"])
            if not math.isfinite(duration) or duration<=0: fail("invalid duration")
        except Exception as e: fail("ffprobe failed: "+str(e))
    refs=manifest.get("references",[])
    if not isinstance(refs,list): refs=[]
    valid=[r for r in refs if isinstance(r,dict) and r.get("url") and r.get("timestamp") and r.get("mechanism") and r.get("observed") is True]
    for role,n in (("LOOK",5),("MOVES",3),("SOUND",3)):
        unique=set()
        for r in valid:
            if role in r.get("roles",[]) and evidence(r.get("evidence"),"reference "+role):
                unique.add(r["url"])
        if len(unique)<n: fail(f"{role}: {len(unique)}/{n} inspected sources")
    if manifest.get("visual_playback_reviewed") is not True: fail("linear playback not reviewed")
    if manifest.get("audio_auditioned") is not True: fail("audio not auditioned")
    if manifest.get("brand_assets_verified") is not True: fail("brand assets unverified")
    if manifest.get("claims_verified") is not True: fail("claims unverified")
    if manifest.get("hero_test_passed") is not True: fail("hero motion test not approved")
    review=manifest.get("review",{})
    if not isinstance(review,dict): review={}
    if not master or review.get("master_sha256")!=digest(master): fail("review does not match current master")
    if review.get("human_independent_review") is not True: fail("independent human review missing")
    if not isinstance(review.get("reviewer"),str) or not review["reviewer"].strip(): fail("reviewer missing")
    dimensions=review.get("dimensions",{})
    if not isinstance(dimensions,dict): dimensions={}
    for k in DIMENSIONS:
        r=dimensions.get(k,{})
        if not isinstance(r,dict): r={}
        score=r.get("score")
        if type(score) not in (int,float) or not math.isfinite(score) or not 4<=score<=5:
            fail(k+": missing or below 4/5")
        if not r.get("timestamp") or not r.get("comparison") or not r.get("reason"):
            fail(k+": missing concrete review")
    issues=review.get("issues")
    if not isinstance(issues,list): fail("issues ledger missing")
    else:
        for i in issues:
            if not isinstance(i,dict): fail("malformed issue"); continue
            if i.get("severity") in ("P0","P1") and (i.get("status")!="resolved" or not evidence(i.get("retest"),"resolved issue retest")):
                fail("unresolved blocker: "+str(i.get("id","unknown")))
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("job",type=Path)
    p.add_argument("--manifest",default="qa/release-manifest.json")
    a=p.parse_args()
    try: errors=evaluate(a.job.resolve(),json.loads((a.job/a.manifest).read_text()))
    except Exception as e: errors=["invalid/missing manifest: "+str(e)]
    print(json.dumps({"status":"EVIDENCE_GATE_BLOCKED" if errors else "EVIDENCE_GATE_PASSED",
                      "artistic_quality_certified":False,"errors":errors},indent=2,ensure_ascii=False))
    return int(bool(errors))
if __name__=="__main__": sys.exit(main())

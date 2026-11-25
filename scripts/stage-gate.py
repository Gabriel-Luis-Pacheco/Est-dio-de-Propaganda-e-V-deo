#!/usr/bin/env python3
"""Evidence gate for staged creative production; never a taste or authenticity certificate."""
import argparse, hashlib, importlib.util, json, math, subprocess, sys
from pathlib import Path

STAGES = {
 "G0": ("capacity", "brand_claims", "rights", "reference_access", "audio_access", "technical_feasibility"),
 "G1": ("reference_calibration", "five_concepts", "brand_swap", "story", "commercial_proof", "originality"),
 "G2": ("styleframes", "rejected_route", "composition", "typography_brand", "materials_light", "mobile_grayscale"),
 "G3": ("animatic_a", "animatic_b", "editorial_comparison", "canonical_timeline", "pacing", "audio_directions", "cue_sync"),
 "G4": ("hero_test", "transition_test", "signature_test", "motion_craft", "camera", "lookdev", "typography_motion", "sound_sync"),
 "G5": ("draft_playback", "mute_audio_combined", "baseline_comparison", "revision_retest", "technical_qa", "regression_review")
}
VIDEO = {"animatic_a", "animatic_b", "hero_test", "transition_test", "signature_test", "draft_playback"}
def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1048576), b""): h.update(chunk)
    return h.hexdigest()
def stage_digest(stage):
    return hashlib.sha256(json.dumps(stage,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def nonblank(x): return isinstance(x,str) and bool(x.strip())
def evaluate(job, manifest, through="G5", master_sha=None, probe=True):
    errors=[]; previous=""; seen=set(); stages=list(STAGES)
    if not isinstance(manifest,dict) or not isinstance(manifest.get("stages"),dict): return ["missing staged manifest"]
    if through not in STAGES: return ["invalid stage"]
    def evidence(item,label):
        if not isinstance(item,dict) or not nonblank(item.get("path")): errors.append(label+": missing evidence"); return None
        p=(job/item["path"]).resolve()
        if not p.is_relative_to(job.resolve()) or not p.is_file() or not p.stat().st_size: errors.append(label+": missing/empty/outside job"); return None
        h=digest(p)
        if h!=item.get("sha256"): errors.append(label+": stale evidence"); return None
        return p,h
    for name in stages[:stages.index(through)+1]:
        s=manifest["stages"].get(name)
        if not isinstance(s,dict): errors.append(name+": missing stage"); continue
        if s.get("previous_sha256")!=previous: errors.append(name+": stale or missing predecessor")
        previous=stage_digest(s)
        if s.get("decision")!="pass": errors.append(name+": stage not passed")
        if not nonblank(s.get("reviewer")) or s.get("review_mode") not in ("self_adversarial","external_human"): errors.append(name+": reviewer/mode missing")
        checks=s.get("checks",{})
        if not isinstance(checks,dict): checks={}
        for key in STAGES[name]:
            label=name+"/"+key; c=checks.get(key,{})
            if not isinstance(c,dict): c={}
            if c.get("decision")!="pass" or not all(nonblank(c.get(x)) for x in ("observation","comparison","reason")): errors.append(label+": missing concrete pass review")
            ev=evidence(c.get("evidence"),label)
            if ev:
                p,h=ev
                if h in seen: errors.append(label+": reused evidence")
                seen.add(h)
                if key in VIDEO and probe:
                    try:
                        data=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(p)],stderr=subprocess.STDOUT,timeout=30))
                        duration=float(data["format"]["duration"]); types={s["codec_type"] for s in data["streams"]}
                        if not math.isfinite(duration) or duration<=0 or "video" not in types: raise ValueError("missing video")
                        if key in {"animatic_a","animatic_b","hero_test","draft_playback"} and "audio" not in types: raise ValueError("missing guide/master audio")
                        if key=="hero_test" and not 2<=duration<=5.1: raise ValueError("hero must be 2–5s")
                        cmd=["ffmpeg","-nostdin","-v","error","-xerror","-i",str(p),"-map","0:v:0","-map","0:a:0?","-f","null","-"]
                        subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=300)
                    except Exception as e: errors.append(label+": invalid audiovisual evidence: "+str(e))
        issues=s.get("issues")
        if not isinstance(issues,list): errors.append(name+": missing issues ledger")
        else:
            ids=set()
            for issue in issues:
                if not isinstance(issue,dict) or not nonblank(issue.get("id")) or issue.get("id") in ids or issue.get("severity") not in ("P0","P1","P2","P3") or not nonblank(issue.get("cause")) or not nonblank(issue.get("description")):
                    errors.append(name+": invalid issue"); continue
                ids.add(issue["id"])
                if issue["severity"] in ("P0","P1"):
                    if issue.get("status")!="resolved" or not nonblank(issue.get("correction")): errors.append(name+": unresolved blocker "+issue["id"])
                    else: evidence(issue.get("retest"),name+"/retest/"+issue["id"])
        if name=="G5":
            if not nonblank(s.get("master_sha256")): errors.append("G5: missing master binding")
            if master_sha is not None and s.get("master_sha256")!=master_sha: errors.append("G5: stale master binding")
            draft=checks.get("draft_playback",{})
            if not isinstance(draft,dict) or not isinstance(draft.get("evidence"),dict) or draft["evidence"].get("sha256")!=s.get("master_sha256"): errors.append("G5: playback not bound to master")
    return errors
def release_bindings(stages, release):
    """Prevent a release from pointing at different animatics, hero, or timeline."""
    errors=[]
    mapping=(("G3","animatic_a","animatic_a"),("G3","animatic_b","animatic_b"),
             ("G3","canonical_timeline","timeline"),("G4","hero_test","shot_test"))
    for name,key,artifact in mapping:
        try:
            a=stages["stages"][name]["checks"][key]["evidence"]["sha256"]
            b=release["artifacts"][artifact]["sha256"]
            if not nonblank(a) or a!=b: raise ValueError("hash mismatch")
        except (KeyError,TypeError,ValueError): errors.append(name+"/"+key+": differs from release "+artifact)
    return errors

def audit(job,manifest,through):
    spec=importlib.util.spec_from_file_location("creative_audit",Path(__file__).with_name("creative-audit.py"))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.audit(job,manifest,through)
def reset(manifest,name):
    """Invalidate this stage and all descendants; preserve historical observations/issue ledger."""
    keys=list(STAGES)
    for k in keys[keys.index(name):]:
        s=manifest["stages"][k];s["decision"]="pending";s["previous_sha256"]=""
        s.pop("master_sha256",None)
        for check in s["checks"].values():
            check["decision"]="pending";check["evidence"]["sha256"]=""
    return manifest
def seal(job, manifest, name):
    """Populate hashes from existing evidence. Never changes a decision or a review."""
    s=manifest["stages"][name]; keys=list(STAGES); i=keys.index(name)
    predecessor=stage_digest(manifest["stages"][keys[i-1]]) if i else ""
    if s["decision"]=="pass" and s.get("previous_sha256") and s["previous_sha256"]!=predecessor:
        raise ValueError("stale predecessor: reset and re-review stage "+name)
    s["previous_sha256"]=predecessor
    def fill(item):
        p=(job/item["path"]).resolve()
        if not p.is_relative_to(job.resolve()) or not p.is_file() or not p.stat().st_size: raise ValueError("missing/empty/outside job: "+str(p))
        h=digest(p)
        if s["decision"]=="pass" and item.get("sha256") and item["sha256"]!=h:
            raise ValueError("changed evidence: reset and re-review stage "+name)
        item["sha256"]=h
    for key in STAGES[name]: fill(s["checks"][key]["evidence"])
    for issue in s["issues"]:
        if issue.get("status")=="resolved" and issue.get("retest"): fill(issue["retest"])
    if name=="G5": s["master_sha256"]=s["checks"]["draft_playback"]["evidence"]["sha256"]
    return manifest

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("job",type=Path); p.add_argument("--through",choices=STAGES,required=True); p.add_argument("--manifest",default="qa/stage-manifest.json"); p.add_argument("--master-sha"); p.add_argument("--seal",action="store_true",help="populate hashes for this stage only; does not approve it")
    p.add_argument("--reset",action="store_true",help="invalidate this stage and descendants")
    a=p.parse_args()
    try:
        job=a.job.resolve(); path=(job/a.manifest).resolve()
        if not path.is_relative_to(job): raise ValueError("manifest outside job")
        manifest=json.loads(path.read_text())
        if a.seal and a.reset: raise ValueError("choose --seal or --reset")
        if a.reset or a.seal:
            if a.reset: reset(manifest,a.through)
            else: seal(job,manifest,a.through)
            tmp=path.with_suffix(path.suffix+".tmp")
            tmp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n"); tmp.replace(path)
        if a.reset:
            print(json.dumps({"status":"STAGES_INVALIDATED","from":a.through})); return 0
        errors=evaluate(job,manifest,a.through,a.master_sha)
        if not errors: errors.extend(audit(job,manifest,a.through))
    except Exception as e: errors=["invalid/missing stage manifest: "+str(e)]
    print(json.dumps({"status":"STAGE_BLOCKED" if errors else "STAGE_EVIDENCE_PASSED","through":a.through,"artistic_quality_certified":False,"errors":errors},ensure_ascii=False,indent=2))
    return int(bool(errors))
if __name__=="__main__": sys.exit(main())

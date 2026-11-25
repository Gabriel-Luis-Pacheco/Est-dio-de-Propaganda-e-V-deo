#!/usr/bin/env python3
"""Fail-closed evidence gate. Does not judge artistic merit or authenticate reviewers."""
import argparse, hashlib, importlib.util, json, math, subprocess, sys
from fractions import Fraction
from urllib.parse import urlparse
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

def nonblank(x): return isinstance(x,str) and bool(x.strip())

def media(path, video=True, audio=True, decode=False):
    data=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(path)],stderr=subprocess.STDOUT,timeout=30))
    streams=data["streams"]
    duration=float(data["format"]["duration"])
    if not math.isfinite(duration) or duration<=0: raise ValueError("invalid duration")
    if video and not any(s["codec_type"]=="video" and s.get("width",0)>0 and s.get("height",0)>0 for s in streams): raise ValueError("missing video")
    if audio and not any(s["codec_type"]=="audio" for s in streams): raise ValueError("missing audio")
    if decode:
        subprocess.run(["ffmpeg","-nostdin","-v","error","-xerror","-i",str(path),"-map","0:v:0","-map","0:a:0","-f","null","-"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=300)
    return data

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
        if item.get("sha256") != digest(p): fail(name+": missing or stale sha256"); return None
        return p
    if not isinstance(manifest,dict): return ["manifest is not an object"]
    master=evidence(manifest.get("master"),"master")
    artifacts=manifest.get("artifacts",{})
    if not isinstance(artifacts,dict): artifacts={}
    paths={k:evidence(artifacts.get(k),k) for k in REQUIRED}
    if paths["animatic_a"] and paths["animatic_b"] and digest(paths["animatic_a"])==digest(paths["animatic_b"]):
        fail("A/B animatics are identical")
    used={}
    for k,p in {"master":master,**paths}.items():
        if p:
            h=digest(p)
            if h in used: fail(k+": duplicates evidence "+used[h])
            else: used[h]=k
    master_meta=None
    for k,p in (("master",master),("animatic_a",paths["animatic_a"]),("animatic_b",paths["animatic_b"]),("shot_test",paths["shot_test"])):
        if p:
            try:
                data=media(p,decode=True)
                if k=="master": master_meta=data
                if k=="shot_test" and not 2<=float(data["format"]["duration"])<=5.1: fail("shot_test: expected 2–5 seconds")
            except Exception as e: fail(k+": invalid or undecodable audiovisual media: "+str(e))
    timeline=None
    if paths["timeline"]:
        try:
            timeline=json.loads(paths["timeline"].read_text())
            fps=timeline["fps"]; duration=timeline["duration"]; width=timeline["width"]; height=timeline["height"]
            if type(fps) is not int or fps<=0 or type(width) is not int or type(height) is not int or min(width,height)<=0 or type(duration) not in (int,float) or not math.isfinite(duration) or duration<=0 or abs(duration*fps-round(duration*fps))>1e-5: raise ValueError("invalid frame grid")
            prev=0; ids=set()
            for track in ("beats","audio","captions"):
                events=timeline[track]
                if not isinstance(events,list) or (track=="beats" and not events): raise ValueError("empty or invalid "+track)
                for e in events:
                    a,b=e["start"],e["end"]
                    if not nonblank(e["id"]) or (track,e["id"]) in ids: raise ValueError("missing/duplicate event id")
                    ids.add((track,e["id"]))
                    if type(a) not in (int,float) or type(b) not in (int,float) or not 0<=a<b<=duration+1e-6: raise ValueError("event outside timeline")
                    if track!="audio" and any(abs(t*fps-round(t*fps))>1e-5 for t in (a,b)): raise ValueError("event off frame grid")
                    if track=="beats":
                        if abs(a-prev)>1e-6: raise ValueError("beat gap or overlap")
                        prev=b
            if abs(prev-duration)>1e-6: raise ValueError("beat coverage incomplete")
            if master_meta:
                v=next(s for s in master_meta["streams"] if s["codec_type"]=="video")
                if (v["width"],v["height"])!=(width,height) or Fraction(v["avg_frame_rate"])!=fps or abs(float(master_meta["format"]["duration"])-duration)>1/fps: raise ValueError("master differs from canonical timeline")
        except Exception as e: fail("timeline: "+str(e)); timeline=None
    if paths["pacing_report"]:
        try:
            pr=json.loads(paths["pacing_report"].read_text())
            if not master or pr.get("master_sha256")!=digest(master): raise ValueError("report not bound to master")
            if not paths["timeline"] or pr.get("timeline_sha256")!=digest(paths["timeline"]): raise ValueError("report not bound to timeline")
            if not timeline: raise ValueError("valid timeline required")
            method=pr.get("method",{})
            expected={"fps":timeline["fps"],"width":320,"height":180,"rgb_max_delta_gt":8,"low_changed_pixel_fraction_lt":.01}
            if any(method.get(k)!=v for k,v in expected.items()): raise ValueError("noncanonical pacing method")
            spec=importlib.util.spec_from_file_location("pacing",Path(__file__).with_name("analyze-pacing.py"))
            mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
            measured=mod.analyze(mod.decode(master,timeline["fps"],320,180),timeline["fps"],8,.01,timeline["beats"])
            for key in ("sampled_frames","compared_seconds","overall","low_intervals","per_second","beats"):
                if pr.get(key)!=measured[key]: raise ValueError("pacing measurement mismatch: "+key)
            windows=pr["review_windows"]
            if not isinstance(windows,list): raise ValueError("review_windows must be array")
            for w in windows:
                if not isinstance(w,dict) or type(w.get("start")) not in (int,float) or type(w.get("end")) not in (int,float) or not 0<=w["start"]<w["end"]<=timeline["duration"]+1e-6 or not nonblank(w.get("reason")) or w.get("decision") not in ("intentional_hold","repaired") or not evidence(w.get("evidence"),"pacing window"): raise ValueError("unreviewed suspicious window")
            if timeline and (not isinstance(pr.get("sampled_frames"),int) or abs(pr["sampled_frames"]-timeline["duration"]*timeline["fps"])>1): raise ValueError("sampling coverage differs from master")
            for interval in pr["low_intervals"]:
                if interval["seconds"]>=1 and not any(w["start"]<=interval["start"]+.04 and w["end"]>=interval["end"]-.04 for w in windows): raise ValueError("low-activity interval missing review")
            for beat in pr["beats"]:
                if beat["low_fraction"] is not None and beat["low_fraction"]>.5 and not any(w["start"]<=beat["start"]+.04 and w["end"]>=beat["end"]-.04 for w in windows): raise ValueError("low-activity beat missing review")
        except Exception as e: fail("pacing_report: "+str(e))
    refs=manifest.get("references",[])
    if not isinstance(refs,list): refs=[]
    valid=[r for r in refs if isinstance(r,dict) and nonblank(r.get("url")) and urlparse(r["url"]).scheme in ("https","http") and bool(urlparse(r["url"]).netloc) and nonblank(r.get("timestamp")) and nonblank(r.get("mechanism")) and r.get("observed") is True]
    for role,n in (("LOOK",5),("MOVES",3),("SOUND",3)):
        unique=set(); hashes=set()
        for r in valid:
            if isinstance(r.get("roles"),list) and role in r["roles"]:
                p=evidence(r.get("evidence"),"reference "+role)
                if p and digest(p) not in hashes:
                    unique.add(r["url"]); hashes.add(digest(p))
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
    if not nonblank(review.get("reviewer")): fail("reviewer missing")
    evidence(review.get("signed_review"),"independent review record")
    for key in ("playback_record","audio_audition_record","hero_review_record","blind_comparison_record"):
        evidence(review.get(key),key)
    dimensions=review.get("dimensions",{})
    if not isinstance(dimensions,dict): dimensions={}
    for k in DIMENSIONS:
        r=dimensions.get(k,{})
        if not isinstance(r,dict): r={}
        score=r.get("score")
        if type(score) not in (int,float) or not math.isfinite(score) or not 4<=score<=5:
            fail(k+": missing or below 4/5")
        if not all(nonblank(r.get(key)) for key in ("timestamp","comparison","reason")):
            fail(k+": missing concrete review")
        evidence(r.get("evidence"),k+" review evidence")
    issues=review.get("issues")
    if not isinstance(issues,list): fail("issues ledger missing")
    else:
        for i in issues:
            if not isinstance(i,dict) or i.get("severity") not in ("P0","P1","P2","P3") or not nonblank(i.get("id")): fail("malformed issue"); continue
            if i.get("severity") in ("P0","P1") and (i.get("status")!="resolved" or not evidence(i.get("retest"),"resolved issue retest")):
                fail("unresolved blocker: "+str(i.get("id","unknown")))
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("job",type=Path)
    p.add_argument("--manifest",default="qa/release-manifest.json")
    a=p.parse_args()
    try:
        job=a.job.resolve()
        manifest=json.loads((job/a.manifest).read_text())
        errors=evaluate(job,manifest)
        spec=importlib.util.spec_from_file_location("stage_gate",Path(__file__).with_name("stage-gate.py"))
        stage=importlib.util.module_from_spec(spec); spec.loader.exec_module(stage)
        try:
            stages=json.loads((job/"qa/stage-manifest.json").read_text())
            errors.extend(stage.evaluate(job,stages,"G5",manifest.get("master",{}).get("sha256")))
        except Exception as e: errors.append("stage history missing/invalid: "+str(e))
    except Exception as e: errors=["invalid/missing manifest: "+str(e)]
    print(json.dumps({"status":"EVIDENCE_GATE_BLOCKED" if errors else "EVIDENCE_GATE_PASSED",
                      "artistic_quality_certified":False,"errors":errors},indent=2,ensure_ascii=False))
    return int(bool(errors))
if __name__=="__main__": sys.exit(main())

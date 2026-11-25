#!/usr/bin/env python3
"""Structured review evidence checks; not a taste or authenticity certificate."""
import hashlib,json,math,subprocess
from pathlib import Path
REGRESSIONS=tuple("V2-%02d"%i for i in range(1,19))
BEAT_FIELDS=("before","action","consequence","novelty","camera_reason","transition_reason","reading_hold_reason","audio_cue")
BEAT_DIMENSIONS=("composition","motion","pacing","continuity","typography","commercial_clarity","sound_sync")
STAGES=("G0","G1","G2","G3","G4","G5")
def nonblank(v): return isinstance(v,str) and bool(v.strip())
def score(v): return type(v) in (int,float) and math.isfinite(v) and 4<=v<=5
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def audit(job,manifest,through="G5",probe=True):
    errors=[];seen=set()
    def fail(label,msg): errors.append(label+": "+msg)
    def file(ref,label):
        try:
            p=(job/ref["path"]).resolve()
            if not p.is_relative_to(job.resolve()) or not p.is_file() or not p.stat().st_size or sha(p)!=ref["sha256"]:raise ValueError()
            return p
        except Exception:fail(label,"invalid or stale evidence");return None
    def unique(ref,label,kind=None):
        p=file(ref,label)
        if p is None:return None
        h=sha(p)
        if h in seen:fail(label,"duplicate underlying evidence")
        seen.add(h)
        if probe and kind:
            try:
                data=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-of","json",str(p)],timeout=30))
                if kind not in {s["codec_type"] for s in data["streams"]}:raise ValueError("missing stream")
                subprocess.run(["ffmpeg","-nostdin","-v","error","-xerror","-i",str(p),"-map","0:"+("a" if kind=="audio" else "v")+":0","-f","null","-"],check=True,stderr=subprocess.PIPE,timeout=90)
            except Exception:fail(label,"not decodable "+kind+" evidence")
        return p
    def record(g,k):
        label=g+"/"+k
        try:
            p=file(manifest["stages"][g]["checks"][k]["evidence"],label)
            d=json.loads(p.read_text()) if p else None
            if not isinstance(d,dict):raise ValueError()
            return d
        except Exception:fail(label,"structured JSON record required");return {}
    def rows(d,k):
        x=d.get(k,[])
        if not isinstance(x,list) or any(not isinstance(r,dict) for r in x):fail(k,"invalid rows");return []
        ids=[r.get("id") for r in x]
        if not all(nonblank(k) for k in ids) or len(set(ids))!=len(ids):fail(k,"missing/duplicate IDs")
        return x
    def texts(r,keys,label):
        if not isinstance(r,dict) or not all(nonblank(r.get(k)) and len(r[k].strip().split())>=5 for k in keys):fail(label,"missing concrete observations/reasons")
    upto=STAGES.index(through)
    if upto>=1:
        rs=rows(record("G1","five_concepts"),"concepts")
        if len(rs)<5:fail("concepts","at least five distinct concepts")
        if sum(r.get("decision")=="selected" for r in rs)!=1 or sum(r.get("decision")=="rejected" for r in rs)!=len(rs)-1:fail("concepts","select one; reject all alternatives")
        for i,r in enumerate(rs):texts(r,("premise","visual_mechanism","brand_specificity","payoff","reason"),"concept "+str(i))
        if len({str(r.get("visual_mechanism","")).strip().casefold() for r in rs})!=len(rs):fail("concepts","duplicate mechanism")
        d=record("G1","reference_calibration");rs=rows(d,"references")
        role_urls={k:set() for k in ("LOOK","MOVES","SOUND")}
        from urllib.parse import urlparse
        for i,r in enumerate(rs):
            label="reference "+str(i);role=r.get("role");url=r.get("url","")
            if role not in role_urls or not isinstance(url,str) or urlparse(url).scheme not in ("http","https") or not urlparse(url).netloc or not nonblank(r.get("timestamp")) or r.get("observed") is not True:fail(label,"missing source/time/observation");continue
            texts(r,("mechanism","transfer","avoid"),label)
            if not nonblank(r.get("rights")):fail(label,"rights/access not recorded")
            if unique(r.get("media"),label,"audio" if role=="SOUND" else "video"):role_urls[role].add(url)
        for k,n in (("LOOK",5),("MOVES",3),("SOUND",3)):
            if len(role_urls[k])<n:fail("references",k+" minimum "+str(n))
        minimum=d.get("requested_minimum",0)
        if type(minimum) is not int or minimum<0 or len(set().union(*role_urls.values()))<minimum:fail("references","requested source count not met")
    if upto>=2:
        rs=rows(record("G2","styleframes"),"frames");accepted=[r for r in rs if r.get("decision")=="accepted"]
        if len(accepted)<3 or not any(r.get("decision")=="rejected" for r in rs):fail("styleframes","three accepted and one rejected route required")
        if not {"opening","hero","signature"}.issubset({r.get("role") for r in accepted}):fail("styleframes","opening, hero and signature not covered")
        for i,r in enumerate(rs):
            label="styleframe "+str(i);texts(r,("observation","comparison","reason"),label)
            if r.get("decision") not in ("accepted","rejected") or (r.get("decision")=="accepted" and not score(r.get("score"))):fail(label,"unapproved frame")
            unique(r.get("media"),label,"video")
    beats=[]
    if upto>=3:
        d=record("G3","canonical_timeline");beats=rows(d,"beats");fps=d.get("fps");duration=d.get("duration")
        if type(fps) is not int or fps<=0 or type(duration) not in (int,float) or not math.isfinite(duration) or duration<=0 or not beats:fail("timeline","invalid fps, duration or beats")
        else:
            prev=0
            for b in beats:
                a,z=b.get("start"),b.get("end")
                if type(a) not in (int,float) or type(z) not in (int,float) or not 0<=a<z<=duration+1e-6 or abs(a-prev)>1e-6 or any(abs(t*fps-round(t*fps))>1e-5 for t in (a,z)):fail("timeline","invalid frame grid or gap")
                else:prev=z
                texts(b,BEAT_FIELDS,"beat "+str(b.get("id")))
            if abs(prev-duration)>1e-6:fail("timeline","incomplete coverage")
        rs=rows(record("G3","audio_directions"),"directions")
        if len(rs)<3 or sum(r.get("decision")=="selected" for r in rs)!=1:fail("audio directions","three auditions, one selected")
        for i,r in enumerate(rs):
            label="audio direction "+str(i);texts(r,("intent","heard_observation","reason"),label)
            if r.get("auditioned") is not True or r.get("decision") not in ("selected","rejected") or not nonblank(r.get("rights")):fail(label,"missing audition/decision/rights")
            unique(r.get("media"),label,"audio")
        if probe:
            try:
                a=file(manifest["stages"]["G3"]["checks"]["animatic_a"]["evidence"],"animatic A")
                b=file(manifest["stages"]["G3"]["checks"]["animatic_b"]["evidence"],"animatic B")
                def fingerprint(p):
                    return subprocess.check_output(["ffmpeg","-nostdin","-v","error","-i",str(p),"-map","0:v:0","-vf","fps=10,scale=160:90,format=gray","-an","-f","hash","-hash","sha256","-"],timeout=90)
                if a and b and fingerprint(a)==fingerprint(b):fail("animatics","same decoded visual sequence; remux is not an alternative")
            except Exception:fail("animatics","decoded comparison failed")
    if upto>=5:
        d=record("G5","regression_review");rs=rows(d,"regressions")
        if not set(REGRESSIONS).issubset({r.get("id") for r in rs}):fail("regressions","all 18 known failures require explicit retest")
        for i,r in enumerate(rs):
            label="regression "+str(i);texts(r,("observation","reason"),label)
            if r.get("decision") not in ("passed","not_applicable") or not nonblank(r.get("timestamp")):fail(label,"unresolved regression")
            file(r.get("evidence"),label)
        rs=rows(d,"beats")
        if {r.get("id") for r in rs}!={b.get("id") for b in beats}:fail("beat reviews","must cover exact timeline beat IDs")
        for r in rs:
            label="beat review "+str(r.get("id"));ds=r.get("dimensions",{})
            for k in BEAT_DIMENSIONS:
                x=ds.get(k,{}) if isinstance(ds,dict) else {}
                if not isinstance(x,dict) or not score(x.get("score")):fail(label,k+" below reference or missing")
                texts(x,("observation","comparison"),label+"/"+k)
            file(r.get("evidence"),label)
    return errors

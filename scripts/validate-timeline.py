#!/usr/bin/env python3
"""Validate a timeline contract, not creative quality."""
import argparse,json,math
from pathlib import Path

def validate(doc):
    errors=[]
    def positive(v): return isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v>0
    for key in ('fps','width','height','duration'):
        if not positive(doc.get(key)): errors.append(f'{key}: positive number required')
    if errors: return errors
    d=doc['duration']; fps=doc['fps']
    for key in ('width','height','fps'):
        if doc[key]!=int(doc[key]): errors.append(f'{key}: integer required')
    if abs(d*fps-round(d*fps))>1e-5: errors.append('duration must resolve to whole frames')
    for key in ('width','height'):
        if doc[key]%2: errors.append(f'{key}: even dimension required for yuv420p')
    for track in ('beats','audio','captions'):
        events=doc.get(track)
        if not isinstance(events,list): errors.append(f'{track}: array required');continue
        if track=='beats' and not events: errors.append('beats: at least one required')
        seen=set();prev=None
        for i,e in enumerate(events):
            prefix=f'{track}[{i}]'
            if not isinstance(e,dict): errors.append(prefix+': object required');continue
            key=e.get('id')
            if not isinstance(key,str) or not key.strip() or key in seen: errors.append(prefix+': unique id required')
            else: seen.add(key)
            a,b=e.get('start'),e.get('end')
            if not (isinstance(a,(int,float)) and not isinstance(a,bool) and math.isfinite(a) and positive(b) and 0<=a<b<=d+1e-6): errors.append(prefix+': invalid time range');continue
            if track=='beats':
                if prev is None and abs(a)>1e-6: errors.append(prefix+': first beat must start at 0')
                if prev is not None and abs(a-prev)>1e-6: errors.append(prefix+': gap or overlap in narrative beats')
                prev=b
        if track=='beats' and prev is not None and abs(prev-d)>1e-6: errors.append('beats: final beat must end at duration')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',type=Path);a=p.parse_args()
    doc=json.loads(a.file.read_text(encoding='utf-8'));errors=validate(doc)
    if errors:
        print('\n'.join(errors));return 1
    print('PASS: timeline structure only; render and creative QA still required.');return 0

if __name__=='__main__': raise SystemExit(main())

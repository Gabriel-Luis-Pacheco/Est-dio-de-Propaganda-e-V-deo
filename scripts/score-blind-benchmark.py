"""Score real blind paired votes; never fabricate reviews. Input CSV columns case,rater,preferred (A/B/tie). Mapping JSON case -> label of skill, A or B."""
import csv,json,argparse
from collections import Counter
from pathlib import Path
def summarize(rows,mapping):
    seen=set();counts=Counter();per_case={}
    for r in rows:
        case=r['case'];rater=r['rater'];v=r['preferred']
        if not rater or case not in mapping or mapping[case] not in ('A','B') or v not in ('A','B','tie') or (case,rater) in seen:raise ValueError('invalid or duplicate vote')
        seen.add((case,rater));key='tie' if v=='tie' else 'skill' if v==mapping[case] else 'baseline'
        counts[key]+=1;per_case.setdefault(case,Counter())[key]+=1
    return {'n_votes':len(seen),'cases':len(per_case),'counts':dict(counts),'per_case':{k:dict(v) for k,v in per_case.items()},'note':'Exploratory descriptive counts, not statistical proof; check rater independence and P0 disqualification separately.'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('votes',type=Path);p.add_argument('mapping',type=Path);a=p.parse_args()
    with a.votes.open(encoding='utf-8',newline='') as f: print(json.dumps(summarize(csv.DictReader(f),json.loads(a.mapping.read_text())),indent=2))

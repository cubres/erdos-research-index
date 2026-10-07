import re, html, os, csv, json, sys
def clean(s):
    s=re.sub(r'<script.*?</script>','',s,flags=re.S); s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',s); t=html.unescape(re.sub(r'\s+',' ',t))
    return t
rows=[]
for fn in sorted(os.listdir('pages'), key=lambda x:int(x.split('.')[0])):
    n=fn.split('.')[0]
    raw=open('pages/'+fn).read()
    t=clean(raw)
    # statement: between 'Random Open' + status line and '#N :'
    m=re.search(r'Random Open\s+(OPEN|DECIDABLE|FALSIFIABLE|VERIFIABLE|SOLVED|PROVED|DISPROVED)[^.]*?\.\s*(.*?)\s*#'+n+r'\s*:', t, flags=re.S)
    status_line = ''
    stmt=''
    if m:
        status_line=m.group(1); stmt=m.group(2)
    else:
        m2=re.search(r'Random Open\s+(.*?)\s*#'+n+r'\s*:', t, flags=re.S)
        stmt = m2.group(1) if m2 else t[:600]
    # remarks: between '#N : [refs] tags' and 'Additional thanks'/'Proof expositions'
    m3=re.search(r'#'+n+r'\s*:(.*?)(?:Additional thanks to|Proof expositions)', t, flags=re.S)
    remarks = m3.group(1) if m3 else ''
    refs = re.findall(r'\[([A-Za-z]+\d{2}[a-z]?)\]', remarks[:400])
    def num(pat):
        mm=re.search(pat,t); return int(mm.group(1)) if mm else -1
    comments=num(r'Comments \((\d+)\)')
    claims=num(r'Proof claims \((\d+)\)')
    expos=num(r'Proof expositions \((\d+)\)')
    def react(label):
        mm=re.search(label+r'\s+(.*?)\s+(?:Looks|Could be|Working on|Open to|Currently|Previous)', t)
        v=mm.group(1).strip() if mm else ''
        return '' if v=='None' else v
    likes=react('Likes'); collab=react('Open to collaboration'); working=react('Currently working on')
    diff=react('Looks difficult'); tract=react('Looks tractable')
    finite = 'finite computation' in t[:1500]
    seealso = re.findall(r'See also \[(\d+)\]', remarks)
    rows.append(dict(number=int(n), status_line=status_line, statement=stmt.strip(), remarks=remarks.strip()[:3000],
        n_refs=len(set(refs)), comments=comments, claims=claims, expositions=expos, likes=likes, collab=collab, working=working,
        looks_difficult=diff, looks_tractable=tract, remarks_len=len(remarks), stmt_len=len(stmt)))
json.dump(rows, open('parsed.json','w'), indent=1, ensure_ascii=False)
print('parsed', len(rows))
for r in rows[:3]:
    print(json.dumps({k:(v[:300] if isinstance(v,str) else v) for k,v in r.items()}, ensure_ascii=False, indent=1))

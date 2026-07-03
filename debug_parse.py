def debug():
    rows=[]
    with open('job_roles.csv', encoding='utf-8') as f:
        for i, line in enumerate(f):
            s=line.strip().strip("'\"")
            if not s:
                continue
            parts=[p.strip() for p in s.split(',')]
            print(i, 'LINE:', repr(s))
            print('PARTS:', parts)
            role=parts[0].lower()
            skills=','.join(parts[1:]) if len(parts)>1 else ''
            rows.append({'JobRole':role, 'Skills': skills})
    print('\nROWS:')
    for r in rows:
        print(r)

if __name__=='__main__':
    debug()

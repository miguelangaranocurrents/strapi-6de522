import json, sys

d = sys.argv[1]
events = []
for line in open(d + '/0-trace.trace'):
    try:
        e = json.loads(line)
    except Exception:
        continue
    if e.get('type') == 'before':
        events.append((e.get('startTime', 0), 'ACTION', e.get('method'), json.dumps(e.get('params'))[:160]))
    if e.get('type') == 'log':
        pass
for line in open(d + '/0-trace.network'):
    try:
        e = json.loads(line)
    except Exception:
        continue
    s = e.get('snapshot', {})
    url = s.get('request', {}).get('url', '')
    if 'relations/api::article.article/authors' in url:
        body = ''
        events.append((e.get('snapshot', {}).get('_monotonicTime', 0) * 1000 if s.get('_monotonicTime') else 0, 'NET', url.split('?')[1], s.get('response', {}).get('content', {}).get('_sha1', '')))
for ev in sorted(events, key=lambda x: x[0]):
    print(ev)

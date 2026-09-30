#!/usr/bin/env python3
import json, sys

with open('biblioteca_recursos.json') as f:
    data = json.load(f)

req = ['id', 'nombre', 'url', 'tipo', 'aplicaciones']
err = []

for i, r in enumerate(data):
    for field in req:
        if field not in r:
            err.append(f'Resource #{i}: missing "{field}"')

ids = [r['id'] for r in data if 'id' in r]
dupes = set(i for i in ids if ids.count(i) > 1)
if dupes:
    err.append(f'Duplicate IDs: {dupes}')

if err:
    for e in err:
        print(f'FAIL: {e}')
    sys.exit(1)
else:
    print(f'OK: {len(data)} resources valid')

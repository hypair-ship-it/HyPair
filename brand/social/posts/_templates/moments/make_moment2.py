#!/usr/bin/env python3
"""Build the 3 moment-2 slides ("Partner dropped out?") for an event from three app screenshots.
Usage: python3 make_moment2.py <folder> "<race name for slide 1>" <date-tag>
  e.g. python3 make_moment2.py dublin-series2 "Series 2 Race 1" 9oct
Needs events/<folder>/screens/{find-a-partner,match,chat}-<folder-short>-<date-tag>.png (see SHORT below).
Uses events/birmingham/moment2-slide*.svg as the layout template. Writes moment2-slide1/2/3 (svg + png-export)."""
import re, base64, subprocess, sys, os
folder, race, tag = sys.argv[1], sys.argv[2], sys.argv[3]
short = {'dublin-series2': 'series2'}.get(folder, folder)
base = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'events'))
tpl, d = os.path.join(base, 'birmingham'), os.path.join(base, folder)
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode('ascii')
def swap(c, img): return re.sub(r'href="data:image/png;base64,[^"]+"', lambda m: 'href="data:image/png;base64,' + img + '"', c, count=1)
os.makedirs(f'{d}/png-export', exist_ok=True)
for n, (name, kind) in enumerate([('partner-dropped-out', 'find-a-partner'), ('match', 'match'), ('chat', 'chat')], 1):
    c = open(f'{tpl}/moment2-slide{n}-{name}.svg').read()
    c = swap(c, b64(f'{d}/screens/{kind}-{short}-{tag}.png'))
    if n == 1:
        old = 'Racing HYROX Birmingham without a'
        assert old in c
        c = c.replace(old, f'Racing {race} without a')
    out = f'moment2-slide{n}-{name}'
    open(f'{d}/{out}.svg', 'w').write(c)
    subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1080', '-o', f'{d}/png-export/{out}.png', f'{d}/{out}.svg'], check=True)
print('built', folder)

#!/usr/bin/env python3
"""Build the two moment-1 slides for an event from two app screenshots.
Usage: python3 make_event_slides.py <folder> "<City>" "<dates>"
  e.g. python3 make_event_slides.py london "London" "2-6 Dec"
Needs events/<folder>/screens/event-<folder>.png and find-a-partner-<folder>.png.
Uses events/johannesburg/*.svg as the layout template. Writes slide1-on-sale and slide2-match-score (svg + png-export)."""
import re, base64, subprocess, sys, os
folder, city, dates = sys.argv[1], sys.argv[2], sys.argv[3]
base = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'events'))
tpl = os.path.join(base, 'johannesburg')
d = os.path.join(base, folder)
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode('ascii')
def swap(c, img): return re.sub(r'href="data:image/png;base64,[^"]+"', lambda m: 'href="data:image/png;base64,' + img + '"', c, count=1)
def rep(c, a, b):
    assert a in c, a
    return c.replace(a, b)
def fix(c):
    # 13 Oct: "Ready to race?" (not everyone has a ticket) and a phone frame the same shape as the screenshot (no cropping or squashing)
    c = c.replace('>Got your ticket?<', '>Ready to race?<')
    for a, b in [('<rect x="580" y="127" width="420" height="826" rx="34"/>', '<rect x="606" y="118" width="388" height="844" rx="34"/>'),
                 ('<rect x="570" y="117" width="440" height="846" rx="42" fill="#000000"/>', '<rect x="596" y="108" width="408" height="864" rx="42" fill="#000000"/>'),
                 ('<image x="580" y="127" width="420" height="826"', '<image x="606" y="118" width="388" height="844"'),
                 ('<rect x="570" y="117" width="440" height="846" rx="42" fill="none"', '<rect x="596" y="108" width="408" height="864" rx="42" fill="none"')]:
        c = c.replace(a, b)
    return c
c = open(f'{tpl}/slide1-on-sale.svg').read()
c = swap(c, b64(f'{d}/screens/event-{folder}.png'))
c = rep(c, 'HYROX · JOHANNESBURG', f'HYROX · {city.upper()}')
c = rep(c, 'HYROX Johannesburg, 26–29 Nov. HyPair', f'HYROX {city}, {dates}. HyPair')
c = fix(c)
open(f'{d}/slide1-on-sale.svg', 'w').write(c)
c = open(f'{tpl}/slide2-match-score.svg').read()
c = swap(c, b64(f'{d}/screens/find-a-partner-{folder}.png'))
c = fix(c)
open(f'{d}/slide2-match-score.svg', 'w').write(c)
os.makedirs(f'{d}/png-export', exist_ok=True)
for s in ('slide1-on-sale', 'slide2-match-score'):
    subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1080', '-o', f'{d}/png-export/{s}.png', f'{d}/{s}.svg'], check=True)
print('built', folder)

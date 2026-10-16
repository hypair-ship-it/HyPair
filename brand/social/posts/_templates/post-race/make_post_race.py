#!/usr/bin/env python3
"""Build the 3-slide "after the race" carousel for an event (1080x1350 PNGs, near-black, Barlow Condensed).

Usage:
  python3 make_post_race.py race   <folder> "<Event label>" "<dates>"
      e.g. race boston "HYROX Boston" "8-11 Oct"
  python3 make_post_race.py podium <folder> "<Event label>" "<dates>"
      e.g. podium tryka-grand-finale-lisbon "Tryka Grand Finale, Lisbon" "10 Oct"

Writes events/<folder>/post-race/slide1.png, slide2.png, slide3.png (+ the .html they were rendered from).
Slide 3 uses the Find a Partner screenshot in this folder (screen-find-a-partner.png). It shows a UPCOMING race,
which is right for a post-race post. Replace it with a fresh screenshot when the countdown pill would be stale.
Rules baked in: no "5K", no arrow on buttons, no claim that HyPair lists sim events (production has none),
no Tryka in the generic variant (US/Canada copy never mentions Tryka).
"""
import os, subprocess, sys, html

variant, folder, label, dates = sys.argv[1:5]
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.normpath(os.path.join(here, '..', '..', 'events', folder, 'post-race'))
fonts = os.path.normpath(os.path.join(here, '..', '..', '..', '..', '..', 'web', 'assets', 'fonts'))
os.makedirs(out, exist_ok=True)
subprocess.run(['cp', os.path.join(here, 'screen-find-a-partner.png'), out], check=True)

COPY = {
    'race': [
        dict(eyebrow=f'{label} · {dates}', head='You did it.',
             body='Congratulations to everyone who raced. Every finisher earned it, and the ones who raced as a pair did it together.'),
        dict(eyebrow='Next time', head='The right partner is half the result.',
             body='Same pace, same goal, same race. That is what makes a doubles day feel easy and fun.'),
        dict(eyebrow='Before you enter', head='Find your partner first.',
             body='HyPair matches you by pace and goal with athletes entering the same race. Free on the App Store and Google Play.', phone=True),
    ],
    'podium': [
        dict(eyebrow=f'{label} · {dates}', head='What a finale.',
             body='Congratulations to everyone who raced in Lisbon. Hard work, on the day, in front of the best in the series.'),
        dict(eyebrow='The podium', head='Want to see yourself up there?',
             body='It starts in training. Race often, and join a local sim event near you to get used to the full race.'),
        dict(eyebrow='And a partner', head='Pick the one who gets you there.',
             body='HyPair matches you by pace and goal with athletes entering the same race. Free on the App Store and Google Play.', phone=True),
    ],
}[variant]

LOGO = '<svg viewBox="226 154 248 343"><path fill="#F2D079" d="M350,399.3c-26.8,0-48.6,21.8-48.6,48.6c0,26.8,21.8,48.6,48.6,48.6s48.6-21.8,48.6-48.6C398.6,421.1,376.8,399.3,350,399.3z M350,463.9c-8.8,0-16-7.2-16-16c0-8.8,7.2-16,16-16c8.8,0,16,7.2,16,16C366,456.7,358.8,463.9,350,463.9z"/><polygon fill="#F2D079" points="412.1,154.1 374.4,154.1 374.4,281.6 325.6,281.6 325.6,154.1 287.9,154.1 287.9,319.2 412.1,319.2"/><polygon fill="#F2D079" points="401.5,336.6 298.5,336.6 298.4,336.8 226,409.1 226,496.4 258.5,496.4 258.5,422.6 306.9,374.3 393.1,374.3 441.5,422.6 441.5,496.4 474,496.4 474,409.1"/></svg>'

CSS = f"""
@font-face{{font-family:'BC';src:url('file://{fonts}/barlow-condensed-900.woff2');font-weight:900}}
@font-face{{font-family:'BC';src:url('file://{fonts}/barlow-condensed-700.woff2');font-weight:700}}
@font-face{{font-family:'B';src:url('file://{fonts}/barlow-400.woff2');font-weight:400}}
html,body{{margin:0;padding:0;background:#0F1318}}
.post{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#0F1318;color:#fff}}
.logo{{position:absolute;left:80px;top:64px;display:flex;align-items:center;gap:14px}}
.logo svg{{width:40px;height:44px}}
.logo span{{font:700 34px 'BC';letter-spacing:2px;color:#F2D079;text-transform:uppercase}}
.stack{{position:absolute;left:80px;top:330px;width:920px}}
.stack .eyebrow,.stack .head,.stack .body{{position:static;margin:0}}
.stack .eyebrow{{margin-bottom:22px}}
.stack .body{{margin-top:44px}}
.eyebrow{{position:absolute;left:80px;font:700 26px 'BC';letter-spacing:6px;color:#F2D079;text-transform:uppercase}}
.head{{position:absolute;left:80px;width:920px;font:900 132px/0.95 'BC';text-transform:uppercase;letter-spacing:1px}}
.body{{position:absolute;left:80px;width:860px;font:400 38px/1.4 'B';color:rgba(255,255,255,0.78)}}
.dots{{position:absolute;right:80px;top:76px;display:flex;gap:10px}}
.dots i{{width:12px;height:12px;border-radius:6px;background:rgba(255,255,255,0.25)}}
.dots i.on{{background:#F2D079}}
.phone{{position:absolute;left:220px;top:640px;width:640px;height:800px;border-radius:64px 64px 0 0;background:#000;border:2px solid rgba(255,255,255,0.18);border-bottom:none;overflow:hidden}}
.screen{{position:absolute;left:14px;top:14px;width:612px;height:800px;border-radius:50px 50px 0 0;overflow:hidden;background:#13181F}}
.screen img{{position:absolute;left:0;top:0;width:612px}}
"""

for n, s in enumerate(COPY, 1):
    phone = s.get('phone')
    esc = lambda k: html.escape(s[k])
    if phone:
        inner = (f'<div class="eyebrow" style="top:170px">{esc("eyebrow")}</div>'
                 f'<div class="head" style="top:214px;font-size:104px">{esc("head")}</div>'
                 f'<div class="body" style="top:560px;font-size:32px">{esc("body")}</div>'
                 '<div class="phone"><div class="screen"><img src="screen-find-a-partner.png"></div></div>')
    else:
        inner = (f'<div class="stack"><div class="eyebrow">{esc("eyebrow")}</div>'
                 f'<div class="head">{esc("head")}</div><div class="body">{esc("body")}</div></div>')
    dots = ''.join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, 4))
    page = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body><div class="post">
<div class="logo">{LOGO}<span>HyPair</span></div><div class="dots">{dots}</div>{inner}
</div></body></html>"""
    hp = os.path.join(out, f'slide{n}.html')
    open(hp, 'w').write(page)
    subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless', '--disable-gpu',
                    f'--screenshot={out}/slide{n}.png', '--window-size=1080,1350', '--allow-file-access-from-files',
                    '--hide-scrollbars', f'file://{hp}'], check=True, capture_output=True)
print('built', out)

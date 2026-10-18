#!/usr/bin/env python3
"""Unified HyPair social post (1080x1350): H app icon only (no wordmark), small label, Barlow Condensed headline, one line of text,
one real phone screen cropped by the bottom edge, hypair.app top right.
Usage: python3 make_post.py <out.png> --theme slate|dark|cream --label "Find a partner" --head "Line one<br>Line two" --sub "One or two lines" --screen path/to/screen.png [--top 540] [--qr qr.png  (group/print posts: white QR card beside the text)]
The screen is a 1206x2622 simulator screenshot (dark theme app). Blank any countdown pill first."""
import argparse, os, subprocess, tempfile, html
ap=argparse.ArgumentParser()
ap.add_argument('out'); ap.add_argument('--theme',default='slate'); ap.add_argument('--label',required=True)
ap.add_argument('--head',required=True); ap.add_argument('--sub',default=''); ap.add_argument('--screen',required=True)
ap.add_argument('--top',type=int,default=590); ap.add_argument('--qr',default='')
a=ap.parse_args()
here=os.path.dirname(os.path.abspath(__file__))
root=os.path.normpath(os.path.join(here,'..','..','..','..'))          # brand/
fonts=os.path.join(root,'..','web','assets','fonts')
icon=os.path.join(root,'print','assets','hypair-app-icon.png')
T={'slate':dict(bg='#374D59',ink='#FFFFFF',sub='rgba(255,255,255,.78)',label='#F2D079',mark='#F2D079',url='rgba(255,255,255,.6)',shadow='rgba(0,0,0,.35)'),
   'dark': dict(bg='#0F1318',ink='#FFFFFF',sub='rgba(255,255,255,.72)',label='#F2D079',mark='#F2D079',url='rgba(255,255,255,.55)',shadow='rgba(0,0,0,.5)'),
   'cream':dict(bg='#EDE7E3',ink='#0F1117',sub='rgba(15,17,23,.72)',label='#E22424',mark='#0F1117',url='rgba(15,17,23,.55)',shadow='rgba(15,17,23,.22)')}[a.theme]
page=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
@font-face{{font-family:'BC';src:url('file://{fonts}/barlow-condensed-900.woff2');font-weight:900}}
@font-face{{font-family:'BC';src:url('file://{fonts}/barlow-condensed-700.woff2');font-weight:700}}
@font-face{{font-family:'B';src:url('file://{fonts}/barlow-500.woff2');font-weight:500}}
html,body{{margin:0;padding:0;background:{T['bg']}}}
.post{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{T['bg']};color:{T['ink']}}}
.logo{{position:absolute;left:80px;top:60px;display:flex;align-items:center;gap:14px}}
.logo img{{width:68px;height:68px;border-radius:15px}}
.logo span{{font:900 40px 'BC';letter-spacing:1px;color:{T['mark']}}}
.url{{position:absolute;right:80px;top:70px;font:700 28px 'BC';letter-spacing:2px;color:{T['url']}}}
.label{{position:absolute;left:80px;top:170px;font:700 26px 'BC';letter-spacing:6px;color:{T['label']};text-transform:uppercase}}
.head{{position:absolute;left:80px;top:214px;width:920px;font:900 92px/0.98 'BC';text-transform:uppercase;letter-spacing:1px}}
.sub{{position:absolute;left:80px;top:408px;width:920px;font:500 29px/1.45 'B';color:{T['sub']}}}
.qr{{position:absolute;right:80px;top:400px;width:150px;height:150px;border-radius:14px;background:#fff;padding:10px;box-sizing:border-box}}
.qr img{{width:130px;height:130px}}
.phone{{position:absolute;left:220px;top:{a.top}px;width:640px;height:960px;border-radius:64px 64px 0 0;background:#000;overflow:hidden;box-shadow:0 24px 50px {T['shadow']}}}
.screen{{position:absolute;left:14px;top:14px;width:612px;height:960px;border-radius:50px 50px 0 0;overflow:hidden;background:#13181F}}
.screen img{{position:absolute;left:0;top:0;width:612px}}
</style></head><body><div class="post"><div class="logo"><img src="file://{icon}"></div><div class="url">hypair.app</div>
<div class="label">{html.escape(a.label)}</div><div class="head">{a.head}</div><div class="sub">{a.sub}</div>
{('<div class="qr"><img src="file://'+os.path.abspath(a.qr)+'"></div>') if a.qr else ''}<div class="phone"><div class="screen"><img src="file://{os.path.abspath(a.screen)}"></div></div></div></body></html>"""
h=tempfile.mktemp(suffix='.html'); open(h,'w').write(page)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless','--disable-gpu','--no-first-run',f'--user-data-dir={tempfile.mkdtemp()}',f'--screenshot={os.path.abspath(a.out)}','--window-size=1080,1350','--allow-file-access-from-files','--hide-scrollbars',f'file://{h}'],capture_output=True)
print('wrote',a.out)

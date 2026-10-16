#!/usr/bin/env python3
"""Builds four A4 gym-noticeboard poster variants (HTML + PDF) into brand/print/posters-oct/. Run from brand/print/."""
import os, subprocess
HEAD='''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>HyPair gym noticeboard poster A4 - %(name)s</title><style>
@font-face { font-family: 'Barlow'; font-weight: 400; src: url('../../../web/assets/fonts/barlow-400.woff2') format('woff2'); }
@font-face { font-family: 'Barlow'; font-weight: 600; src: url('../../../web/assets/fonts/barlow-600.woff2') format('woff2'); }
@font-face { font-family: 'Barlow Condensed'; font-weight: 700; src: url('../../../web/assets/fonts/barlow-condensed-700.woff2') format('woff2'); }
@font-face { font-family: 'Barlow Condensed'; font-weight: 900; src: url('../../../web/assets/fonts/barlow-condensed-900.woff2') format('woff2'); }
@page { size: A4; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:210mm; height:297mm; background:#fff; font-family:'Barlow',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:210mm; height:297mm; padding:12mm; }
.panel { width:186mm; height:273mm; border-radius:7mm; padding:9mm 10mm; display:flex; flex-direction:column; overflow:hidden; %(panel)s }
.tile { width:%(tile)smm; height:%(tile)smm; border-radius:%(rad)smm; overflow:hidden; %(tilefx)s }
.tile img { width:100%%; height:100%%; display:block; }
h1 { font-family:'Barlow Condensed',sans-serif; font-weight:900; line-height:0.98; letter-spacing:-0.2mm; }
.sub { line-height:1.4; }
.phone img { display:block; width:100%%; height:auto; border-radius:4.5mm; }
.cap { font-family:'Barlow Condensed',sans-serif; font-weight:700; letter-spacing:0.1mm; }
.qrcard { background:#fff; border-radius:6mm; display:flex; align-items:center; gap:8mm; }
.qrcard img.code { background:#fff; border-radius:2.5mm; flex-shrink:0; }
.qrcard .t { font-family:'Barlow Condensed',sans-serif; font-weight:700; line-height:1.1; color:#0F1117; }
.qrcard .s { line-height:1.4; color:#4A5568; margin-top:2mm; }
.qrcard .s strong { color:#0F1117; }
.badges { display:flex; gap:4mm; margin-top:4mm; } .badges img { height:11mm; }
.foot { margin-top:auto; text-align:center; }
.foot .site { font-family:'Barlow Condensed',sans-serif; font-weight:700; letter-spacing:0.1mm; }
%(css)s
</style></head><body><div class="page"><div class="panel">'''
TAIL='</div></div></body></html>'
S='../../../web/assets/'
PHONES=f'''<div class="phones"><div class="phone"><img src="../assets/screens/find-partner.png"><div class="cap">Find your partner</div></div><div class="phone"><img src="../assets/screens/chat.png"><div class="cap">Say hello</div></div><div class="phone"><img src="../assets/screens/match.png"><div class="cap">Race together</div></div></div>'''
QR=f'''<div class="qrcard"><img class="code" src="{S}badges/hypair-qr-code.png"><div><div class="t">Scan to get the app</div><div class="s">Point your phone camera at the code, or search <strong>HyPair</strong> on the App Store or Google Play.</div><div class="badges"><img src="{S}badges/apple-app-store-badge-black.svg"><img src="{S}badges/google-play-badge-black.png"></div></div></div>'''
FOOT='<div class="foot"><div class="site">hypair.app</div><div class="social">Instagram &nbsp;·&nbsp; Facebook &nbsp;·&nbsp; @hypair.app</div></div>'
TILE='<div class="tile"><img src="../assets/hypair-app-icon.png"></div>'
HERO='<h1>Need a HYROX or TRYKA<br><span class="acc">doubles partner?</span></h1><p class="sub">HyPair matches you with a partner by pace, goal and the exact race you\'re entering. Find someone who\'s on the same page before race day.</p>'
MID='''
.top { display:flex; justify-content:center; padding-bottom:5mm; }
.hero { text-align:center; } .hero h1 { font-size:17mm; } .hero .sub { font-size:4.4mm; margin:3mm auto 0; max-width:150mm; }
.phones { display:flex; justify-content:center; gap:8mm; margin-top:5mm; } .phone { width:40mm; text-align:center; } .cap { font-size:5mm; margin-top:2mm; }
.qrcard { margin-top:6mm; padding:5mm 7mm; } .qrcard img.code { width:30mm; height:30mm; } .qrcard .t { font-size:8mm; } .qrcard .s { font-size:3.8mm; } .badges { margin-top:3mm; } .badges img { height:10mm; }
.foot { padding-top:4mm; } .foot .site { font-size:6.5mm; } .foot .social { font-size:3.4mm; margin-top:0.5mm; }
'''
std=f'<div class="top">{TILE}</div><div class="hero">{HERO}</div>{PHONES}{QR}{FOOT}'
V={}
V['A-dark']=dict(name='A dark',panel='background:#0F1318;',tile=30,rad=7,tilefx='',css=MID+'.hero h1{color:#fff}.acc{color:#F2D079}.hero .sub{color:rgba(255,255,255,.78)}.phone img{border:.4mm solid rgba(255,255,255,.2)}.cap{color:#fff}.foot .site{color:#F2D079}.foot .social{color:rgba(255,255,255,.7)}',body=std)
V['B-red']=dict(name='B red',panel='background:#E22424;',tile=30,rad=7,tilefx='',css=MID+'.hero h1{color:#fff}.acc{color:#0F1318}.hero .sub{color:rgba(255,255,255,.92)}.phone img{border:.6mm solid #fff}.cap{color:#fff}.foot .site{color:#fff}.foot .social{color:rgba(255,255,255,.85)}',body=std)
V['C-cream']=dict(name='C cream',panel='background:#EDE7E3;',tile=30,rad=7,tilefx='',css=MID+'.hero h1{color:#0F1117}.acc{color:#E22424}.hero .sub{color:#4A5568}.phone img{border:.4mm solid #cfc7c1}.cap{color:#0F1117}.foot .site{color:#0F1117}.foot .social{color:#4A5568}',body=std)
D_CSS='''
.brand { display:flex; align-items:center; gap:6mm; } .brand .word { font-family:'Barlow Condensed',sans-serif; font-weight:900; font-size:14mm; color:#F2D079; letter-spacing:0.3mm; }
h1 { font-size:22mm; color:#fff; margin-top:7mm; } .acc { color:#F2D079; }
.mid { display:flex; gap:9mm; margin-top:7mm; align-items:flex-start; }
.mid .phone { width:56mm; height:76mm; overflow:hidden; border-radius:5mm 5mm 0 0; flex-shrink:0; } .mid .phone img { border:.5mm solid rgba(255,255,255,.3); border-radius:5mm 5mm 0 0; }
.steps { display:flex; flex-direction:column; gap:6mm; padding-top:3mm; }
.step { display:flex; gap:5mm; align-items:center; } .step .n { width:14mm; height:14mm; border-radius:50%; background:#E22424; color:#fff; font-family:'Barlow Condensed',sans-serif; font-weight:900; font-size:9.5mm; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.step .l { font-family:'Barlow Condensed',sans-serif; font-weight:900; font-size:10.5mm; line-height:1; color:#fff; }
.note { font-size:4.6mm; line-height:1.4; color:rgba(255,255,255,.85); margin-top:2mm; }
.qrcard { margin-top:7mm; padding:5mm 7mm; } .qrcard img.code { width:36mm; height:36mm; } .qrcard .t { font-size:9mm; } .qrcard .s { font-size:4mm; } .badges { margin-top:3mm; } .badges img { height:10mm; }
.foot { padding-top:4mm; } .foot .site { font-size:7mm; color:#F2D079; } .foot .social { font-size:3.4mm; color:rgba(255,255,255,.75); margin-top:0.5mm; }
'''
D_BODY=f'''<div class="brand">{TILE}<div class="word">HyPair</div></div><h1>Need a HYROX<br>or TRYKA<br><span class="acc">doubles partner?</span></h1>
<div class="mid"><div class="phone"><img src="../assets/screens/find-partner.png"></div><div class="steps"><div class="step"><div class="n">1</div><div class="l">Find your partner</div></div><div class="step"><div class="n">2</div><div class="l">Say hello</div></div><div class="step"><div class="n">3</div><div class="l">Race together</div></div><p class="note">Matched by pace, goal and the exact race you're entering.</p></div></div>{QR}{FOOT}'''
V['D-slate-bigtype']=dict(name='D slate big type',panel='background:#374D59;',tile=28,rad=6,tilefx='',css=D_CSS,body=D_BODY)
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

import tempfile, time
def printpdf(html_path,pdf_path):
    for attempt in range(4):
        d=tempfile.mkdtemp()
        r=subprocess.run([chrome,'--headless','--disable-gpu','--no-first-run',f'--user-data-dir={d}','--print-to-pdf-no-header',f'--print-to-pdf={pdf_path}','--allow-file-access-from-files',f'file://{os.path.abspath(html_path)}'],capture_output=True)
        if r.returncode==0 and os.path.exists(pdf_path): return
        time.sleep(2)
    raise SystemExit('chrome failed for '+html_path)
os.makedirs('posters-oct',exist_ok=True)
for k,v in V.items():
    p=f'posters-oct/poster-{k}.html'
    open(p,'w').write(HEAD%v+v['body']+TAIL)
    printpdf(p,f'posters-oct/poster-{k}.pdf')
    subprocess.run(['sips','-s','format','png','-Z','1100',f'posters-oct/poster-{k}.pdf','--out',f'/tmp/print/{k}.png'],capture_output=True)
print('done')

# ---- final: cream poster (A4) and its A5 handout version ----
import re
def scale(html,k):
    def mm(m): return f"{round(float(m.group(1))*k,2)}mm"
    head,rest=html.split('</style>',1)
    head=re.sub(r'(\d+(?:\.\d+)?)mm',mm,head)
    head=head.replace('size: A4','size: A5').replace(f'{round(210*k,2)}mm',  '148mm').replace(f'{round(297*k,2)}mm','210mm')
    return head+'</style>'+rest
cream=HEAD%V['C-cream']+V['C-cream']['body']+TAIL
open('posters-oct/final-poster-A4-cream.html','w').write(cream)
open('posters-oct/final-handout-A5-cream.html','w').write(scale(cream,148/210))
for n in ('final-poster-A4-cream','final-handout-A5-cream'):
    printpdf('posters-oct/'+n+'.html',f'posters-oct/{n}.pdf')
    subprocess.run(['sips','-s','format','png','-Z','1100',f'posters-oct/{n}.pdf','--out',f'/tmp/print/{n}.png'],capture_output=True)
print('finals done')

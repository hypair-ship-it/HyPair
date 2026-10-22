#!/usr/bin/env python3
"""Builds two leaflets as PDFs into brand/print/ (the HTML they are printed from goes to brand/print/source/):
  1. athlete poster (A4) + handout (A5): "Need a partner for a HYROX or TRYKA?"
  2. gym-owner flyer (A4 + A5): "Running a HYROX or TRYKA SIM at your gym?" (QR to hypair.app/for-gyms)
Each also gets a -print copy with 3 mm bleed for the print shop.

Run from brand/print/:   python3 make_posters.py
Needs Google Chrome (headless print) and the qrcode + Pillow Python packages. Screens live in assets/screens/ (real app screenshots from
../app-screenshots/2026-10-store-listing/originals/ and, for the gym-owner flyer, ../app-screenshots/2026-10-gym-flyer-dublin/); the A5 handout is the A4 design scaled by 148/210.
Approved by Ante 16 Oct 2026.
"""
import os, re, subprocess, tempfile, time

import shutil
# Chrome/Chromium on Windows, Mac or Linux (set CHROME env var to override)
CHROME = os.environ.get('CHROME') or next((c for c in (
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chrome')) if c and os.path.exists(c)), None)
if not CHROME:
    raise SystemExit('Chrome not found: install Chrome or set the CHROME environment variable')
WEB = '../../web/assets/'
BORDER = '#E22424'  # red border around the cream panel (approved 16 Oct 2026)

HEAD = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>HyPair gym noticeboard poster A4</title><style>
@font-face { font-family: 'Barlow'; font-weight: 400; src: url('%(web)sfonts/barlow-400.woff2') format('woff2'); }
@font-face { font-family: 'Barlow'; font-weight: 600; src: url('%(web)sfonts/barlow-600.woff2') format('woff2'); }
@font-face { font-family: 'Barlow Condensed'; font-weight: 700; src: url('%(web)sfonts/barlow-condensed-700.woff2') format('woff2'); }
@font-face { font-family: 'Barlow Condensed'; font-weight: 900; src: url('%(web)sfonts/barlow-condensed-900.woff2') format('woff2'); }
@page { size: A4; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:210mm; height:297mm; background:%(border)s; font-family:'Barlow',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:210mm; height:297mm; padding:12mm; }
.panel { width:186mm; height:273mm; border-radius:7mm; padding:9mm 10mm; display:flex; flex-direction:column; overflow:hidden; background:#EDE7E3; }
.tile { overflow:hidden; } .tile img { width:100%%; height:100%%; display:block; }
h1 { font-family:'Barlow Condensed',sans-serif; font-weight:900; line-height:0.98; letter-spacing:-0.2mm; color:#0F1117; }
.acc { color:#E22424; }
.hero { text-align:center; padding-top:6mm; }
.hero h1 { font-size:19mm; }
.sub { line-height:1.4; font-size:4.6mm; margin:4mm auto 0; color:#4A5568; }
.phones { display:flex; justify-content:center; gap:6mm; margin-top:8mm; }
.phone { width:50mm; text-align:center; display:flex; flex-direction:column; justify-content:flex-end; }
.phone img { display:block; width:100%%; height:auto; border-radius:4.5mm; border:.4mm solid #cfc7c1; }
.cap { font-family:'Barlow Condensed',sans-serif; font-weight:700; letter-spacing:0.1mm; font-size:5.2mm; margin-top:2.5mm; color:#0F1117; }
.qrcard { background:#fff; border-radius:6mm; display:flex; align-items:center; gap:8mm; margin-top:10mm; padding:5mm 7mm; }
.qrcard img.code { width:30mm; height:30mm; background:#fff; border-radius:2.5mm; flex-shrink:0; }
.qrcard .t { font-family:'Barlow Condensed',sans-serif; font-weight:700; line-height:1.1; color:#0F1117; font-size:7.6mm; }
.qrcard .s { line-height:1.4; color:#4A5568; margin-top:2mm; font-size:3.8mm; } .qrcard .s strong { color:#0F1117; }
.badges { display:flex; gap:4mm; margin-top:3mm; } .badges img { height:10mm; }
.foot { margin-top:auto; text-align:center; padding-top:3mm; }
.foot .brand { display:flex; align-items:center; justify-content:center; gap:3.5mm; margin-bottom:1.5mm; }
.foot .tile { width:20mm; height:20mm; border-radius:4.6mm; }
.foot .word { font-family:'Barlow Condensed',sans-serif; font-weight:900; font-size:10mm; letter-spacing:0.2mm; color:#0F1117; }
.foot .social { font-size:4mm; color:#4A5568; }
</style></head><body><div class="page"><div class="panel">''' % {'web': WEB, 'border': BORDER}
TAIL = '</div></div></body></html>'

HERO = ('<div class="hero"><h1>Need a partner for a<br><span class="acc">HYROX or TRYKA?</span></h1>'
        '<p class="sub">Find a doubles partner who matches your pace, goals and race.</p></div>')
PHONES = ('<div class="phones">'
          '<div class="phone"><img src="assets/screens/profile.png"><div class="cap">Fill out your profile</div></div>'
          '<div class="phone"><img src="assets/screens/find-partner.png"><div class="cap">Find a race partner</div></div>'
          '<div class="phone"><img src="assets/screens/match.png"><div class="cap">Race together</div></div></div>')
QR = (f'<div class="qrcard"><img class="code" src="{WEB}badges/hypair-qr-code.png"><div>'
      '<div class="t">Your next race partner is one scan away.</div>'
      '<div class="s">Free to download. Point your phone camera at the code, or search <strong>HyPair</strong> on the App Store or Google Play.</div>'
      f'<div class="badges"><img src="{WEB}badges/apple-app-store-badge-black.svg"><img src="{WEB}badges/google-play-badge-black.png"></div>'
      '</div></div>')
FOOT = ('<div class="foot"><div class="brand"><div class="tile">'
        '<img src="assets/hypair-app-icon.png"></div></div></div>')


def scale(html, k):
    """Scale every mm value in the <style> block by k and switch the page size to A5."""
    head, rest = html.split('</style>', 1)
    head = re.sub(r'(\d+(?:\.\d+)?)mm', lambda m: f"{round(float(m.group(1)) * k, 2)}mm", head)
    head = head.replace('size: A4', 'size: A5').replace(f'{round(210 * k, 2)}mm', '148mm').replace(f'{round(297 * k, 2)}mm', '210mm')
    return head + '</style>' + rest


def print_pdf(html_path, pdf_path):
    for _ in range(4):
        r = subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-first-run', *(['--no-sandbox'] if hasattr(os, 'geteuid') and os.geteuid() == 0 else []), f'--user-data-dir={tempfile.mkdtemp()}',
                            '--print-to-pdf-no-header', f'--print-to-pdf={pdf_path}', '--allow-file-access-from-files',
                            f'file://{os.path.abspath(html_path)}'], capture_output=True)
        if r.returncode == 0 and os.path.exists(pdf_path):
            return
        time.sleep(2)
    raise SystemExit('chrome failed for ' + html_path)


def add_bleed(html, w, h, pad, b=3):
    """Same page with `b` mm of red bleed on every side, for the print shop to trim back to the trim size."""
    html = re.sub(r'@page \{ size: [^;]+;', f'@page {{ size: {w + 2*b}mm {h + 2*b}mm;', html, count=1)
    html = html.replace(f'html, body {{ width:{w}mm; height:{h}mm;', f'html, body {{ width:{w + 2*b}mm; height:{h + 2*b}mm;', 1)
    return html.replace(f'.page {{ width:{w}mm; height:{h}mm; padding:{pad}mm; }}', f'.page {{ width:{w + 2*b}mm; height:{h + 2*b}mm; padding:{round(pad + b, 2)}mm; }}', 1)


# ---- gym-owner flyer: who it is for, what the app does for a sim, how to get in touch ----
import shutil
SHOTS = '../app-screenshots/2026-10-gym-flyer-dublin/'
for name in ('gym-dashboard.png', 'gym-events-list.png', 'gym-waves.png'):
    shutil.copy(SHOTS + name, 'assets/screens/' + name)
import qrcode
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
q.add_data('https://hypair.app/for-gyms'); q.make(fit=True)
q.make_image(fill_color='black', back_color='white').save('assets/qr-for-gyms.png')

OWNER_CSS = '.hero { padding-top:0mm; } .hero h1 { font-size:14mm; } .hero h1 .acc { font-size:19mm; } .phones { margin-top:5mm; } .qrcard { margin-top:6mm; padding:4mm 7mm; } .qrcard img.code { width:42mm; height:42mm; } .foot { padding-top:2mm; } .qrcard .s { font-size:4.2mm; } .qrcard .url { font-family:"Barlow Condensed",sans-serif; font-weight:700; font-size:5.2mm; color:#E22424; margin-top:2.5mm; }'
OWNER_HERO = ('<div class="hero"><h1>Running a<br><span class="acc">HYROX or TRYKA SIM</span><br>at your gym?</h1>'
              '<p class="sub">More than event registration. Athletes find their race partner through your SIM.</p></div>')
OWNER_PHONES = ('<div class="phones">'
                '<div class="phone"><img src="assets/screens/gym-dashboard.png"><div class="cap">Set up your SIM</div></div>'
                '<div class="phone"><img src="assets/screens/gym-events-list.png"><div class="cap">Athletes find it in Events</div></div>'
                '<div class="phone"><img src="assets/screens/gym-waves.png"><div class="cap">Plan your waves</div></div></div>')
OWNER_QR = ('<div class="qrcard"><img class="code" src="assets/qr-for-gyms.png"><div>'
            '<div class="t">Bring your next SIM to HyPair.</div>'
            '<div class="s">Scan the code to find out how listing your events works.</div>'
            '<div class="url">hypair.app/for-gyms</div></div></div>')


def build(hero, phones, qr, css=''):
    return HEAD.replace('</style>', css + '</style>', 1) + hero + phones + qr + FOOT + TAIL


k = 148 / 210
sets = {
    'hypair-gym-poster-a4': (build(HERO, PHONES, QR), 'hypair-gym-handout-a5'),
    'hypair-gym-owner-flyer-a4': (build(OWNER_HERO, OWNER_PHONES, OWNER_QR, OWNER_CSS), 'hypair-gym-owner-flyer-a5'),
}
jobs = {}
for a4_name, (a4, a5_name) in sets.items():
    a5 = scale(a4, k)
    jobs[a4_name] = a4
    jobs[a5_name] = a5
    # print-shop copies: 3 mm bleed each side, ask the shop to trim to A4 / A5
    jobs[a4_name + '-print'] = add_bleed(a4, 210, 297, 12)
    jobs[a5_name + '-print'] = add_bleed(a5, 148, 210, round(12 * k, 2))
os.makedirs('source', exist_ok=True)
for name, html in jobs.items():
    # the HTML lives one folder down in source/, so asset paths go up one more level
    html = html.replace(WEB, '../' + WEB).replace('src="assets/', 'src="../assets/')
    open(f'source/{name}.html', 'w').write(html)
    print_pdf(f'source/{name}.html', name + '.pdf')
print('done')

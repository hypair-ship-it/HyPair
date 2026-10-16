import subprocess, os, tempfile
FONTS='../../../../web/assets/fonts'
LOGO_TILE='../../../../brand/print/assets/hypair-app-icon.png'
CSS=f"""
@font-face{{font-family:'BC';src:url('{FONTS}/barlow-condensed-900.woff2');font-weight:900}}
@font-face{{font-family:'BC';src:url('{FONTS}/barlow-condensed-700.woff2');font-weight:700}}
@font-face{{font-family:'B';src:url('{FONTS}/barlow-500.woff2');font-weight:500}}
html,body{{margin:0;padding:0;background:#EDE7E3}}
.post{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#EDE7E3;color:#0F1117}}
.logo{{position:absolute;left:80px;top:60px;display:flex;align-items:center;gap:14px}}
.logo img{{width:52px;height:52px;border-radius:12px}}
.logo span{{font:900 34px 'BC';letter-spacing:2px;color:#0F1117;text-transform:uppercase}}
.eyebrow{{position:absolute;left:80px;top:170px;font:700 26px 'BC';letter-spacing:6px;color:#E22424;text-transform:uppercase}}
.head{{position:absolute;left:80px;top:214px;width:920px;font:900 92px/0.98 'BC';text-transform:uppercase;letter-spacing:1px}}
.sub{{position:absolute;left:80px;top:408px;width:920px;font:500 29px/1.45 'B';color:rgba(15,17,23,.72)}}
.phone{{position:absolute;left:220px;top:540px;width:640px;height:960px;border-radius:64px 64px 0 0;background:#000;border:0;overflow:hidden;box-shadow:0 24px 50px rgba(15,17,23,.22)}}
.screen{{position:absolute;left:14px;top:14px;width:612px;height:960px;border-radius:50px 50px 0 0;overflow:hidden;background:#13181F}}
.screen img{{position:absolute;left:0;top:0;width:612px}}
"""
def page(eyebrow,head,img,sub='',top=540): return f'<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body><div class="post"><div class="logo"><img src="{LOGO_TILE}"><span>HyPair</span></div><div class="eyebrow">{eyebrow}</div><div class="head">{head}</div><div class="sub">{sub}</div><div class="phone" style="top:{top}px"><div class="screen"><img src="{img}"></div></div></div></body></html>'
slides={
 'mix-slide1-off': page('Join a race','Got a ticket?<br>Say so.','reg-ticket-off.png','Tick the box and other athletes can find you by ticket status.',top=490),
 'mix-slide1-on':  page('Join a race','Got a ticket?<br>Say so.','reg-ticket-on.png','Tick the box and other athletes can find you by ticket status.',top=490),
 'mix-slide2':     page('Find a partner','Ticket or no ticket.<br>Filter for both.','source-find-a-partner-has-ticket.png','Got a ticket, need a partner? Filter for athletes without one.<br>No ticket yet? See who already has theirs.'),
}
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for k,h in slides.items():
    open(k+'.html','w').write(h)
    subprocess.run([chrome,'--headless','--disable-gpu','--no-first-run',f'--user-data-dir={tempfile.mkdtemp()}',f'--screenshot={k}.png','--window-size=1080,1350','--allow-file-access-from-files','--hide-scrollbars',f'file://{os.path.abspath(k+".html")}'],capture_output=True)
from PIL import Image
import cv2, numpy as np
off=Image.open('mix-slide1-off.png').convert('RGB'); on=Image.open('mix-slide1-on.png').convert('RGB')
off.resize((720,900),Image.LANCZOS).save('ticket-registration-mixed.gif',save_all=True,append_images=[on.resize((720,900),Image.LANCZOS)],duration=[1700,2200],loop=0,optimize=True)
A=cv2.cvtColor(np.array(off),cv2.COLOR_RGB2BGR); B=cv2.cvtColor(np.array(on),cv2.COLOR_RGB2BGR)
vw=cv2.VideoWriter('ticket-registration-mixed.mp4',cv2.VideoWriter_fourcc(*'avc1'),30,(1080,1350))
def put(f,n):
    for _ in range(n): vw.write(f)
put(A,66)
for i in range(1,7): put(cv2.addWeighted(A,1-i/6,B,i/6,0),1)
put(B,84)
for i in range(1,7): put(cv2.addWeighted(B,1-i/6,A,i/6,0),1)
put(A,6)
vw.release()
print('built')

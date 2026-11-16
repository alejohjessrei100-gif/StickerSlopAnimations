import math, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS,DUR=1080,1920,30,5
FONT=[l for l in __import__('subprocess').check_output("fc-list : file | grep -i 'Inter' | grep -i -E 'ExtraBold|Black'",shell=True,text=True).splitlines()][0].split(':')[0].strip()
F=lambda s:ImageFont.truetype(FONT,s)
def ease_out_back(t,s=1.9):
    t=min(max(t,0),1)-1; return 1+t*t*((s+1)*t+s)
def lerp(a,b,t): return a+(b-a)*t
def grad(c1,c2):
    im=Image.new('RGB',(1,H)); 
    for y in range(H): im.putpixel((0,y),tuple(int(lerp(c1[i],c2[i],y/H)) for i in range(3)))
    return im.resize((W,H))
def bg_porch():
    im=grad((120,140,170),(70,85,110)).convert('RGBA'); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,760],fill=(98,118,150))              # siding
    for y in range(0,760,60): d.line([0,y,W,y],fill=(88,106,136),width=3)
    d.rectangle([380,160,700,700],fill=(60,78,96)); d.rectangle([400,180,680,680],fill=(120,150,170)) # door
    d.rectangle([0,1560,W,H],fill=(150,150,155))             # floor
    d.rectangle([0,1500,W,1560],fill=(120,120,125))
    return im
def bg_dark():
    im=grad((12,27,77),(30,60,130)).convert('RGBA'); d=ImageDraw.Draw(im)
    for i in range(40): d.ellipse([(i*173)%W,(i*311)%700,(i*173)%W+6,(i*311)%700+6],fill=(255,255,255,120))
    return im
def bg_red():
    im=grad((198,40,40),(120,15,25)).convert('RGBA'); d=ImageDraw.Draw(im)
    d.rectangle([0,1560,W,H],fill=(60,10,15)); return im
BG=[bg_porch(),bg_dark(),bg_red()]
def head(size,mood,skin=(236,190,150)):
    S=size*2; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([S*.06,S*.04,S*.94,S*.96],fill=skin,outline=(60,35,25),width=int(S*.025))
    d.arc([S*.1,S*.1,S*.9,S*.8],200,340,fill=(255,255,255,70),width=int(S*.03))
    hair=(70,45,30); d.pieslice([S*.05,S*.0,S*.95,S*.7],180,360,fill=hair)
    ey=S*.45
    for ex in (.34,.66):
        d.ellipse([S*ex-S*.08,ey-S*.09,S*ex+S*.08,ey+S*.09],fill='white',outline=(40,25,20),width=int(S*.012))
        d.ellipse([S*ex-S*.03,ey-S*.03,S*ex+S*.03,ey+S*.04],fill=(30,20,15))
    bw=int(S*.022)
    if mood=='shock':
        for ex in (.34,.66): d.arc([S*ex-S*.1,ey-S*.24,S*ex+S*.1,ey-S*.08],200,340,fill=hair,width=bw)
        d.ellipse([S*.43,S*.66,S*.57,S*.84],fill=(90,20,25),outline=(40,20,15),width=bw)
    elif mood=='laugh':
        for ex in (.34,.66): d.arc([S*ex-S*.1,ey-S*.2,S*ex+S*.1,ey-S*.06],200,340,fill=hair,width=bw)
        d.pieslice([S*.3,S*.58,S*.7,S*.86],0,180,fill=(100,20,30),outline=(40,20,15),width=bw)
        d.rectangle([S*.36,S*.72,S*.64,S*.735],fill='white')
    else:
        for ex in (.34,.66): d.line([S*ex-S*.09,ey-S*.14,S*ex+S*.09,ey-S*.14],fill=hair,width=bw)
        d.arc([S*.36,S*.62,S*.64,S*.78],20,160,fill=(40,20,15),width=bw)
    return im.resize((size,size),Image.LANCZOS)
def person(shirt,pants,hd,scale=1.0,arms='box'):
    w,h=420,1000; im=Image.new('RGBA',(w*2,h*2),(0,0,0,0)); d=ImageDraw.Draw(im); k=2
    d.rounded_rectangle([110*k,440*k,310*k,720*k],30*k,fill=pants+(255,))      # legs top
    d.rectangle([120*k,700*k,200*k,980*k],fill=pants); d.rectangle([220*k,700*k,300*k,980*k],fill=pants)
    d.rounded_rectangle([105*k,720*k,205*k,760*k],18,fill=(30,30,30)); 
    d.rounded_rectangle([215*k,720*k,315*k,760*k],18,fill=(30,30,30))
    d.rounded_rectangle([80*k,230*k,340*k,560*k],50*k,fill=shirt)                # torso
    d.rounded_rectangle([40*k,250*k,100*k,520*k],30*k,fill=shirt); d.rounded_rectangle([320*k,250*k,380*k,520*k],30*k,fill=shirt)
    d.ellipse([36*k,500*k,104*k,568*k],fill=(236,190,150)); d.ellipse([316*k,500*k,384*k,568*k],fill=(236,190,150))
    d.rectangle([185*k,200*k,235*k,250*k],fill=(236,190,150))
    im=im.resize((w,h),Image.LANCZOS)
    hd_img=head(250,hd); im.alpha_composite(hd_img,((w-250)//2,-10+0))
    return im
def pizza(sz):
    im=Image.new('RGBA',(sz*2,sz*2),(0,0,0,0)); d=ImageDraw.Draw(im); s=sz*2
    d.rounded_rectangle([0,s*.15,s,s*.85],16,fill=(176,120,70),outline=(110,70,40),width=6)
    d.rounded_rectangle([s*.06,s*.2,s*.94,s*.8],10,fill=(228,170,110))
    d.ellipse([s*.3,s*.3,s*.7,s*.7],fill=(215,40,40)); d.ellipse([s*.36,s*.36,s*.64,s*.64],fill=(255,205,60))
    return im.resize((sz,sz),Image.LANCZOS)
def phone(t):
    im=Image.new('RGBA',(520,980),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,520,980],70,fill=(20,20,24)); d.rounded_rectangle([18,18,502,962],56,fill=(250,250,252))
    d.rectangle([18,120,502,220],fill=(0,110,150)); d.text((50,145),"CUSTOMER ACCOUNT",font=F(34),fill='white')
    n=int(min(t*18,28))
    for i in range(28):
        x=50+(i%7)*64; y=270+(i//7)*90
        col=(235,150,40) if i<n else (225,225,228)
        d.ellipse([x,y,x+52,y+52],fill=col)
    return im
def paste_c(base,im,cx,cy,sc=1.0,rot=0,alpha=1.0):
    if sc<=0.01: return
    im=im.resize((max(1,int(im.width*sc)),max(1,int(im.height*sc))),Image.BILINEAR)
    if rot: im=im.rotate(rot,expand=True,resample=Image.BILINEAR)
    if alpha<1: a=im.getchannel('A').point(lambda v:int(v*alpha)); im.putalpha(a)
    base.alpha_composite(im,(int(cx-im.width/2),int(cy-im.height/2)))
def shadow(base,cx,cy,w,sc):
    s=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(s).ellipse([cx-w*sc/2,cy-26*sc,cx+w*sc/2,cy+26*sc],fill=(0,0,0,110))
    base.alpha_composite(s.filter(ImageFilter.GaussianBlur(14)))
def stroke_text(base,text,cx,cy,size=64,fill='white'):
    d=ImageDraw.Draw(base); f=F(size); w=d.textlength(text,font=f)
    d.text((cx-w/2+3,cy+5),text,font=f,fill=(0,0,0,150),stroke_width=9,stroke_fill=(0,0,0,150))
    d.text((cx-w/2,cy),text,font=f,fill=fill,stroke_width=9,stroke_fill='black')
MAN=person((40,70,130),(80,80,90),'laugh'); MAN_S=person((40,70,130),(80,80,90),'shock'); MAN_N=person((40,70,130),(80,80,90),'neutral')
DRV=person((200,35,35),(40,40,50),'neutral'); DRV_S=person((200,35,35),(40,40,50),'shock')
PZ=pizza(300); PH=phone(0)
# (start,end,bg), captions (t0,t1,text)
SC=[(0,1.7,0),(1.7,3.4,1),(3.4,5.0,2)]
CAP=[(0,.55,"a man"),(.55,1.15,"in Oregon"),(1.15,1.7,"ordered"),(1.7,2.3,"Domino's"),(2.3,2.9,"every day"),(2.9,3.4,"for 7 years"),
     (3.4,4.0,"Then"),(4.0,4.5,"the orders"),(4.5,5.0,"stopped")]
def frame(i):
    t=i/FPS
    sid=[k for k,(a,b,_) in enumerate(SC) if a<=t<b][-1]; a,b,bgi=SC[sid]; lt=t-a; ld=(t-a)/(b-a)
    bgim=BG[bgi].copy()
    z=1+0.06*ld; bgim=bgim.resize((int(W*z),int(H*z)),Image.BILINEAR).crop(((int(W*z)-W)//2,(int(H*z)-H)//2,(int(W*z)-W)//2+W,(int(H*z)-H)//2+H))
    im=bgim
    if sid==0:
        sc=1+0.12*ld; shadow(im,540,1560,380,sc)
        m=MAN if lt<1.15 else MAN_N
        paste_c(im,m,540,1560-500*sc,sc,math.sin(lt*6)*1.0)
        paste_c(im,PZ,540,1180-0*sc,ease_out_back(lt/0.25)*1.0*(0.9+0.1*ld),-6*0+0)
        stroke_text(im,"2016",540,300,120,(255,216,77)) if lt>0.6 else None
    elif sid==1:
        p=phone(lt); paste_c(im,p,540,1000,ease_out_back(lt/0.3)*(1+0.05*ld))
        if lt>0.9:
            s=ease_out_back((lt-0.9)/0.25); paste_c(im,Image.new('RGBA',(1,1)),0,0,0)
            bw=Image.new('RGBA',(640,200),(0,0,0,0)); d=ImageDraw.Draw(bw); d.rounded_rectangle([0,0,640,200],36,fill=(255,216,77),outline='black',width=8)
            d.text((320,100),"7 YEARS",font=F(100),fill=(20,20,20),anchor='mm'); paste_c(im,bw,540,330,s,-4)
    else:
        sc=1+0.10*ld; shadow(im,540,1560,380,sc)
        who=DRV if lt<0.9 else DRV_S
        paste_c(im,who,540+lerp(-700,0,min(lt/0.35,1)) if lt<0.35 else 540,1560-500*sc,sc)
        if lt>0.8:
            s=ease_out_back((lt-0.8)/0.25); q=Image.new('RGBA',(300,300),(0,0,0,0)); dq=ImageDraw.Draw(q)
            dq.ellipse([0,0,300,260],fill='white',outline='black',width=8); dq.text((150,125),"?",font=F(200),fill=(200,35,35),anchor='mm'); paste_c(im,q,820,520,s)
    cap=[c for c in CAP if c[0]<=t<c[1]]
    if cap:
        c=cap[0]; pop=1+0.0
        stroke_text(im,c[2],540,1345+(0 if sid!=1 else 120),64)
    return im.convert('RGB')
import os
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
for i in range(FPS*DUR): frame(i).save(f'{out}/f{i:04d}.png')

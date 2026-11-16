import math,os
from PIL import Image,ImageDraw,ImageFilter
S=2048; CX=1024; CY=1040; RX=780; RY=860
OUT='/home/user/StickerSlopAnimations/assets/heads'; os.makedirs(OUT,exist_ok=True)
INK=(58,34,24)
def sh(c,f): return tuple(max(0,min(255,int(v*f))) for v in c)
CH={ # name: skin, hair, style, extras
 'everyman':dict(skin=(238,192,152),hair=(72,46,30),style='short'),
 'baker':dict(skin=(142,92,62),hair=(28,20,18),style='curlybun'),
 'elder':dict(skin=(236,196,168),hair=(190,190,195),style='balding',extra=['mustache','glasses']),
 'exec':dict(skin=(205,150,110),hair=(24,22,24),style='slick',extra=['stubble']),
 'teen':dict(skin=(244,208,176),hair=(222,176,72),style='messy'),
 'granny':dict(skin=(240,204,180),hair=(235,235,240),style='bun',extra=['glasses']),
}
EXPR=['neutral','laugh','shock','angry','sad','sleepy','smug','worried']
def poly_arc(d,box,a0,a1,fill,w):
    d.arc(box,a0,a1,fill=fill,width=w)
def brow(d,x,y,w,ang,th,col,flip=1):
    dx=math.cos(math.radians(ang))*w/2; dy=math.sin(math.radians(ang))*w/2*flip
    d.line([x-dx,y+dy,x+dx,y-dy],fill=col,width=th)
    d.ellipse([x-dx-th/2,y+dy-th/2,x-dx+th/2,y+dy+th/2],fill=col); d.ellipse([x+dx-th/2,y-dy-th/2,x+dx+th/2,y-dy+th/2],fill=col)
def make(name,ex):
    c=CH[name]; skin=c['skin']; hair=c['hair']
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    OW=62
    if ex=='angry': skin=(min(255,skin[0]+12),int(skin[1]*.84),int(skin[2]*.82))
    if c['style'] in('curlybun','bun'):  # bun behind
        bx,by=CX,CY-RY-40
        if c['style']=='bun':
            d.ellipse([bx-190,by-150,bx+190,by+150],fill=hair,outline=INK,width=OW//2)
        else:
            for k in range(7):
                a=math.radians(k*51); d.ellipse([bx+math.cos(a)*150-130,by+math.sin(a)*100-130,bx+math.cos(a)*150+130,by+math.sin(a)*100+130],fill=hair,outline=INK,width=OW//2)
    # ears
    for sx in(-1,1):
        ex_=CX+sx*(RX-10); d.ellipse([ex_-110,CY-110,ex_+110,CY+130],fill=skin,outline=INK,width=OW)
        d.ellipse([ex_-45,CY-40,ex_+45,CY+60],fill=sh(skin,.86))
    # head
    d.ellipse([CX-RX,CY-RY,CX+RX,CY+RY],fill=skin,outline=INK,width=OW)
    # shading crescent (bottom-right) clipped to head
    m=Image.new('L',(S,S),0); md=ImageDraw.Draw(m); md.ellipse([CX-RX+OW//2,CY-RY+OW//2,CX+RX-OW//2,CY+RY-OW//2],fill=255)
    shd=Image.new('RGBA',(S,S),(0,0,0,0)); sd=ImageDraw.Draw(shd)
    sd.ellipse([CX-RX-120,CY-RY-140,CX+RX-120,CY+RY-80],fill=(0,0,0,255)); inv=Image.eval(shd.getchannel('A'),lambda v:255-v)
    over=Image.new('RGBA',(S,S),sh(skin,.82)+(255,)); a=Image.composite(inv,Image.new('L',(S,S),0),m)
    over.putalpha(a.point(lambda v:int(v*.9))); im.alpha_composite(over)
    d=ImageDraw.Draw(im)
    # cheeks blush
    bl=Image.new('RGBA',(S,S),(0,0,0,0)); bd=ImageDraw.Draw(bl)
    for sx in(-1,1): bd.ellipse([CX+sx*430-150,CY+150-90,CX+sx*430+150,CY+150+90],fill=(230,90,90,70))
    im.alpha_composite(bl.filter(ImageFilter.GaussianBlur(30))); d=ImageDraw.Draw(im)
    # hair front (mask based)
    st=c['style']
    def ell(box,v=255):
        mm=Image.new('L',(S,S),0); ImageDraw.Draw(mm).ellipse(box,fill=v); return mm
    def sub(m1,m2): return Image.composite(Image.new('L',(S,S),0),m1,m2)
    def inter(m1,m2): return Image.composite(m1,Image.new('L',(S,S),0),m2)
    def rect(x0,y0,x1,y1):
        mm=Image.new('L',(S,S),0); ImageDraw.Draw(mm).rectangle([x0,y0,x1,y1],fill=255); return mm
    hm=None
    if st in('short','messy','slick','curlybun','bun'):
        outer=ell([CX-RX-26,CY-RY-26,CX+RX+26,CY+RY+26])
        if st=='messy':
            for k in range(7):
                x=CX-560+k*187; r=150+(k%2)*40; outer=Image.composite(Image.new('L',(S,S),255),outer,ell([x-r,CY-RY-60-r*.4,x+r,CY-RY-60+r*1.6]))
        if st=='slick': outer=Image.composite(Image.new('L',(S,S),255),outer,ell([CX-RX+40,CY-RY-110,CX+RX+60,CY-RY+500]))
        hm=inter(outer,rect(0,0,S,CY-60))
        fh=ell([CX-(640 if st!='slick' else 600),CY-RY+(330 if st!='slick' else 290),CX+(640 if st!='slick' else 600),CY-RY+(1330 if st!='slick' else 1290)])
        hm=sub(hm,fh)
        if st=='slick':   # side part sweep
            hm=sub(hm,ell([CX-RX+240,CY-RY+210,CX-60,CY-RY+700]) if False else Image.new('L',(S,S),0))
    elif st=='balding':
        outer=ell([CX-RX-26,CY-RY-26,CX+RX+26,CY+RY+26])
        hm=inter(inter(outer,rect(0,CY-320,S,CY+60)),Image.eval(ell([CX-590,CY-1200,CX+590,CY+700]),lambda v:255-v))
    if hm is not None:
        hm=hm.filter(ImageFilter.GaussianBlur(1.2)).point(lambda v:255 if v>127 else 0)
        edge=hm.filter(ImageFilter.GaussianBlur(14)).point(lambda v:255 if v>8 else 0)
        ink=Image.composite(Image.new('L',(S,S),0),edge,hm)
        L=Image.new('RGBA',(S,S),INK+(255,)); L.putalpha(ink); im.alpha_composite(L)
        F=Image.new('RGBA',(S,S),hair+(255,)); F.putalpha(hm); im.alpha_composite(F)
        # highlight stripe
        Hh=Image.new('RGBA',(S,S),(0,0,0,0)); hd=ImageDraw.Draw(Hh); hd.arc([CX-RX+160,CY-RY-60,CX+RX-160,CY-RY+620],205,260,fill=sh(hair,1.7)+(255,),width=40)
        Hh.putalpha(Image.composite(Hh.getchannel('A'),Image.new('L',(S,S),0),hm)); im.alpha_composite(Hh)
        # hairline outline
        d=ImageDraw.Draw(im)
    d=ImageDraw.Draw(im)
    # eyes
    ey=CY-70; exs=(CX-280,CX+280)
    ew,eh=135,160; pup=62
    for i,x in enumerate(exs):
        s=-1 if i==0 else 1
        if ex=='sleepy':
            d.arc([x-ew,ey-60,x+ew,ey+90],20,160,fill=INK,width=44)
        elif ex=='laugh':
            d.arc([x-ew,ey-60,x+ew,ey+90],200,340,fill=INK,width=46)
        else:
            e_h=eh+(40 if ex=='shock' else 0)-(35 if ex in('angry','smug') else 0)
            d.ellipse([x-ew,ey-e_h,x+ew,ey+e_h],fill='white',outline=INK,width=36)
            po=(0,0)
            if ex=='smug': po=(25*s*-1,10)
            if ex=='sad': po=(0,35)
            if ex=='worried': po=(15*s*-1,25)
            pr=pup-(22 if ex=='shock' else 0)
            d.ellipse([x+po[0]-pr,ey+po[1]-pr,x+po[0]+pr,ey+po[1]+pr],fill=(28,18,14))
            d.ellipse([x+po[0]-pr*.35+12,ey+po[1]-pr*.55,x+po[0]+pr*.1+12,ey+po[1]-pr*.1],fill='white')
            if ex=='smug': d.rectangle([x-ew-10,ey-e_h-5,x+ew+10,ey-25],fill=skin); d.line([x-ew,ey-25,x+ew,ey-25],fill=INK,width=36)
            if ex=='angry': d.polygon([(x-ew-30,ey-e_h-20),(x+ew+30,ey-e_h-20),(x+ew+30,ey-e_h+60+s*-45),(x-ew-30,ey-e_h+60+s*45)],fill=skin)
        # brows
        thick=44 if name!='elder' else 52; bc=hair if name!='granny' else (200,200,205)
        by=ey-250
        if ex=='neutral': brow(d,x,by,230,0,thick,bc)
        elif ex=='laugh': brow(d,x,by-30,230,12,thick,bc,s)
        elif ex=='shock': brow(d,x,by-90,240,0,thick,bc)
        elif ex=='angry': brow(d,x,by+30,260,-26,thick+10,bc,(1 if i==0 else -1))
        elif ex=='sad' or ex=='worried': brow(d,x,by-10,240,22,thick,bc,(1 if i==0 else -1))
        elif ex=='smug': brow(d,x,by-(60 if i else 0),240,(10 if i else 0),thick,bc,s)
        elif ex=='sleepy': brow(d,x,by+20,230,-6,thick,bc)
    # nose
    d.arc([CX-90,CY+10,CX+90,CY+170],20,160,fill=INK,width=36)
    # mouth
    my=CY+400
    if ex=='neutral': d.arc([CX-190,my-130,CX+190,my+60],20,160,fill=INK,width=46)
    elif ex=='laugh':
        d.pieslice([CX-300,my-200,CX+300,my+250],0,180,fill=(110,22,34),outline=INK,width=44)
        d.chord([CX-270,my-170,CX+270,my+40],0,180,fill='white'); d.line([CX-290,my-100,CX+290,my-100],fill=INK,width=0)
        d.pieslice([CX-300,my-200,CX+300,my+250],0,180,fill=None,outline=INK,width=44)
        d.chord([CX-170,my+30,CX+170,my+230],200,340,fill=(220,90,100))
        d.arc([CX-300,my-200,CX+300,my+250],0,180,fill=INK,width=44)
        d.line([CX-296,my+25,CX+296,my+25],fill=INK,width=44)
    elif ex=='shock': d.ellipse([CX-110,my-110,CX+110,my+150],fill=(100,20,30),outline=INK,width=44)
    elif ex=='angry':
        d.rounded_rectangle([CX-240,my-60,CX+240,my+110],40,fill='white',outline=INK,width=44)
        for k in range(-3,4): d.line([CX+k*68,my-60,CX+k*68,my+110],fill=INK,width=16)
        d.line([CX-240,my+25,CX+240,my+25],fill=INK,width=16)
    elif ex in('sad','worried'):
        d.arc([CX-190,my-10,CX+190,my+210],200,340,fill=INK,width=46)
        if ex=='sad':
            for x in exs: d.polygon([(x,ey+eh+10),(x-45,ey+eh+110),(x+45,ey+eh+110)],fill=(120,190,240)); d.ellipse([x-45,ey+eh+75,x+45,ey+eh+145],fill=(120,190,240))
    elif ex=='sleepy':
        d.ellipse([CX-85,my-60,CX+85,my+110],fill=(100,20,30),outline=INK,width=40)
    elif ex=='smug':
        d.arc([CX-190,my-150,CX+250,my+70],10,120,fill=INK,width=46); d.line([CX+230,my-10,CX+270,my-50],fill=INK,width=36)
    # extras
    for e in c.get('extra',[]):
        if e=='mustache': d.pieslice([CX-300,my-230,CX+300,my-10],180,360,fill=hair,outline=INK,width=26)
        if e=='stubble':
            ov=Image.new('RGBA',(S,S),(0,0,0,0)); od=ImageDraw.Draw(ov); od.ellipse([CX-RX+60,CY-100,CX+RX-60,CY+RY-30],fill=(40,30,30,70)); od.ellipse([CX-RX+180,CY-300,CX+RX-180,CY+RY-220],fill=(0,0,0,0)); ov.putalpha(Image.composite(ov.getchannel('A'),Image.new('L',(S,S),0),m)); im.alpha_composite(ov); d=ImageDraw.Draw(im)
        if e=='glasses':
            for x in exs: d.ellipse([x-210,ey-210,x+210,ey+210],outline=(30,30,36),width=34)
            d.line([exs[0]+210,ey,exs[1]-210,ey],fill=(30,30,36),width=34)
    if ex=='sleepy':
        for k,(zx,zy,zs) in enumerate([(CX+RX-100,CY-RY+120,150),(CX+RX+40,CY-RY-40,110)]):
            pass
    return im.crop((0,CY-RY-330,S,CY+RY+60)).resize((1024,int(1024*(2*RY+390)/S)),Image.LANCZOS)
def mystery():
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([CX-RX,CY-RY,CX+RX,CY+RY],fill=(18,18,22),outline=(0,0,0),width=OW if False else 40)
    for sx in(-1,1): d.ellipse([CX+sx*(RX-10)-110,CY-110,CX+sx*(RX-10)+110,CY+130],fill=(18,18,22))
    d.ellipse([CX-RX,CY-RY,CX+RX,CY+RY],fill=(18,18,22))
    from PIL import ImageFont
    f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Black.otf' if os.path.exists('/usr/share/fonts/opentype/inter/Inter-Black.otf') else '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf',1000)
    d.text((CX,CY),'?',font=f,fill='white',anchor='mm')
    return im.crop((0,CY-RY-330,S,CY+RY+60)).resize((1024,int(1024*(2*RY+390)/S)),Image.LANCZOS)
if __name__=='__main__':
    sheet=Image.new('RGB',(len(EXPR)*260,(len(CH)+1)*300),(70,150,120))
    for r,n in enumerate(CH):
        os.makedirs(f'{OUT}/{n}',exist_ok=True)
        for k,e in enumerate(EXPR):
            h=make(n,e); h.save(f'{OUT}/{n}/{n}_{e}.png')
            t=h.copy(); t.thumbnail((250,290)); sheet.paste(t,(k*260+5,r*300+5),t)
        print(n,flush=True)
    m=mystery(); m.save(f'{OUT}/mystery_question.png'); t=m.copy(); t.thumbnail((250,290)); sheet.paste(t,(5,len(CH)*300+5),t)
    sheet.save(f'{OUT}/_contact_sheet.png')

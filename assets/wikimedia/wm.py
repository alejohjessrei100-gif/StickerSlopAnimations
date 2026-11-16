import json,time,csv,os,re,subprocess,html,sys,urllib.parse
from PIL import Image,ImageDraw
UA='StyleResearchBot/1.0 (personal video-asset research)'
OUT='/home/user/StickerSlopAnimations/assets/wikimedia'; os.makedirs(OUT+'/thumbs',exist_ok=True)
Q={
 'period_street_1930s':['1930s street photograph','1930s american diner','1930s hamburger stand'],
 'london_ww2':['London Blitz bombed street','St Paul\'s Cathedral Blitz','London bread queue wartime','bakery wartime Britain'],
 'ration_newspaper':['ration book 1940s','newspaper front page 1940s','1940s bread loaf'],
 'maps':['antique map of Italy','antique atlas map Europe','antique map United States 19th century','map Korea antique'],
 'interiors':['courtroom interior','prison cell interior','bakery interior','restaurant kitchen interior'],
 'landmarks_skies':['Statue of Liberty sky','Nashville skyline night','Stockholm 18th century painting'],
}
OKLIC=re.compile(r'(public domain|cc0|cc by|ogl|pd)',re.I)
def api(params):
    for a in range(5):
        r=subprocess.run(['curl','-sS','-m','30','-A',UA,'-w','\n%{http_code}','https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(params)],capture_output=True,text=True)
        body,code=r.stdout.rsplit('\n',1)
        if code=='200': return json.loads(body)
        time.sleep(6*(a+1))
    return {}
rows=[];
for cat,qs in Q.items():
    for q in qs:
        d=api({'action':'query','generator':'search','gsrsearch':q+' filetype:bitmap','gsrnamespace':6,'gsrlimit':8,'prop':'imageinfo','iiprop':'url|size|mime|extmetadata','iiurlwidth':360,'format':'json'})
        time.sleep(3)
        for p in sorted(d.get('query',{}).get('pages',{}).values(),key=lambda x:x.get('index',0)):
            ii=p['imageinfo'][0]; m=ii['extmetadata']
            if ii['mime'] not in('image/jpeg','image/png') or ii['width']<1000: continue
            lic=m.get('LicenseShortName',{}).get('value','?')
            if not OKLIC.search(lic): continue
            art=re.sub('<[^>]+>','',html.unescape(m.get('Artist',{}).get('value','') or ''))[:60]
            rows.append(dict(category=cat,query=q,title=p['title'][5:],width=ii['width'],height=ii['height'],license=lic,author=art,file_page=ii['descriptionurl'],original=ii['url'],thumb=ii['thumburl']))
        print(cat,q,len(rows),flush=True)
seen=set(); R=[]
for r in rows:
    if r['title'] in seen: continue
    seen.add(r['title']); R.append(r)
for i,r in enumerate(R):
    r['id']=f"{r['category'][:6]}_{i:03d}"; fp=f"{OUT}/thumbs/{r['id']}.jpg"
    if not os.path.exists(fp):
        for a in range(3):
            c=subprocess.run(['curl','-sS','-m','40','-A',UA,'-o',fp,'-w','%{http_code}',r['thumb']],capture_output=True,text=True).stdout
            if c=='200': break
            time.sleep(5*(a+1))
        time.sleep(1.2)
    r['ok']=os.path.exists(fp) and os.path.getsize(fp)>2000
R=[r for r in R if r['ok']]
with open(OUT+'/catalog.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','category','query','title','width','height','license','author','file_page','original']); w.writeheader()
    for r in R: w.writerow({k:r[k] for k in w.fieldnames})
cats={}
for r in R: cats.setdefault(r['category'],[]).append(r)
for cat,L in cats.items():
    cols=6; tw,th=200,260; rows_=(len(L)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows_*(th+16)),'white'); d=ImageDraw.Draw(M)
    for k,r in enumerate(L):
        im=Image.open(f"{OUT}/thumbs/{r['id']}.jpg").convert('RGB'); im.thumbnail((tw-4,th-4))
        x,y=(k%cols)*tw,(k//cols)*(th+16); M.paste(im,(x+2,y+2)); d.text((x+4,y+th),f"{r['id'][-3:]} {r['license'][:16]}",fill='black')
    M.save(f'{OUT}/sheet_{cat}.png')
print({c:len(l) for c,l in cats.items()},len(R))

# -*- coding: utf-8 -*-
import math
RE=6371.0
GR = dict(gunes=696000, merkur=2439.7, venus=6051.8, dunya=6371, mars=3389.5,
          ceres=473, jupiter=71492, saturn=60268, uranus=25559, neptun=24764,
          pluton=1188, eris=1163,
          ay=1737.4, phobos=11.1, deimos=6.2, io=1821.6, europa=1560.8,
          ganymede=2634.1, callisto=2410.3, titan=2574.7, enceladus=252.1,
          miranda=235.8, triton=1353.4, charon=606)
UYDU = dict(ay=('dunya',384400), phobos=('mars',9376), deimos=('mars',23463),
            io=('jupiter',421700), europa=('jupiter',671100), ganymede=('jupiter',1070400),
            callisto=('jupiter',1882700), enceladus=('saturn',238040), titan=('saturn',1221870),
            miranda=('uranus',129900), triton=('neptun',354800), charon=('pluton',19591))
YOR = dict(merkur=(52,0.108), venus=(73,0.004), dunya=(86,0.009), mars=(107,0.049),
           ceres=(146,0.041), jupiter=(203,0.025), saturn=(279,0.028),
           uranus=(401,0.025), neptun=(506,0.004), pluton=(579,0.131))
HALKA = dict(saturn=2.3, uranus=1.9)
SIRA=['merkur','venus','dunya','mars','ceres','jupiter','saturn','uranus','neptun','pluton']
CIFT=[(SIRA[i],SIRA[i+1]) for i in range(len(SIRA)-1) if SIRA[i]!='neptun']
def bosluk(a,b):
    a1,e1=YOR[a]; a2,e2=YOR[b]; return a2*(1-e2)-a1*(1+e1)

def coz(E,P,M,SIN=1.55,PAY=0.16,ZEMIN=0.04,FTAVAN=60.0):
    r={k:max(ZEMIN,E*(v/RE)**P) for k,v in GR.items()}
    def ic(g): return max(r[g]*SIN, r[g]*HALKA.get(g,0)*1.18)
    def uyd(g): return sorted([u for u,(gg,_) in UYDU.items() if gg==g], key=lambda u:UYDU[u][1])
    def enAz(g):
        ul=uyd(g)
        return ic(g)+max(r[u] for u in ul) if ul else max(r[g]*1.3, r[g]*HALKA.get(g,0)*1.05)
    def uzan(g,F):                       # F = erim (gezegen yaricapi cinsinden)
        ul=uyd(g)
        if not ul: return enAz(g)
        return max(enAz(g), r[g]*F + max(r[u] for u in ul))
    # max-min adil: once herkese ortak en buyuk F, sonra yeri olana ayrica buyut
    def uygun(Fs):
        for a,b in CIFT:
            if uzan(a,Fs[a])+uzan(b,Fs[b])+max(4.0,bosluk(a,b)*PAY) > bosluk(a,b)+1e-9:
                return False
        return True
    lo,hi=0.0,FTAVAN
    for _ in range(60):
        md=(lo+hi)/2
        if uygun({g:md for g in SIRA}): lo=md
        else: hi=md
    F={g:lo for g in SIRA}
    for _ in range(30):                  # yeri olan sistemleri ayrica buyut
        for g in SIRA:
            lo2,hi2=F[g],FTAVAN
            for _ in range(40):
                md=(lo2+hi2)/2; F[g]=md
                if uygun(F): lo2=md
                else: hi2=md
            F[g]=lo2
    ua={}
    for g in SIRA:
        ul=uyd(g)
        if not ul: continue
        w=[(UYDU[u][1]/GR[g])**M for u in ul]
        i0=ic(g)+r[ul[0]]; d0=max(i0, uzan(g,F[g])-r[ul[-1]])
        if len(ul)==1: ua[ul[0]]=d0
        else:
            A=(d0-i0)/(w[-1]-w[0]); B=i0-A*w[0]
            for u,wi in zip(ul,w): ua[u]=A*wi+B
        # sikistirma tek yonlu: hicbir uydu gercekte oldugundan UZAGA konmaz
        for u in ul: ua[u]=min(ua[u], (UYDU[u][1]/GR[g])*r[g])
    return r,ua,F

def denetle(r,ua):
    h=[]
    ad=sorted(GR)
    for i in range(len(ad)):
        for j in range(i+1,len(ad)):
            a,b=ad[i],ad[j]
            if (GR[a]-GR[b])*(r[a]-r[b])<0 and abs(r[a]-r[b])>0.004:
                h.append(f'BOYUT SIRASI {a}/{b}')
    for g in SIRA:
        ul=sorted([u for u,(gg,_) in UYDU.items() if gg==g], key=lambda u:ua[u])
        if not ul: continue
        gs=sorted(ul,key=lambda u:UYDU[u][1])
        if gs!=ul: h.append(f'UYDU SIRASI {g}')
        esik=max(0.10, r[g]*0.15)
        d0=ua[ul[0]]-r[ul[0]]-max(r[g],r[g]*HALKA.get(g,0))
        if d0<esik: h.append(f'ÇAKIŞMA {g}-yüzey/{ul[0]} {d0:.2f}<{esik:.2f}')
        for i in range(len(ul)-1):
            d=ua[ul[i+1]]-r[ul[i+1]]-ua[ul[i]]-r[ul[i]]
            if d<esik: h.append(f'ÇAKIŞMA {ul[i]}/{ul[i+1]} {d:.2f}<{esik:.2f}')
    def ext(g):
        e=max(r[g]*1.25,r[g]*HALKA.get(g,0)*1.05)
        for u,(gg,_) in UYDU.items():
            if gg==g: e=max(e,ua[u]+r[u])
        return e
    for a,b in CIFT:
        d=bosluk(a,b)-ext(a)-ext(b)
        if d<2.0: h.append(f'SİSTEM {a}/{b} {d:.1f}')
    d=YOR['merkur'][0]*(1-YOR['merkur'][1])-r['gunes']-ext('merkur')
    if d<6: h.append(f'GÜNEŞ/Merkür {d:.1f}')
    return h

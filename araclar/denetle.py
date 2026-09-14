# -*- coding: utf-8 -*-
import re, math, json
s=open('../uzay-macerasi.html',encoding='utf-8').read()
i=s.index('var CISIMLER'); j=s.index('\n];',i); blok=s[i:j]
d=0;bas=None;C={}
for k,ch in enumerate(blok):
    if ch=='{':
        if d==0:bas=k
        d+=1
    elif ch=='}':
        d-=1
        if d==0:
            rr=blok[bas:k+1]; m=re.match(r"\{id:'([a-z0-9]+)'",rr)
            if m: C[m.group(1)]=rr
def al(idd,alan):
    rr=C[idd]
    for mm in re.finditer(r"[,{]\s*"+alan+r":\s*([-\d.]+)", rr):
        onc=rr[:mm.start()]
        if onc.count('{')-onc.count('}')==1: return float(mm.group(1))
    return None
GUN=1/365.25
DONUS={m.group(1):eval(m.group(2),{'GUN':GUN}) for m in
       re.finditer(r"(\w+):\s*([\d.]+\*GUN)", s[s.index('var DONUS_YIL'):s.index('var ATMOSFER')])}
EKS={m.group(1):float(m.group(2)) for m in
     re.finditer(r"(\w+):\s*([\d.]+)", s[s.index('var EKSEN_EGIM'):s.index('\n};',s.index('var EKSEN_EGIM'))])}

# ---------------- gercek degerler ----------------
# (e, egim°, yil, donus_gun, eksen_egim°)
G = {
 'merkur': (0.20563, 7.005, 0.24085, 58.646, 0.034),
 'venus':  (0.00677, 3.395, 0.61520, 243.025, 177.36),
 'dunya':  (0.01671, 0.000, 1.00000, 0.99727, 23.44),
 'mars':   (0.09339, 1.850, 1.88085, 1.02596, 25.19),
 'ceres':  (0.07580,10.594, 4.60000, 0.37810, 4.00),
 'jupiter':(0.04839, 1.304,11.86200, 0.41354, 3.13),
 'saturn': (0.05386, 2.485,29.45700, 0.44401, 26.73),
 'uranus': (0.04726, 0.773,84.02000, 0.71833, 97.77),
 'neptun': (0.00859, 1.770,164.7900, 0.67125, 28.32),
 'pluton': (0.24883,17.160,247.9400, 6.38720,122.53),
 'eris':   (0.43607,44.040,559.0000, 1.07910, 78.00),
 'halley': (0.96714,162.26,75.32000, None,   None),
}
UY = {  # (gezegen, gercek a km, yorunge periyodu gun, retrograd mi)
 'ay':('dunya',384400,27.3217,False), 'phobos':('mars',9376,0.31891,False),
 'deimos':('mars',23463,1.26244,False), 'io':('jupiter',421700,1.769,False),
 'europa':('jupiter',671100,3.551,False), 'ganymede':('jupiter',1070400,7.155,False),
 'callisto':('jupiter',1882700,16.689,False), 'enceladus':('saturn',238040,1.370,False),
 'titan':('saturn',1221870,15.945,False), 'miranda':('uranus',129900,1.413,False),
 'triton':('neptun',354800,5.877,True), 'charon':('pluton',19591,6.387,False),
}
h=[]; not_=[]
print('%-9s %-22s %-22s' % ('cisim','bizde','gerçek'))
print('-'*72)
# 1) yorunge periyotlari
for k,(e,eg,yil,don,eks) in G.items():
    v=al(k,'yil')
    if v is None: h.append(f'{k}: yil yok'); continue
    if abs(v-yil)/yil > 0.02: h.append(f'YIL {k}: {v} ≠ {yil}')
# 2) egim (radyan)
for k,(e,eg,yil,don,eks) in G.items():
    v=al(k,'egim')
    if v is None: continue
    gerc=math.radians(eg)
    if abs(v-gerc) > max(0.01, gerc*0.05): h.append(f'EĞİM {k}: {v:.4f} rad = {math.degrees(v):.2f}° ≠ {eg}°')
# 3) e — sikistirilmis olmali: (q^0.52, Q^0.52) ile tutarli mi
OL=86.0
for k,(e,eg,yil,don,eks) in G.items():
    if k=='halley': continue
    a=al(k,'a'); ee=al(k,'e')
    if a is None: continue
    AU={'merkur':0.38710,'venus':0.72333,'dunya':1.00000,'mars':1.52368,'ceres':2.7658,
        'jupiter':5.20260,'saturn':9.55491,'uranus':19.2184,'neptun':30.1104,
        'pluton':39.4821,'eris':67.864}[k]
    q=AU*(1-e); Q=AU*(1+e)
    qb=OL*q**0.52; Qb=OL*Q**0.52
    ab=(qb+Qb)/2; eb=(Qb-qb)/(Qb+qb)
    if abs(a-ab)>max(1.5,ab*0.02) or abs(ee-eb)>max(0.004,eb*0.06):
        h.append(f'YÖRÜNGE {k}: a={a} e={ee} → 0,52 sıkıştırması a={ab:.1f} e={eb:.3f} olmalı')
# 4) eksen donusu
for k,(e,eg,yil,don,eks) in G.items():
    if don is None: continue
    if k not in DONUS: h.append(f'DÖNÜŞ {k}: tabloda yok'); continue
    if abs(DONUS[k]/GUN - don)/don > 0.01: h.append(f'DÖNÜŞ {k}: {DONUS[k]/GUN:.4f} gün ≠ {don}')
    if DONUS[k] < 0: h.append(f'DÖNÜŞ {k}: eksi periyot (yön eksen eğikliğinden gelmeli)')
# 5) eksen egikligi
for k,(e,eg,yil,don,eks) in G.items():
    if eks is None: continue
    if k not in EKS: h.append(f'EKSEN {k}: tabloda yok'); continue
    if abs(math.degrees(EKS[k]) - eks) > max(1.0, eks*0.03):
        h.append(f'EKSEN {k}: {math.degrees(EKS[k]):.1f}° ≠ {eks}°')
    ters_biz = EKS[k] > math.pi/2; ters_ger = eks > 90
    if ters_biz != ters_ger: h.append(f'DÖNÜŞ YÖNÜ {k}: ters/düz uyuşmuyor')
# 6) uydu periyotlari ve gelgit kilidi
for u,(g,km,per,ret) in UY.items():
    v=al(u,'yil'); gerc=per/365.25
    if v is None: h.append(f'{u}: yil yok'); continue
    if abs(abs(v)-gerc)/gerc > 0.03: h.append(f'UYDU YIL {u}: {v} ≠ {gerc:.5f} ({per} gün)')
    if (v<0) != ret: h.append(f'UYDU YÖN {u}: {"ters" if v<0 else "düz"} olmamalı')
print('\n'.join(h) if h else '✓ hata yok')

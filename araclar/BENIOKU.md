# Araçlar

Bu iki betik `uzay-macerasi.html` içindeki ölçeği üretir ve denetler. Uygulamanın
çalışması için gerekli değiller — dosyayı elle değiştirmek yerine hesabı
tekrarlamak istediğinde kullanılırlar.

## `olcek.py` — boyut ve mesafe çözücüsü

Güneş'ten Deimos'a kadar her cismin yarıçapını ve her uydunun yörünge
yarıçapını üretir. Üç kural:

- **Boyut:** her cisim `E × (R_gerçek / R_⊕)^p`. Şu an `E=0.7021, p=0.80`
  (Güneş 30 birim çıkacak şekilde seçildi). Tek eğri olması şart — gezegenlere
  bir, uydulara başka eğri uygulanırsa Ceres, Ganymede'den iri çizilir.
- **Uydu yörüngesi:** gerçek uzaklık (gezegen yarıçapı cinsinden) 0,52 üssüyle
  sıkıştırılır; aile bir uçtan gezegenin yüzeyine, öbür uçtan sistemin
  bütçesine oturtulur. Hiçbir uydu gerçeğinden **uzağa** konmaz.
- **Bütçe:** komşu sistemlerin çakışmaması koşuluyla max-min adil paylaştırılır
  (ortak erim `F` ikili aramayla büyütülür, sonra yeri olan sistemler tek tek
  daha da büyütülür). Boşluğu yarı yarıya bölmek yanlış — minicik Ceres,
  Jüpiter'in yarısı kadar yer kapar.

```
python3 -c "
import olcek
r,ua,F = olcek.coz(E=0.7021, P=0.80, M=0.52)
print(olcek.denetle(r,ua) or 'hata yok')
print({k:round(v,3) for k,v in r.items()}); print({k:round(v,2) for k,v in ua.items()})"
```

`p`'yi büyütmek oranları gerçeğe yaklaştırır ama gezegenleri küçültür
(0,85'te Dünya 0,70 → 0,56, Merkür 0,33 → 0,25). Değiştirirsen çıkan bütün
`r` ve `a` değerlerini HTML'e birlikte yazman gerekir.

## `denetle.py` — veri denetimi

HTML'i okur; yörünge periyodu, eksantriklik, eğiklik, eksen eğikliği, dönüş
yönü ve uydu periyotlarını gerçek değerlerle karşılaştırır.

```
cd araclar && python3 denetle.py
```

Beklenen çıktı: yalnız `EKSEN eris` uyarısı. Eris'in kutup yönelimi gerçekten
ölçülmemiş — o uyarı bilerek bırakıldı, uydurma bir sayıyla kapatma.

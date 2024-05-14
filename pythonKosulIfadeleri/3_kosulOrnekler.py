# 1- Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 yaş ve eğitim durumu
#    lise ya da üniversite olmalıdır
isim= input('isim: ')
yas= int(input('yaş: '))
ebilgisi= input('eğitim bilgisi: ')
if (yas>=18):
    if (ebilgisi=='lise'or ebilgisi=='üniversite'):
        print(f'{isim} kişisi, ehliyet alabilirsiniz.')
    else:
        print(f'{isim} kişisi, eğitim durumunuz yetersiz, ehliyet alamazsınız')
else:
    print(f'{isim} kişisi, ehliyet alamazsınız, reşit değilsiniz')



# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karsılık gelen not bilgisini yazdırınız.
#   0-24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5

yazili1=int(input('1.sınav notu: '))
yazili2=int(input('2.sınav notu: '))
sozlu=int(input('Sözlü notu: '))

ortalama= (yazili1+yazili2+sozlu)/3

if (ortalama > 0) and (ortalama < 25):
    print('not bilgisi:0 ')

elif (ortalama > 24) and (ortalama < 45):
    print('not bilgisi:1 ')

elif ortalama > 44 and ortalama < 55:
    print('not bilgisi:2 ')

elif ortalama > 54 and ortalama < 70 :
    print('not bilgisi:3 ')

elif ortalama > 69 and ortalama < 85:
    print('not bilgisi:4 ')

elif ortalama > 84 and ortalama < 101:
    print('not bilgisi:5 ')
else:
    print('Yanlış bilgi girdiniz ')


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşagıdaki bilgilere
# göre hesaplayınız.
# 1. Bakım: 1.yıl
# 2.Bakım: 2.yıl
# 3. Bakım : 3. yıl
#  ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#  *** datetime modülünü kullanınız
#  (simdi)-(2018/8/1)=> gün


import datetime

tarih= input('aracınız hangi tarihte trafiğe çıktı (2019/8/3): ')
tarih= tarih.split('/')
print('yıl:',tarih[0]) # yıl
print('ay: ', tarih[1]) # ay
print('gün: ', tarih[2]) # gün

trafigeCikis= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi= datetime.datetime.now()
fark=(simdi-trafigeCikis)
days=fark.days
if days<=365:
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3.servis aralığı')
else:
    print('servis aralığı dısında ')

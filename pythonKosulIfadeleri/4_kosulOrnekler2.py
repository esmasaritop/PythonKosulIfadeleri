# 1- Girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz
sayi=float(input('Sayı giriniz: '))
result = (sayi<=100) and (sayi>0)

if result:
    print(f'{sayi} sayisi 0-100 arasındadır')
else:
    print(f'{sayi} sayisi 0-100 arasında değildir')




# 2- Girilen bir sayının pozitif çift sayı olup olmadıgını kontrol ediniz
sayi= float(input('Sayı giriniz: '))
if (sayi>0) :
    if (sayi%2==0):
        print(f'{sayi} pozitif çift sayıdır')
    else:
        print(f'{sayi} pozitif ancak tektir')
else:
    print(f'{sayi}  negatiftir')




# 3- Email ve parola bilgileri ile giriş kontrolu yapınız
email='esmasaritop@gmail.com'
password='abc123'

girilenmail=input('email: ')
girilenPassword=input('password: ')

if(girilenmail==email):
    if (girilenPassword==password):
        print('uygulamaya giriş başarılı ')
    else:
        print('uygulamaya giriş başarısız, parolanız yanlış ')
else:
    print('uygulamaya giriş başarısız, mail bilginiz yanlış ')




# 4- Girilen 3 sayıyı büyüklük olarak karsılastırınız
a=int(input('Sayı1: '))
b=int(input('Sayı2: '))
c=int(input('Sayı3: '))
if (a>b) and (a>c):
    print('Sayı1 en büyük sayı mıdır. ')
elif (b>a) and (b>c):
    print('Sayı2 en büyük sayı mıdır. ')
elif (c>b) and (c>a):
    print(f'Sayı3 en büyük sayı mıdır. ')




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstü ise gecti değilse kaldı
# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
# b-) finalden 70 aldıgında ortalamanın onemi olmasın
vize1=float(input('vize1: '))
vize2=float(input('vize2: '))
final=float(input('final: '))
ortalama=((((vize1+vize2)/2)*0.6)+(final*0.4))

if (ortalama>=50):
    if (final>=50):
        print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: başarılı')
    else:
        print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: başarısız... Finalden en az 50 almalısınız')
else:
    print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu: başarısız')

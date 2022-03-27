# # import os
# # try:
# #     papkaNomi='Fayillar bilan ishlash'
# #     papkaYoli='D:/'
# #     path=os.path.join(papkaYoli, papkaNomi)
# #     os.mk dir(path)
# #     print('success')
# # except:
# #     print('bu papka mavjud')
# try:
#     fayl=open('D:/Temp/second.txt','a')
#     fayl.write('\n test bajarildi')
#     print('yozildi')
#     fayl.close()
# except:
#     print('fayl mavjud')    
# import random
# ism=['sardor','javlonbek','umidbek','kozimjon','abbosbek']
# print (random.rangchoice(len(ism)))
from tkinter import N


print('"Nexia","Tico"',"'Damas'",'ko\'rganlar qilar havas')
#5 ning 4-darajasini toping
print('5-ning 4-chi darajasi=',5**4)
#Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
a=125
s=a*a
p=4*a
print('kvadratni yuzi=',s,'\nkvadratni peremetri=',p)
#Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( deb oling)
d=12
pi=3.14
s=pi*(d**2)/4
print('doiraning yuzi=',s)
#Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping.
x=6
y=7
z=(x**2+y**2)**(1/2)
print('gepotenuza',z)
#"Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring.
salomlashuv='Hello world'
print(salomlashuv)
xabar='Sizga xabar keldi javob berishingizni kutyati'
print(xabar)
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
ism='Sardor'
familiya='Haydaraliyev'
ism_sharif=f'{ism}  {familiya}'
print(ism_sharif)
ism='Sardor'
familiya='Haydaraliyev'
print(f'Salom mening  ismim {ism},\nmening ism\tfamiliyam {ism} {familiya}')
ism=input('ismingizni kiriting /n>>>')
print('Assalomu aleykum'+'   '+ism.title())
kocha=input('kochangizni nomini kiriting:')
mahalla=input('mahallangizni nomini kiriting:')
tuman=input('tumaningizni nomini kiriting:')
viloyat=input('viloyat nomini kiriting:')
print(kocha.title()+'  ko\'chasi,\n'+mahalla.title()+' mahallasi,\n'+tuman.title()+'  tumani,\n'+viloyat.title()+'  viloyat')
 
a=int(input('sonni kiriting:'))
print('kiritgan sonni kvadrati= ',a**2,'\nkiritilgan sonni kubi= ',a**3) 
yosh=int(input('yoshingizni kiriting='))
tug_yilingiz=2022-yosh
print('Sizning tug\'ilgan kuningiz=',tug_yilingiz)
a=int(input('Birinchi sonni kiriting:'))
b=int(input('ikkinchi sonni kiriting:'))
print('ikki sonni yig\'indisi ',a+b,'\nikki sonni ayirmasi=',a-b,'\nikki sonni kopaytmasi',a*b,'\nikki sonni bo\'linmasi',a/b)
ism='sardor'
t_yil=2001.1
print(type(ism),type(t_yil))
from numpy import append


viloyatlar=['namangan','andijon','fargo\'ona','toshkent','navoiy','surxandaryo']
viloyatlar[0]='samarqand'
viloyatlar[-1]='qashqadaryo'
#append ro'yhatni o'xiriga malumot q'oshish uchun
viloyatlar.append('xorazm')
#insert royhatga index boyicha malumot qoshish
viloyatlar.insert(3,'buxoro')
print(viloyatlar)
moshinalar=['nexia','lacceti','tico','matiz']
del moshinalar[0]
print(moshinalar)
moshinalar.append('mersedes')
moshinalar.insert(3,'tesla')
del moshinalar[2]
print(moshinalar)
moshinalar.remove('tico')
print(moshinalar)
royhatni istalgan joyidan malumot o'chirish uchun REMOVE funksiyasidan foydalanamiz.
hayvonlar=['it','qoy','mushuk','sigir']
hayvonlar.remove('qoy')
print(hayvonlar)
pop metodi yordamida istalgan indexisdagi nmalumotni su'girib olishimiz mumkin ekan
bozorliklar=['piyoz','makaron','sabzi','gurunch']
mahsulotim=bozorliklar.pop(1)
print('Men bozordan '+mahsulotim+' sotib oldim')
print('Sotib olmaganlarim',bozorliklar)
ismlar=['shukurullo','ilyosbek','muhammad ali']
print(ismlar[0].title()+' nima gaplar dost ishlaring yaxshimi')
print(ismlar[1].upper()+' va '+ismlar[2].upper()+' yaqin do\'stlar.')
print(ismlar[0].title() + ' qayerdasan ' + ismlar[1].title() + ' nima qilyapsan '+ ismlar[2].capitalize()+' ishlaring yaxshmi ')
sonlar=[10,21,-14,0.15,100,45]
sonlar[0]=sonlar[0]+sonlar[2]
sonlar[1]=12
sonlar[4]=54
print(sonlar)
cars=['matiz','tesla','audi','benwi','mustang']
#sort alfabit bo'yicha tartiblash berish uchun hizmat qiladi.
cars.sort()
print(cars)
#ro'yhatni teskari tartibdalash uchun .sort metodi ichida reverse=True argumentini ham yozamiz
moshinalar=['audi','tesla','inpala','mustang','wolswagen','volvo']
cars.sort(reverse=True)
print(cars) 
moshinalar=['audi','tesla','inpala','mustang','wolswagen','volvo']
print('sorted qaytargan royhat:',sorted(moshinalar))
print('asl qiymat o\'zgarmas qoladi:',moshinalar)
print(sorted(moshinalar,reverse=True))
raqamlar=[12,25,56,15,24,45]
raqamlar.sort()
print(raqamlar)
print(sorted(raqamlar,reverse=True))
mevalar=['olma','gilos','uzum','banan','anor']
#reverse metodi bilan biz ro'yhatni teskari tartibga aylantirishimiz mumkin
mevalar.reverse()
print(mevalar)
mevalar=['olma','gilos','uzum','banan','anor']
#royhat uzunligini yani royhat nechta elementdan tashkil topganini aniqlash uchun len funksiyasidan foydalanamiz
print('Elementlar soni:',len(mevalar))
range funksiyasi yordamida biz malum oraliqdagi sonlar ketma ketligini yaratishimiz mumkin
list funksiyasi yordamida esa bu ketma ketlikni royhatga aylantirildi
raqamlar=list(range(0,14))
print(raqamlar)
juft_sonlar=list(range(1,20,2))#1 dan 20 gacha 2 qadam bilan royhat yaratadi
toq_sonlar=list(range(1,20,2)) #1 dan 20 gacha 3 qadam bilan royhat yaratadi
print('juft sonlar =',juft_sonlar)
print('toq sonlar =',toq_sonlar)


davlatlar=['uzbekiston','tojikiston','amerika','rossiya','angilya']
uzunligi=len(davlatlar)
print(uzunligi)
a=sorted(davlatlar)
print(sorted(a,reverse=True))
asl=sorted(a)
print(asl)
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
print(sorted(davlatlar,reverse=True))
royhat=list(range(120,1200,2))
summa=sum(royhat)
ayirmasi=royhat[-1]-royhat[0]
print(royhat)
print('yigindisi=',summa)
print('eng katta va eng kichiklari ayirmasi=',ayirmasi)
print('royhat elementlari soni=',len(royhat))
print('Royhat boshidan o\'nta qiymati',royhat[:10],'\n royhat o\'rtasidan o\'nta qiymati',royhat[265:276],'\n Royhat oxiridan onta elementi',royhat[530:])
taomlar=['shorva','osh','mastava','palov','manti']
nonushta=taomlar[:]
yeyiladigon_nonushta=nonushta[0:2]
yeyiladigon_nonushta.insert(0,'xodog')
yeyiladigon_nonushta.append('kok somsa')
print(yeyiladigon_nonushta)
print(taomlar)
nonushta=type(nonushta)
nonushta[0]='qaymoq musqaymoq'
print(nonushta)
a=5
b=8
a=a+b
b=a-b
a=a-b
print(b,a)
dostlarim=['alisher','humoyin','shukurullo','azizbek','hasanboy','ilyosbek']
for xabar in dostlarim:
    print(xabar,'salom dostlarim')
print(f'Kodimiz {len(dostlarim)} marta takrorlandi.')
sonlar=list(range(10,100,3))
for sonlarni_kubi in sonlar:
    a=pow(sonlarni_kubi,3)
    print('sonlarni kubi ',a)
kinolar=[]
print('eng sevimli kinolaringizni kiriting:')
for n in range(5):
    kinolar.append(input(f'{n+1} kinoni kiriting:'))
print(kinolar)    
n=int(input('Foydalanuvchidan bugun nechta odam bilan uchrashdingiz: '))
suhbat=[]
for k in range(n):
    suhbat.append(input(f'{k12+1}  korishgan insonni  kiriting: '))
print(suhbat)    
firends=[]
firends.append('sardor')
firends.append('ayubxon')
firends.append('abbosbek')
firends.append('amidbek')
print(firends)
firends.remove('ayubxon')
print(firends)
firends.insert(0,'ilyosbek')
firends.append('lutfullo')
print(firends)
mehmonlar=['axror','jamshid','bunyod','muhammadali','islomjon']
kelmagonlar=mehmonlar.pop(0)
print(kelmagonlar)
print(mehmonlar)
amalyot 10 dars
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car!='gm':
        print(car.upper())
    else:
        print(car.title())    
login=input('ismingizni kiriting:>>>\n')
if login=='admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" )
else:
    print(f"Xush kelibsiz, {login}!" )    
a=float(input('Birinchi sinni kiriting:'))
b=float(input('ikkinchi sinni kiriting:'))
if a==b:
    print("Kiritgan sonlar teng")
a=float(input('istalgan sonni kiriting:'))
if a>0:
    print('musbat sonni kiritdingiz')
else:
    print('kiritgan son manfiy')
hafta=int(input('hafta kunlarini kiriting:\n>>>'))
if hafta==1:
    print('Dushanba')
elif hafta==2:
    print('Seshanba')        
elif hafta==3:
    print('chorshanba')
elif hafta==4:
    print('payshanba')
elif hafta==5:
    print('juma')
elif hafta==6:
    print('shanba')
elif hafta==7:
    print('yakshanba')
else:
    print('hafta kunlarini 1 va 7 oraliqda berib koring!')
k=int(input('ka snini kiriting:\n>>>'))
n=int(input('takrorlanish sonini kiriting:\n>>>'))
for k in k:
    if a>0:
        print(k*n)
juft=int(input('juft sonni kiriting!='))
if juft%2==0:
    print('rahmat')
else:
    print('Bu juft son emas')  
yosh=int(input('yoshingizni kiriting:'))
if yosh<=4 or yosh>=60:
    print("kirish bepul")
if yosh>4 and yosh<=18:
    print('kirish 10000 so\'m')
if yosh>18 and yosh<60:
    print('krish 20000 so\'m')  
a=float(input('birinchi sonni kiriting:'))
b=float(input('ikkinchi sonni kiriting:'))
if a==b:
    print(f'{a==b}  bu ikki son teng') 
elif a>b:
    print(f'{a>b} birinchi son katta')
else:
    print(f'{a<b} ikkinchi son katta')  
mahsulotlar=['sabzi','banan','grunch','olma','makaron','olcha','gosht','tuxum','tuz','xurmo']
savat=[]

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f'Dokonimizda {mahsulot} bor.')
    else:
        print(f'kechirasiz {mahsulot} hali kelmagan')   
mahsulotlar=['sabzi','banan','grunch','olma','makaron','olcha','gosht','tuxum','tuz','xurmo'] 
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
for n in range(5):
    savat.append(input(f'savatga {n+1}-mahsulotni qoshing:'))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot) 
if mavjud_emas:
    print(f"dokonimizda quyidagi mahsulotlar yoq")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("siz soragan mahsulotlar dokonimizda bor")        
foydalanuvchi=['admin','sardor','umidbek','abbosbek','javohir']
yangi_login=input('o\'zingizga login tanlang:')
if yangi_login in foydalanuvchi:
    print('Bu login band, boshqa login tanlang.')
else:
    print('xush kelibsiz')    
foydalanuvchi=int(input('istalgan butun sonni kiriting:'))
for n in range(2,11):
    if foydalanuvchi%n==0:
        print(f'{foydalanuvchi} soni {n} qoldiqsiz bolinadi')
  
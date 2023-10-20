# # print('Hello World')
# #print('Merhaba Dünya\nMerhaba Dünya\nHello World\n')
# # print('Hello'+ ' ' +'Yağmur')
# # print( input('Adın Nedir?'))
# # print('Merhaba' + ' ' + input('Adın Ne?'))
# # # print(len(input('Hello Whats Your Name?'
# # Name = ('Yağmur')
# # print(Name)
# print('Hello World')
# # Name = ('Nazan')
# # # print(Name)
# # isim = input('Hello Whats Your Name?')
# # uzunluk = len(isim)
# # print(uzunluk)
# # print(input('Hello Whats Your Name?'))
# # ensongidilenşehir = input('en son gittiğiniz şehir nedir?')
# # ensevdiğinhayvan = input('en sevdiğiniz hayvanın adı nedir')
# # # print('Grup Adı: '+' '+ ensongidilenşehir + ensevdiğinhayvan)
# sayı1 = input('1inci sayıyı giriniz:')
# sayı2 = input('2nci sayıyı giriniz:')
# toplam = int(sayı1) + int(sayı2)
# # print('Toplam =' + str(toplam))
# kısakenar = int(input('kısa kenarı giriniz:'))
# uzunkenar = int(input('uzun kenarı giriniz:'))
# # Çevre = (kısakenar + uzunkenar) *2
# # Alan = kısakenar * uzunkenar
# # print('Dikdörtgenin çevresi:' + str(Çevre))
# # print('Dikdörtgenin alanı:' + str(Alan))
# Yarıçap = int(input('Yarıçapı Giriniz'))
# Yükseklik = int(input('Yüksekliği Giriniz'))
# Pİsayısı = 3.14
# TabanAlanı = Pİsayısı * Yarıçap * Yarıçap
# TabanÇevresi = 2* Pİsayısı * Yarıçap
# YanalAlan = Yükseklik * TabanÇevresi
# ToplamAlan = (2*TabanAlanı) * YanalAlan
# Hacim = TabanAlanı * Yükseklik
# print('Silindirin hacmi: ' + str(Hacim))
# print('Silindirin alanı: '+ str(ToplamAlan))
# Yarıçap = int(input('Yarıçapı Giriniz'))
# Pİsayısı = 3.14
# Çevre = 2* Pİsayısı * Yarıçap
# Hacim = Pİsayısı * Yarıçap * Yarıçap
# print('Dairenin Hacmi:' + str(Hacim))
# # print('Dairenin Çevresi: ' + str (Çevre))
# # print('Çek Cumhuriyeti'[4])
# İsimUzunluk = len(input('Merhaba, Adın Ne?'))
# # isimUzunluk_Str = str(İsimUzunluk)
# # print('İsminde ' + isimUzunluk_Str + ' karakter var.')
# ikihanelisayı = str(input('İki haneli bir sayı giriniz '))
# toplam = int(ikihanelisayı[0]) + (int(ikihanelisayı[0]))
# # print('Toplam:' + str(toplam))
# # print(4 * 8 / 2)
# Boy = float(input('Boyunuzu giriniz: '))
# Kilo = float(input('Kilonuzu giriniz: '))
# vki = int(Kilo/Boy**2)
# vki= 5
# print(f"Vücut Kilo Endeksiniz: {vki} ")
# print(8/3)
# print(type(8/3))
# # print(type)(8//3)
# Yaş = input('Kaç yaşındasın?')
# Yaş_int = int(Yaş)
# Ay = Yaş_int * 12
# Hafta = Yaş_int * 52
# Gün = Yaş_int * 365
# print(f'{Ay} aylıksın')
# print(f'{Gün} günlüksün')
# print(f'{Hafta} haftalıksın')
# print('Bahşiş hesaplayıcıya hoşgeldiniz!')   
# Hesap = float(input('Hesap ne geldi?'))
# KişiSayısı = int(input('kaç kişisiniz?'))
# Oran = float(input('Bahşiş oranı ne olsun?'))
# Toplam = Hesap + (Hesap * Oran * 100)
# KişiBaşı = Toplam / KişiSayısı
# print(f'Kişi başı ödemeniz gerekn tutar = {KişiSayısı} TL')
# if bla blaysa al 
# elif bla bla değilse al 
# else ikisi de değilse al vb. 
# print('Lunaparka hoşgeldiniz!')
# print('Bilet fiyatı yetişkin 10 TL. 12 yaşından küçükler 10 TL. ')
# Boy = int(input('Lütfen boyunuzu giriniz (cm) '))
# Yaş = int(input('Lütfen yaşınızı giriniz '))
# BiletFiyatı = 0
# if Boy > 80 :
#     if(Yaş <12):
#         BiletFiyatı = 5
#     else:
#         BiletFiyatı = 10
#     print(f'Çarpışan arabalara binebilirsiniz. Fiyat {BiletFiyatı} TL')
# elif Boy >80 and Boy < 120:
#     if(Yaş < 12):
#         BiletFiyatı = 5
#     else:
#         Biletfiyatı = 10
#         print(f'Lunapark hız trenine binebilirsiniz. Fiyat {BiletFiyatı} TL')
# elif Boy > 120 and Boy < 140:
#     if(Yaş < 12):
#         Biletfiyatı = 5
#     else:
#         Biletfiyatı = 10
#     print(f'Gondola binebilirsiniz. Fıyat {Biletfiyatı} TL')
# elif Boy > 140 :
#     if(Yaş < 12) :
#         Biletfiyatı = 5
#     else:
#         Biletfiyatı =10
#         print(f'Kamikazeye binebilirsiniz. Fiyat {Biletfiyatı} TL')
# else:
#     print('Lunaparkta herhangi bir araca binmek için boyunuz yeterli değil.')
# Yıl = int(input('Hangi yılı kontrol etmek istiyorsunuz? '))
# if Yıl % 4 == 0:
#     if Yıl %100 == 0:
#         if Yıl % 400 == 0:
#              print(f'{Yıl} artık bir yıldır.')
#         else:
#               print(f'{Yıl} artık bir yıl değildir.')
#     else:
#          print(f' {Yıl} artık bir yıl değildir')
# else:
#      print(f' {Yıl} artık bir yıl değildir')
# print('Lunaparka hoşgeldiniz!')
# Boy = int(input('Boyunuz kaç cm? '))
# Ücret = 0
# if Boy >= 120:
#     print('Rollercoastera binebilirsiniz.')
#     Yaş = int(input('Kaç yaşındasınız? '))
#     if Yaş < 12:
#         Ücret = 5
#     elif Yaş <= 18:
#         Ücret= 10
#     else:
#         Ücret = 20
#     Fotoğrafistiyor = input('Fotoğraf çektirmek istiyor musunuz? e veya h ')
#     if Fotoğrafistiyor == 'e':
#         Ücret += 3
#     print(f'Toplam ödeme: {Ücret}')
# else:
#     print('Üzgünüm, boyunuz rollercoastera binmek için yeterli değil')
# Boy = input('Yazılım Pizzaya hoşgeldiniz! Hangi boy pizza sipariş etmek istiyorsunuz? k veya o veya b =>')
# Ekstrasos = input('Ekstra sos ister misiniz? e veya h =>')
# Ekstrapeynir = input('Ekstra peynir ister misiniz? e veya h =>')
# Toplam = 0
# if Boy =='k':
#     Toplam += 15
# elif Boy =='o':
#     Toplam += 20
# elif Boy == 'b':
#     Toplam += 25
# if Ekstrasos =='e':
#     if Boy == 'k':
#         Toplam += 2
#     else:
#         Toplam += 5
# if Ekstrapeynir == 'e':
#     Toplam += 3
# print(f'Toplam ödeme = {Toplam}')
# print('Sevgi hesaplayıcıya hoş geldiniz!')
# İsim1 = input('Adınızı giriniz.')
# İsim2 = input('Onun adını giriniz.')
# İsimler = ( İsim1 + İsim2) . lower()
# g = İsimler.count('g')
# e = İsimler.count ('e')
# r = İsimler.count('r')
# ç = İsimler.count('ç')
# a = İsimler.count ('a')
# ş = İsimler.count ('ş')
# k = İsimler.count('k')
# Toplam = g + e + r + ç + a + ş + k
# if( Toplam < 10 or Toplam > 90):
#     print(f'Sevgi Puanınız: {Toplam}, kola ve mentos gibisiniz!')
# elif(Toplam > 40 and Toplam < 50):
#     print(f'Sevgi Puanınız: {Toplam}, beraber iyisiniz!')
# else:
#     print(f'Sevgi Puanınız: {Toplam}')
# Yaş = int(input('Kaç yaşındasınız? '))
# if Yaş >= 18:
#     Sağlık = input('Herhangi, bir rahatsızlığınız var mı? e veya h ')
#     if Sağlık == 'h':
#         print('Ehliyet alabilirsiniz!')
#     else:
#         print('Üzgünüm, ehliyet alamazsınız!')
# else:
#     print('Üzgünüm, ehliyet alamazsınız!')
# Şifre = '1234'
# print('Yazılım Bankasına Hoş Geldiniz!')
# Girilenşifre =input('Lütfen şifrenizi giriniz!')
# if len(Girilenşifre) != 4:
#     print('Eksik ya da fazla tuşladınız!')
# elif Şifre == Girilenşifre:
#     print('Hoşgeldiniz!')
# else:
#     print('Yanlış tuşladınız!')
# import math
# Boy = float(input('Boyunuzu m cinsinden giriniz'))
# Kilo = int(input('Kilonuzu kg cinsinden giriniz'))
# İdealkilo = math.floor(22*Boy*Boy)
# Fark = abs(İdealkilo - Kilo)
# if İdealkilo > Kilo:
#     print(f'{Fark} kilo almanızı öneririm')
# else:
#     print(f'{Fark} kilo vermenizi öneririm')
# Sayı1 = int(input('1inci sayıyı giriniz'))
# Sayı2 = int(input('2nci sayıyı giriniz'))
# sayı3 = int(input('3üncü sayıyı giriniz'))
# sayı4 = int(input('4üncü sayıyı giriniz'))
# Sayı5 = int(input('5inci sayıyı giriniz'))
# Enbüyük = Sayı1
# if Enbüyük < Sayı2:
#     Enbüyük = Sayı2
# if Enbüyük < sayı3:
#     Enbüyük = sayı3
# if Enbüyük < sayı4:
#     Enbüyük = sayı4
# if Enbüyük < Sayı5:
#     Enbüyük = Sayı5
# print(f'Girilen sayıların en büyüğü = {Enbüyük}')
# import random
# Randomsayı = random.
# Şehirler = ["Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman",
# "Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ",
# "Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük",
# "Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya",
# "Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa",
# "Siirt","Sinop","Şırnak","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"]
# # print(Şehirler[0])
# # print(Şehirler.index("Adana"))
# # print(Şehirler[12])
# # print(Şehirler[80])
# # print(Şehirler[-1])
# # print(Şehirler[-2])
# # Şehirler[33] = "İçel"
# # print(Şehirler[33])

# # Şehirler.append("Tarsus")
# # print(Şehirler[81])
# # print(len(Şehirler))
# # Şehirler.remove("Tarsus")
# # print(len(Şehirler))
# Şehirler.pop()
# print(len(Şehirer)) 
# import random
# İsimler = ' Ecem, Işıl, İkra, Defne, İmge, Nisa'
# İsimdizisi = İsimler.split (',')
# index = random.randint(0, len(İsimdizisi) - 1)
# print(f'Hesabı {İsimdizisi[index]} ödeyecek!')
Row1 = ['⬜️, ⬜️, ⬜️']
Row2 = ['⬜️, ⬜️, ⬜️']
Row3 = ['⬜️, ⬜️, ⬜️']
Harita = [Row1, Row2, Row3]
print(f'{Row1}\n{Row2}\n {Row3}\n')
Pozisyon = input('Hazineyi nereye saklamak istersiniz?')
Yatay = int(Pozisyon[0]) -1
Dikey = int(Pozisyon[1]) -1
Harita[Dikey] [Yatay] = 'X'
print (f'{Row1}\n{Row2}\n{Row3}\n')
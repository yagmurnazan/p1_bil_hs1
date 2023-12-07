# 0 dan girilen sayıya kadar ki tüm çift sayıarın toplamını bulma
Sayı = int(input('Lütfen bir sayı giriniz!'))
Toplam = 0
for Sayı2 in range (0, Sayı):    
    if Sayı2 %2 == 0:
        Toplam = Toplam + Sayı2

print(Toplam)
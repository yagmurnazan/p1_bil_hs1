# girilen sayının rakamlarının çarpımını bulma
Sayı = input('Bir sayı giriniz')
Sayıdizisi = list(Sayı) 
Toplam = 1
for Çarpım in Sayıdizisi:
    Toplam = Toplam * int(Çarpım)
print(Toplam)
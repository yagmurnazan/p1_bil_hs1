#bilgisayar bir sayı seçecek kişi o sayıyı bulmaya çalışacak eğer tahmin sayıdan küçükse k büyükse b eşitse e yazacak bilgisayar
import random
Sayı = random.randint(1,100)
Kullanıcıtahmini = 0
while Kullanıcıtahmini != Sayı :
    Kullanıcıtahmini = int(input('Sayı giriniz: '))
    if Kullanıcıtahmini > Sayı :
        print('Tahmininiz seçtiğim sayıdan büyüktür:')
    elif Kullanıcıtahmini < Sayı :
        print('Tahmininiz seçtiğim sayıdan küçüktür:')
    else :
        print('Tebrikler seçtiğim sayıyı buldunuz!!')
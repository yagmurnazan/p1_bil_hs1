Boy= float(input('Boyunuzu metre cinsinden giriniz!'))
Kilo = float(input('Kilonuzu giriniz'))
Vki = (Kilo/Boy**2)
if Vki < 18.5 :
    Ulaşılmasıgerekenkilo1 =18.5 * Boy * Boy
    Alınmasıgerekenkilo = Ulaşılmasıgerekenkilo1 - Kil
    print(f'Almanız gereken kilo miktarı {round(Alınmasıgerekenkilo,2)}')

elif Vki > 24.5:
    Ulaşılmasıgerekenkilo2 = 24.9 * Boy * Boy
    Verilmesigerekenkilo = Kilo - Ulaşılmasıgerekenkilo2 
    print(f'Vermeniz gereken kilo miktarı {round(Verilmesigerekenkilo,2)}')
else:
    print('Vücut kitleniz idealdir, kilo alıp vermenize gerek yoktur.')
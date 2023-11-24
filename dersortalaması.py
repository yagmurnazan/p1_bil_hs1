# problem a dersinin ortalamasını bulma
Matematik1yazılı =int(input('Matematik dersinin 1. yazılı sınavından aldığınız notu giriniz. '))
Matematik2yazılı = int(input('Matematik dersinin 2. yazılı sınavından aldığınız notu giriniz. '))
Matematik1sözlü =int(input('Matematik dersinden aldığınız ilk sözlü notunu giriniz. '))
Matematik2sözlü = int(input('Matematik dersinden aldığınız ikinci sözlü notunu giriniz. '))
Toplam = (Matematik1yazılı + Matematik2yazılı + Matematik1sözlü + Matematik2sözlü)
Sonuç = Toplam / 4
print(f"Matematik dersi ortalamanız = {Sonuç}")
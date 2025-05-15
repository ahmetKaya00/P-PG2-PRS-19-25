try:
    sayi = int(input("Bir Sayı Girin:"))
    sonuc = 10 / sayi
except ZeroDivisionError:
    print("Sıfıra Bölünemez!")
except ValueError:
    print("Lütfen geçerli bir sayı girin!")
else:
    print(sonuc)

yas = int(input("Yaşınızı Girin:"))
if yas < 0:
    raise ValueError("Yaş Negatif Olamaz!")
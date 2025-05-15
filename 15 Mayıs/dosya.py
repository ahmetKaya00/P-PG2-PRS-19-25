with open("demo.txt","r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("demo.txt","w",encoding="utf-8") as dosya:
    dosya.write("Bu satır Yeni Eklendi!\n")

with open("demo.txt","a",encoding="utf-8") as dosya:
    dosya.write("\n Merhaba Yeni Yazı")


isim = input("Adınızı Girin: ")

with open("kullanici.txt","a", encoding="utf-8") as dosya:
    dosya.write(f"Merhaba, {isim}")
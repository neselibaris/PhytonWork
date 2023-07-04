sayi1 = 25
sayi2 = 30

sonuc = int(str(sayi1) + str(sayi2)) 

print(sonuc)








isim = input("Adınızı giriniz: ")

kücükisim = isim.lower()

print(kücükisim)









ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")

while True:
    yas = input("Yaşınızı girin: ")
    if yas.isdigit():
        break
    else:
        print("Hatalı giriş! Lütfen bir sayı girin.")

print("Ad: ", ad)
print("Soyad: ", soyad)
print("Yaş: ", yas)

sayi3 = float(input("Birinci sayıyı girin: "))
sayi4 = float(input("İkinci sayıyı girin: "))
sayi5 = float(input("Üçüncü sayıyı girin: "))

toplam = sayi3 + sayi4 + sayi5

print("Toplam: ", toplam)


metin = input("Bir metin girin: ")

kelime1 = input("Değiştirmek istediğiniz ilk kelimeyi girin: ")
kelime2 = input("İkinci kelimeyi girin: ")

degistirilmis_metin = metin.replace(kelime1, kelime2)

print("Değiştirilmiş Metin: ", degistirilmis_metin)


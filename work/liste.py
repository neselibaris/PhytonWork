meyveler = ["elma", "armut", "muz", "çilek", "portakal"]

print("Meyve Listesi:", meyveler)

girilen_meyve = input("Çıkarmak istediğiniz meyveyi girin: ")

if girilen_meyve in meyveler:
    meyveler.remove(girilen_meyve)
    print("Meyve çıkarıldı.")
else:
    print("Meyve listede bulunmamaktadır.")

print("Güncellenmiş Meyve Listesi:", meyveler)


isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali"]

print("Mevcut İsim Listesi:", isimler)

girilen_isim = input("İsminizi girin: ")

if girilen_isim in isimler:
    print("Hoş geldiniz,", girilen_isim, "!")
else:
    isimler.append(girilen_isim)
    print("İsim listenize eklendi.")

print("Güncellenmiş İsim Listesi:", isimler)

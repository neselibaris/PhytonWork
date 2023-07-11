class Bilet:
    def __init__(self):
        self.kapasite = 0
        self.biletSayisi = 0
        self.biletDetay = []

    def biletAyarlama(self, kapasite):
        self.kapasite = kapasite

    def biletSat(self, ad, soyad):
        if self.biletSayisi < self.kapasite:
            self.biletSayisi += 1
            self.biletDetay.append({"Ad": ad, "Soyad": soyad})
            print("Bilet satıldı!")
        else:
            print("Bilet tükendi!")

    def biletDetayListele(self):
        return self.biletDetay

    def kalanBiletSayisi(self):
        return self.kapasite - self.biletSayisi

bilet = Bilet()
bilet.biletAyarlama(8)

while True:
    kacBilet = int(input("Kaç bilet almak istiyorsunuz? (Çıkmak için 0 girin): "))
    if kacBilet == 0:
        break

    for _ in range(kacBilet):
        isim = input("Bilet alan kişinin adını girin: ")
        soyad = input("Bilet alan kişinin soyadını girin: ")
        bilet.biletSat(isim, soyad)
        print("Kalan bilet sayısı:", bilet.kalanBiletSayisi())

    print("Bilet Detayları:")
    for detay in bilet.biletDetayListele():
        print("Ad:", detay["Ad"])
        print("Soyad:", detay["Soyad"])
        print("---------------")

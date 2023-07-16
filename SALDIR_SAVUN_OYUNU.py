import sys,random,time

def bekleme():
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.2)

def exit():
    print("Oyun Kapatılıyor")
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.2)
    sys.exit()
def kurallar():
    print("""
    1 :Saldır
    2 :Savun
    3 :Oyundan Çık""")


class karakter():
    def __init__(self,isim,can=100,güç=12,dayanıklılık=8):
        self.isim = isim
        self.can = can
        self.güç = güç
        self.dayanıklılık = dayanıklılık

    def bilgileri_goster(self):
        print("""
        İsim: {}
        Can: {}
        Güç: {}
        Dayanıklılık: {}
        """.format(self.isim, self.can, self.güç, self.dayanıklılık))

    def saldiri_basarili(self):
        self.güç -= 1

    def saliri_basarisiz(self):
        self.güç -= 1
        self.can -= 5

    def savunma_basarili(self):
        self.can -= 5
    def savunma_basarisiz(self):
        self.can -= 5
        self.dayanıklılık -= 1

print("Oyunuma Hoşgeldiniz")

def oyun():
    isim = input("Karakterinizin ismini belirleyin: ")
    kahraman = karakter(isim)
    dusman = karakter("Düşman")
    print("Oyun Başlıyor")
    while True:
        bekleme()
        kurallar()
        hamle = input("Hamleniz: ")

        sayi = random.randint(1, 2)

        if(hamle == "3"):
            exit()

        elif(hamle == "1"):
            if(sayi == 1):
                bekleme()
                print("Saldırı Başarılı")
                kahraman.saldiri_basarili()
                dusman.savunma_basarisiz()
                kahraman.bilgileri_goster()
                dusman.bilgileri_goster()

            elif(sayi == 2):
                bekleme()
                print("Saldırı Başarısız")
                kahraman.saliri_basarisiz()
                dusman.savunma_basarili()
                kahraman.bilgileri_goster()
                dusman.bilgileri_goster()


        elif(hamle == "2"):
            if(sayi == 1):
                bekleme()
                print("Savunma Başarılı")
                kahraman.savunma_basarili()
                dusman.saliri_basarisiz()
                kahraman.bilgileri_goster()
                dusman.bilgileri_goster()

            elif(sayi == 2):
                bekleme()
                print("Savunma Başarısız")
                kahraman.savunma_basarisiz()
                dusman.saldiri_basarili()
                kahraman.bilgileri_goster()
                dusman.bilgileri_goster()




        else:
            bekleme()
            print("!!HATALI TUŞLAMA!!")
            print("Tekrar Deneyin")

        if(kahraman.güç <= 0 or kahraman.can <= 0 or kahraman.dayanıklılık <= 0):
            print("!!KAYBETTİNİZ!!")
            tekrar = input("Tekrar Oynamak İstermisiniz Y/N :")

            if(tekrar == "Y" or tekrar == "y"):
                oyun()

            elif(tekrar == "N" or tekrar == "n"):
                exit()

        elif(dusman.güç <= 0 or dusman.can <= 0 or dusman.dayanıklılık <= 0):
            print("!!TEBRİKLER KAZANDINIZ!!")
            tekrar = input("Tekrar Oynamak İstermisiniz Y/N :")

            if (tekrar == "Y" or tekrar == "y"):
                oyun()

            elif (tekrar == "N" or tekrar == "n"):
                exit()
oyun()




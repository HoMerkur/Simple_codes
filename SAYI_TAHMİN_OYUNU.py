import time, random

def geri_sayim():
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)

def exit():
    print("Oyun Kapatılıyor")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

def oyun_baslat():
    def start():
        print("Oyun Başlatılıyor")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
    start()

    print("**Sayı Tahmin Oyunu**")
    print("!!Oyun Başlamak Üzere ve Sadece 5 Tahmin Hakkın Var!!")
    geri_sayim()

    tahmin_adedi = 5

    sayi = random.randint(0, 50)

    while(tahmin_adedi > 0):
        tahmin =int(input("Aklımdan 0 ile 50 arasında bir sayı tuttum Bil bakalım hangi sayı: "))

        if(sayi > tahmin):
                print("Yanlış Tahmin, Sayını Büyütmen Lazım")
                tahmin_adedi -= 1

        elif(sayi < tahmin):
                print("Yanlış Tahmin, Sayını Küçültmen Lazım")
                tahmin_adedi -= 1
        else:
            print("Tebrikler Doğru Bildiniz!!!")
            print("Aklımdan Tuttuğum Sayı", sayi, "idi.")
            break


    if(tahmin_adedi == 0):
        print("Malesef Tahmin Hakkınız Kalmadı!!")
        print("Doğru Sayı", sayi, "idi.")

    tuslama = input("Tekrar Oynamak İstermisin Y/N: ")

    if(tuslama == "Y"):
        oyun_baslat()

    else:
        exit()

oyun_baslat()
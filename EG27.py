


while True:

    print("""Çevre ve Alan heaplayıcısına hoşgeldiniz
    Çıkmak için 'q' tuşlaın.
    """)
    def kare_alan(x):
        print("Karenin alanı:", x**2)

    def kare_cevre(x):
        print("Karenin çevresi:", x*4)

    def dikdotrgen_alan(x,y):
        print("Dikdörtgenin alanı:", x*y)

    def dikdortgen_cevre(x,y):
        print("Dikdörgenin çevresi:", (x+y)*2)

    def ucgen_alan(x,y):
        print("Üçgenin alanı:", (x*y)/2)

    def ucgen_cevre(x,y,z):
        print("Üçgenin çevresi:", x+y+z)

    def daire_alan(x):
        print("Dairenin alanı:", 3.14*(x**2))

    def daire_cevre(x):
        print("Dairenin çevresi:", 2*3.14*x)

    sekil = input("""(Bütün harfler küçük olacak şekilde) Alanını yada çevresini hesaplamak istediğiniz şeli girin: """)


    if(sekil == "q"):
        print("Program kapatılıyor...")
        break

    else:
        hesap = input("""Alan hesabı yapmak için 'a' tuşlayın Çevre hesabı yapmak için 'ç' tuşlayın: """)
        if(sekil == "kare" and hesap == "a"):
            uzunluk1 = float(input("Karenin bir kenar uzunluğunu girin: "))
            kare_alan(uzunluk1)

        elif(sekil == "kare" and hesap == "ç"):
            uzunluk1 = float(input("Karenin bir kenar uzunluğunu girin: "))
            kare_cevre(uzunluk1)

        elif(sekil == "dikdörtgen" and hesap == "a"):
            uzunluk1 = float(input("Dikdörtgenin uzun kenarının uzunluğunu girin: "))
            uzunluk2 = float(input("Dikdörtgenin kısa kenarının uzunluğunu girin: "))
            dikdotrgen_alan(uzunluk1,uzunluk2)

        elif(sekil == "dikdörgen" and hesap == "ç"):
            uzunluk1 = float(input("Dikdörtgenin uzun kenarının uzunluğunu girin: "))
            uzunluk2 = float(input("Dikdörtgenin kısa kenarının uzunluğunu girin: "))
            dikdortgen_cevre(uzunluk1,uzunluk2)

        elif(sekil == "üçgen" and hesap == "a"):
            uzunluk1 = float(input("Üçgenin taban uzunluğunu girin: "))
            uzunluk2 = float(input("Üçgenin yüksekliğini girin: "))
            ucgen_alan(uzunluk1,uzunluk2)

        elif(sekil == "üçgen" and hesap == "ç"):
            uzunluk1 = float(input("Üçgenin birinci kenar uzunluğunu girin: "))
            uzunluk2 = float(input("Üçgenin ikinci kenar uzunluğunu girin: "))
            uzunluk3 = float(input("Üçgenin üçüncü kenar uzunluğunu girin: "))
            ucgen_cevre(uzunluk1,uzunluk2,uzunluk3)

        elif(sekil == "daire" and hesap == "a"):
            uzunluk1 = float(input("Dairenin yarıçap uzunluğunu girin: "))
            daire_alan(uzunluk1)

        elif(sekil == "daire" and hesap == "ç"):
            uzunluk1 = float(input("Dairenin yarıçap uzunluğunu girin: "))
            daire_cevre(uzunluk1)

        else:
            print("Hatalı tuşlama yaptınız!")


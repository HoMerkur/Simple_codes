def ebob(x,y):
    bolen = 1
    if(x > y):
        for i in range(2,x):
            if(x%i == 0 and y%i == 0 and i> bolen):
                bolen = i

        print("Ebob({},{})= {} dir".format(x,y,bolen))
    elif(y > x):
        for i in range(2,y):
            if (x % i == 0 and y % i == 0 and i > bolen):
                bolen = i
        print("Ebob({},{})= {} dir".format(y, x, bolen))



while True:
    print("""Ebob hesaplayıcısına hoşlgeldiniz
    Çıkmak için 'q' tuşlayabilirsiniz.""")

    sayi1 = input("Birinci sayıyı girin: ")

    if(sayi1 == "q"):
        print("Program Kapatılıyor...")
        break

    else:

        sayi1 = int(sayi1)
        sayi2 = int(input("İkinci sayıyı girin"))
        ebob(sayi1, sayi2)



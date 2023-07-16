def ekok(x,y):
    a = 1

    while True:
        if(a >= x and a >= y and a%x == 0 and a%y == 0):
            print("Ekok:", a)
            break
        else:
            a += 1


sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
ekok(sayi1,sayi2)
sayi = int(input("Bir sayı girin: "))

a = 0

for i in range(2,sayi):
    if(sayi%i == 0):
        a = 1
        break
if(a == 1):
    print(sayi, "Bir asal sayı değildir.")
else:
    print(sayi, "Bir asla sayıdır")
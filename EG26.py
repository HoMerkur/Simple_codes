sayi = int(input("Bir sayı girin: "))
a = 1
for i in range(2,sayi+1):
    a *= i
print(sayi, "Sayısının faktöriyeli: ", a)
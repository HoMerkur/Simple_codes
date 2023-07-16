birinci_liste = [1, 2, 4, 8, 101, 203, 568, 784, 45, 63, 52, 89, 45, 36, 21, 410, 23, 56, 78, 45, 14, 459, 125, 456, 98, 96, 621]
ikinci_liste = [1, 2, 8, 101, 568, 45, 63, 21, 52, 21, 410, 78, 459, 96, 103, 460, 452, 602]

a = []
b = []
for i in birinci_liste:
    if (not i in ikinci_liste):
        a.append(i)
print("Birinci listede olup ikinci listede olmayan sayılar: ", a)

for i in ikinci_liste:
    if(not i in birinci_liste):
        b.append(i)
print("İkinci listenin içinde olup birinci listenin içinde olmayan sayılar: ", b)


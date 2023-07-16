ogrenci = {"Ali": [90, 67, 80], "Mustafa": [58, 45, 65], "Osman": [85, 90, 95],
           "Meryem": [56, 57, 58], "Eda": [59, 60, 61]}
isim = input("Lütfen notlarını görmek istediğiniz öğrencinin adını girin: ")
ortalama = (ogrenci[isim][0] + ogrenci[isim][1] + ogrenci[isim][2])/3
print(""""{} isimli öğrencinin 1.Sınav Notu: {}
2.Sınav Notu: {}
3.Sınav Notu: {}""".format(isim, ogrenci[isim][0], ogrenci[isim][1], ogrenci[isim][2]))
print("Not Ortalaması: {}".format(ortalama))
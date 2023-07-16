tarih = input("""Tarih girin :
ör:01/01/1999
""")
konu = input("Konuyu girin :")
ad = input("Ad ve soyad girin :")
adres = input("Adres girin :")
tel = input("Telefon numarası :")

print("""TIP FAKÜLTESİ DEKANLIĞINA İSTANBUL {}

Konu:{}

Gereğinin yapılmasını arz ederim. Saygılarımla,

Ad-Soyad:{}

Adres Bilgileri:{}

Telefon:{}""".format(tarih,konu,ad,adres,tel))
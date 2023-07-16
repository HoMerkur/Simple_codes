telefon_rehberi = {"Ahmet": "0525 456 23 56",
                   "Mehmet": "0596 569 78 45",
                   "Ali": "0549 678 32 27",
                   "Osman": "0531 436 85 85"}
kisi = input("Lütfen numarasını öğrenmek istediğiniz kişinin adını girin:")
print("{} isimli kişinin numarası şu şekildedir: {}".format(kisi, telefon_rehberi[kisi]))
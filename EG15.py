calisanlar = {"Mert": ["Bursa", 25, "Makine teknikeri"],
              "Osman": ["Adıyaman", 20, "Stajyer"],
              "Ayşe": ["Giresun", 27, "Kordinatör"],
              "Murat": ["Mersin", 35, "Genel Müdür"]}
isim = input("Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: ")
print("{}= Memleket: {} Yaş: {} Görev: {}".format(isim, calisanlar[isim][0],
                                                  calisanlar[isim][1],
                                                  calisanlar[isim][2]))
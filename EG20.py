print("""Pizza Fiytları
Büyük Boy: 30 TL
Orta Boy: 22 TL
Küçük Boy: 15 TL""")
pizza = input("Almak istediğiniz pizzayı girin:\n"
              "(Lütfen bütün hafleri küçük girin)")
if(pizza == "Büyük Boy" or pizza == "Büyük boy" or pizza == "büyük"):
    print("""Seçiminiz: Büyük Boy
    Ödemeniz Gereken Miktar: 30 TL""")
elif(pizza == "Orta Boy" or pizza == "Orta boy" or pizza == "orta"):
    print("""Seçiminiz: Orta Boy
    Ödemeniz Gereken Tutar: 22 TL""")
elif(pizza == "Küçük Boy" or pizza == "Küçük boy" or pizza == "küçük"):
    print("""Seçiminiz: Küçük Boy
    Ödemeniz Gereken Tutar: 15 TL""")

else:
    print("Hatalı giriş yaptınız!")
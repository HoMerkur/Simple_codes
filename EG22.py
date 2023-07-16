while True:
    sifre = input("""Paroa belirleyin: """)
    if(not sifre):
        print("Parola boş bırakılamaz!")

    elif(len(sifre) in range(3,9)):
        print("Parolanız başarıyla oluşturuldu.")
        break
    else:
        print("Parolanız 8 karakterden fazla 3 karakterden az olamaz.")
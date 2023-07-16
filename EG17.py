kullanici_ad = input("Bir kullanıcı adı belirleyin: ")
parola = input("Bir parola belirleyin: ")
toplam = len(kullanici_ad) + len(parola)

if( toplam <= 20):
    print("Parolanız başarıyla oluşturuldu.")

else:
    print("Kullanıcı adı ve parolanızın toplam uzunluğu 20 karakteri geçmemeli!")
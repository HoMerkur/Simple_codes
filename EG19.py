vize1 = int(input("Birinci vize notunuzu girin: "))
vize2 = int(input("İkinci vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

ortalama = int(vize1*3/10 + vize2*3/10 + final*4/10)

if(ortalama <= 100 and ortalama >= 90):
    print("Notunuz AA")

elif(ortalama >= 85 and ortalama <=89):
    print("Notunuz BA")

elif(ortalama >= 80 and ortalama <= 84):
    print("Notunuz BB")

elif(ortalama >=75 and ortalama <= 79):
    print("Notunuz CB")

elif(ortalama >= 70 and ortalama <= 74):
    print("Notunuz CC")

elif(ortalama >= 65 and ortalama <= 69):
    print("Notunuz DC")

elif(ortalama >= 60 and ortalama <=64):
    print("Notunuz DD")

elif(ortalama >= 50 and ortalama <= 59):
    print("Notunuz FD")

elif(ortalama >= 0 and ortalama <= 49):
    print("Notunuz FF")

else:
    print("Hatalı giriş yaptınız.")
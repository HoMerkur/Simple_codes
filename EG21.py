ates = float(input("Lütfen ateşinizi girin: "))

if(ates <= 38 and ates >= 36):
    print("AVM'ye Girebilirsiniz.")
elif(ates > 38 or ates < 36):
    print("Ateşiniz {} derece. AVM'ye Giremezsiniz".format(ates))
else:
    print("Hatalı giriş yaptınız!")
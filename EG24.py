metin = """Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. 
Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini
 alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. 
 Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır.
  1960'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda 
Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur."""



harf = input("Kaç defa geçtiğini öğrenmek istediğiniz harfi girin: ")

a = 0
for i in metin:
    if(harf == i):
            a += 1
print(harf, "Harfi metin içerisinde {} defa geçmektedir.".format(a))
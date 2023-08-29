# Bu şekilde fonksiyonları direk import edebiliriz
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

import os, sys


# Yukarıda yaptığımız importlama işlemi sayesinde tekrardan sınıfı çağırmadan fonksiyonunu kullanabiliriz
class ManWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Yazdığımız kısım burası
        self.editor = QPlainTextEdit()
        # Pencereye dahil ediyoruz
        self.setCentralWidget(self.editor)

        # Yazı fontunu ayarladığımız kod
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(12)
        self.editor.setFont(font)

        self.path = None

        # Status bar(Mesajların yazıldığı bar) oluşturduğumuz kod
        status = QStatusBar()
        self.setStatusBar(status)

        # Tool bar oluşturduğumuzkısım
        # //Kaydetme gibi işlemlerin manuel olarak yapılmasını sağlayan objelerin bulunduğu bar//
        toolbar = QToolBar()
        # Objelerin boyutlarını ayarladığımız kısım
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)

        menu_bar = QMenuBar()
        menu_bar = self.menuBar()

        dosya_menu = menu_bar.addMenu("Dosya")
        ekle_menu = menu_bar.addMenu("Ekle")

        # Menu ve Tool barlarına Action eklediğimiz kodlar
        # Action larımıza kısayol, bilgi yazısı ve ikon eklediğimiz kodlar
        dosya_ac = QAction(QIcon(os.path.join("dosya_ac.png")), "Dosya Aç", self)
        dosya_ac.setStatusTip("Dışarıdan Başka Bir Text Dosyasını NotePad'inize Açmanızı Sağlar")
        dosya_ac.setShortcut("Ctrl+O")
        toolbar.addAction(dosya_ac)
        dosya_menu.addAction(dosya_ac)

        kaydet = QAction(QIcon(os.path.join("kaydet.png")), "Kaydet", self)
        kaydet.setStatusTip("Oluşturduğunuz Notlarınızı txt Olarak Kaydeder")
        kaydet.setShortcut("Ctrl+S")
        toolbar.addAction(kaydet)
        dosya_menu.addAction(kaydet)

        farkli_kaydet = QAction(QIcon(os.path.join("farkli_kaydet.png")), "Farklı Kaydet", self)
        farkli_kaydet.setStatusTip("NotPad'i İstediğiniz Konumda ve Formatta Kaydetmenizi Sağlar")
        toolbar.addAction(farkli_kaydet)
        dosya_menu.addAction(farkli_kaydet)

        yazdir = QAction(QIcon(os.path.join("yazdir.png")), "Yazdır", self)
        yazdir.setStatusTip("Dosyanızı Yazdırmanızı Sağlar")
        yazdir.setShortcut("Ctrl+P")
        dosya_menu.addAction(yazdir)

        geri_al = QAction(QIcon(os.path.join("geri_al.png")), "Geri Al", self)
        geri_al.setStatusTip("İşleminizi Geri Almanızı Sağlar")
        geri_al.setShortcut("Crtl+Z")
        ekle_menu.addAction(geri_al)
        toolbar.addAction(geri_al)

        ileri_al = QAction(QIcon(os.path.join("ileri_al.png")), "İleri Al", self)
        ileri_al.setShortcut("Ctrl+Y")
        ileri_al.setStatusTip("Geri Aldığınız İşlemi Tekrar Yapar")
        toolbar.addAction(ileri_al)
        ekle_menu.addAction(ileri_al)

        kes = QAction(QIcon(os.path.join("kes.png")), "Kes", self)
        kes.setStatusTip("Seçtiğiniz Öğeyi Keser")
        kes.setShortcut("Ctrl+X")
        toolbar.addAction(kes)
        ekle_menu.addAction(kes)

        kopyala = QAction(QIcon(os.path.join("kopyala.png")), "Kopyala", self)
        kopyala.setStatusTip("Seçtiğiniz Öğeyi Kopyalar")
        kopyala.setShortcut("Ctrl+C")
        toolbar.addAction(kopyala)
        ekle_menu.addAction(kopyala)

        yapistir = QAction(QIcon(os.path.join("yapistir.png")), "Yapıştır", self)
        yapistir.setStatusTip("Kestiğiniz veya Kopyaladığınız Öğeyi Yapıştırır")
        yapistir.setShortcut("Ctrl+V")
        toolbar.addAction(yapistir)
        ekle_menu.addAction(yapistir)

        hepsini_sec = QAction(QIcon(os.path.join("hepsini_sec.png")), "Hepsini Seç", self)
        hepsini_sec.setShortcut("Ctrl+A")
        hepsini_sec.setStatusTip("Bütün Öğeleri Seçmenizi Sağlar")
        toolbar.addAction(hepsini_sec)
        ekle_menu.addAction(hepsini_sec)

        # // Fonksiyonların Parantezleri Olmadan Verilmesi Lazım! //
        dosya_ac.triggered.connect(self.dosya_ac_def)
        kaydet.triggered.connect(self.kaydet_def)
        farkli_kaydet.triggered.connect(self.farkli_kaydet_def)
        yazdir.triggered.connect(self.yazdir_def)
        # .undo fonksiyonu editor'e atadığımız TextEdit içide tanımlı geri alma fonksiyonu
        geri_al.triggered.connect(self.editor.undo)
        # .redo fonksiyonu editor'e atadığımız TextEdit içide tanımlı ileri alma fonksiyonu
        ileri_al.triggered.connect(self.editor.redo)
        # .cut fonksiyonu editor'e atadığımız TextEdit içide tanımlı kesme fonksiyonu
        kes.triggered.connect(self.editor.cut)
        # .copy fonksiyonu editor'e atadığımız TextEdit içide tanımlı kopyalama fonksiyonu
        kopyala.triggered.connect(self.editor.copy)
        # .paste fonksiyonu editor'e atadığımız TextEdit içide tanımlı yapıştrma fonksiyonu
        yapistir.triggered.connect(self.editor.paste)
        # .selectAll fonksiyonu editor'e atadığımız TextEdit içide tanımlı hepsini seçme fonksiyonu
        hepsini_sec.triggered.connect(self.editor.selectAll)

        self.basligi_guncelle()
        self.setGeometry(250, 250, 500, 500)
        self.show()

    def basligi_guncelle(self):
        self.setWindowTitle("{} - NotePad".format(os.path.basename(self.path) if self.path else "Untitled"))

    def dosya_ac_def(self):
        path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Text Dosyaları(*.txt)")
        if path:
            try:
                with open(path, "r") as file:
                    text = file.read()
            except Exception as e:
                self.hata_mesaj(e)
            else:
                self.editor.setPlainText(text)
                self.path = path
                self.basligi_guncelle()

    def kaydet_def(self):
        if self.path == None:
            return self.farkli_kaydet_def()

        text = self.editor.toPlainText()

        try:
            with open(self.path, "w") as file:
                file.write(text)
        except Exception as e:
            self.hata_mesaj(e)

    def hata_mesaj(self, mesaj):
        hata = QMessageBox()
        hata.setText(mesaj)
        hata.setIcon(QMessageBox.Critical)
        hata.show()

    def farkli_kaydet_def(self):
        path, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Text Dosyaları(*.txt)")

        if not path:
            return
        text = self.editor.toPlainText()
        try:
            with open(path, "w") as file:
                file.write(text)
        except Exception as e:
            self.hata_mesaj(e)
        else:
            self.path = path
            self.basligi_guncelle()

    def yazdir_def(self):
        mesaj = QPrintDialog()
        if mesaj.exec_():
            self.editor.print_(mesaj.printer())

# Bu proje çalıştırılırken başka bir dosya üzerinden çalıştırılmasını engelleyen bir koşullu durum
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("NotePad")

    window = ManWindow()

    app.exec_()

import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.fiyat_list = list()
        self.birim = list()
        self.refresh()
        self.init_ui()

    def init_ui(self):

        refresh_buton = QtWidgets.QPushButton("Yenile")
        refresh_buton.clicked.connect(self.refresh)

        vertical_layout1 = QtWidgets.QVBoxLayout()
        vertical_layout1.addStretch()
        vertical_layout1.addWidget(QtWidgets.QLabel(self.birim[0]))
        vertical_layout1.addWidget(self.birim[1])
        vertical_layout1.addWidget(self.birim[2])
        vertical_layout1.addWidget(self.birim[3])
        vertical_layout1.addWidget(self.birim[4])
        vertical_layout1.addStretch()

        vertical_layoot2 = QtWidgets.QVBoxLayout()
        vertical_layoot2.addStretch()
        vertical_layoot2.addWidget(self.fiyat_text1)
        vertical_layoot2.addWidget(self.fiyat_text2)
        vertical_layoot2.addWidget(self.fiyat_text3)
        vertical_layoot2.addWidget(self.fiyat_text4)
        vertical_layoot2.addWidget(self.fiyat_text5)
        vertical_layoot2.addStretch()

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addLayout(vertical_layoot1)
        horizontal_layout.addLayout(vertical_layoot2)
        horizontal_layout.addStretch()

        self.setLayout(horizontal_layout)



    def refresh(self):
        url = "https://finans.mynet.com/borsa/"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"}
        response = requests.get(url, headers=headers)

        content = response.content

        html_veri = BeautifulSoup(content, "html.parser")
        div_element = html_veri.find_all("div", {"class": "widget-data-bar"})

        for i in div_element[0].find_all("span", {"class": "name"}):
            self.birim.append(i.text)
        self.birim_text1 = QtWidgets.QLabel()
        self.birim_text2 = QtWidgets.QLabel()
        self.birim_text3 = QtWidgets.QLabel()
        self.birim_text4 = QtWidgets.QLabel()
        self.birim_text5 = QtWidgets.QLabel()




        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-XU100"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-USDTRY"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-EURTRY"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-EURUSD"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-GAUTRY"}))

        self.fiyat_text1 = QtWidgets.QLabel(str(self.fiyat_list[0]))
        self.fiyat_text2 = QtWidgets.QLabel(str(self.fiyat_list[1]))
        self.fiyat_text3 = QtWidgets.QLabel(str(self.fiyat_list[2]))
        self.fiyat_text4 = QtWidgets.QLabel(str(self.fiyat_list[3]))
        self.fiyat_text5 = QtWidgets.QLabel(str(self.fiyat_list[4]))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(250, 250, 300, 200)
    window.show()
    sys.exit(app.exec_())

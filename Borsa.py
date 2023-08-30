
import sys
from bs4 import BeautifulSoup
import requests
from PyQt5 import QtWidgets
import subprocess


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.yazi1 = None
        self.yazi2 = None
        self.yazi3 = None
        self.yazi4 = None
        self.yazi5 = None
        self.fiyat_list = None
        self.birim_list = None
        self.refresh()
        self.init_ui()

    def init_ui(self):
        refresh_button = QtWidgets.QPushButton("Yenile")

        vertical_layout1 = QtWidgets.QVBoxLayout()
        vertical_layout1.addStretch()
        vertical_layout1.addWidget(self.yazi1)
        vertical_layout1.addWidget(self.yazi2)
        vertical_layout1.addWidget(self.yazi3)
        vertical_layout1.addWidget(self.yazi4)
        vertical_layout1.addWidget(self.yazi5)
        vertical_layout1.addStretch()

        vertical_layout2 = QtWidgets.QVBoxLayout()
        vertical_layout2.addStretch()
        vertical_layout2.addWidget(QtWidgets.QLabel(str(self.fiyat_list[0])))
        vertical_layout2.addWidget(QtWidgets.QLabel(str(self.fiyat_list[1])))
        vertical_layout2.addWidget(QtWidgets.QLabel(str(self.fiyat_list[2])))
        vertical_layout2.addWidget(QtWidgets.QLabel(str(self.fiyat_list[3])))
        vertical_layout2.addWidget(QtWidgets.QLabel(str(self.fiyat_list[4])))
        vertical_layout2.addStretch()

        vertical_layout3 = QtWidgets.QVBoxLayout()
        vertical_layout3.addStretch()
        vertical_layout3.addWidget(refresh_button)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addLayout(vertical_layout1)
        horizontal_layout.addLayout(vertical_layout2)
        horizontal_layout.addStretch()
        horizontal_layout.addLayout(vertical_layout3)

        refresh_button.clicked.connect(self.close)
        refresh_button.clicked.connect(self.real_refresh)

        self.setLayout(horizontal_layout)
        self.show()

    def refresh(self):
        url = "https://finans.mynet.com/borsa/"

        headers = {"User-Agent": "TheUserAgent"}
        response = requests.get(url, headers=headers)

        content = response.content

        html_veri = BeautifulSoup(content, "html.parser")
        div_element = html_veri.find_all("div", {"class": "widget-data-bar"})
        self.birim_list = list()
        self.fiyat_list = list()
        for i in div_element[0].find_all("span", {"class": "name"}):
            self.birim_list.append(i)
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-XU100"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-USDTRY"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-EURTRY"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-EURUSD"}))
        self.fiyat_list.append(div_element[0].find_all("span", {"class": "dynamic-price-GAUTRY"}))
        self.yazi1 = QtWidgets.QLabel(str(self.birim_list[0]))
        self.yazi2 = QtWidgets.QLabel(str(self.birim_list[1]))
        self.yazi3 = QtWidgets.QLabel(str(self.birim_list[2]))
        self.yazi4 = QtWidgets.QLabel(str(self.birim_list[3]))
        self.yazi5 = QtWidgets.QLabel(str(self.birim_list[4]))

    def real_refresh(self):
        subprocess.run(['python', 'Borsa.py'], check=True)
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(250, 250, 300, 100)
    sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("PyQt5 Demo")
window.setGeometry(750, 250, 500, 500)

yazi = QtWidgets.QLabel(window)
yazi.setText("Hello World")
yazi.move(200, 50)

resim = QtWidgets.QLabel(window)
resim.setPixmap(QtGui.QPixmap("python.png"))
resim.move(110, 100)

buton = QtWidgets.QPushButton(window)
buton.setText("Buton")
buton.move(190, 380)



window.show()
sys.exit(app.exec_())






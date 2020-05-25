from PyQt5.QtWidgets import QApplication # esto me permite trabajarlo como aplicacion
from PyQt5.QtWidgets import QLabel 
from PyQt5.QtWidgets import QWidget #importar lo necesario para trabajar con widgets

app = QApplication([])

window = QWidget()
window.setWindowTitle('CARROS')
window.setGeometry(100, 100, 280, 280)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()
app.exec_()
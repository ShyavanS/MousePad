# 1. Import `QApplication` and all the required widgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QMainWindow, QWidget, QVBoxLayout
from IO import *
import sys
# Drop down for every button
# Slider for vibration sensitivity
# Number for vibration timerr
# Movement Scroll Speed
# Controller ID
# Reset to Default


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setGeometry(560, 370, 800, 300)
        self.setWindowTitle("MousePad Configuration")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Controller Mapping")
        self.label.move(350, 0)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Reset To Default")
        self.b1.move(400, 100)
        self.b1.clicked.connect(self.clicked)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Left Joystick")
        self.label.move(5, 10)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Right Joystick")
        self.label.move(5, 30)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("A")
        self.label.move(5, 50)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("B")
        self.label.move(5, 70)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("X")
        self.label.move(5, 90)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Y")
        self.label.move(5, 110)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Up")
        self.label.move(5, 130)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Down")
        self.label.move(5, 150)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Left")
        self.label.move(5, 170)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Right")
        self.label.move(5, 190)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("R1")
        self.label.move(5, 210)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("R2")
        self.label.move(5, 230)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("L1")
        self.label.move(5, 250)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("L2")
        self.label.move(5, 270)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.label.move(400, 100)
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setGeometry(560, 370, 800, 300)
    win.setWindowTitle("MousePad Configuration")

    win.show()
    sys.exit(app.exec_())


window()

from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Kumir
import sys
app = QtWidgets.QApplication(sys.argv)

Kumir = QtWidgets.QWidget()
ui = Ui_Kumir()
ui.setupUi(Kumir)
Kumir.show()

code = ""

Kumirs = ["влево", "вправо", "вверх", "вниз"]
Pythons = ["left()", "right()", "up()", "down()"]

xcoord = ui.label.pos().x()
ycoord = ui.label.pos().y()


def left():
    global xcoord
    global ycoord
    xcoord -= 40
    ui.label.move(xcoord, ycoord)


def right():
    global xcoord
    global ycoord
    xcoord += 40
    ui.label.move(xcoord, ycoord)


def up():
    global xcoord
    global ycoord
    ycoord -= 40
    ui.label.move(xcoord, ycoord)


def down():
    global xcoord
    global ycoord
    ycoord += 40
    ui.label.move(xcoord, ycoord)


def read():
    global code
    code = ui.textEdit.toPlainText()
    for i in code.splitlines():
        # print(code.splitlines()[i])
        if i in Kumirs:
            code = code.replace(Kumirs[Kumirs.index(i)], Pythons[Kumirs.index(i)])
        else:
            code = code.replace(i, "")


def launch():
    read()
    print(code)
    try:
        exec(code)
    except NameError:
        print("A?")
    ui.tabWidget.setCurrentIndex(1)


ui.pushButton.clicked.connect(launch)


sys.exit(app.exec_())

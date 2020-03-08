from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Kumir
import sys
app = QtWidgets.QApplication(sys.argv)

Kumir = QtWidgets.QWidget()
ui = Ui_Kumir()
ui.setupUi(Kumir)
Kumir.show()

code = ""

Kumirs = ["влево", "вправо", "вверх", "вниз", "цикл", "закрасить"]
Pythons = ["left", "right", "up", "down", "for i in range", "color"]

xcoord = ui.label.pos().x()
ycoord = ui.label.pos().y()
colored_cells = 0

def left(a):
    global xcoord
    global ycoord
    if xcoord > 20:
        xcoord -= (40 * a)
        ui.label.move(xcoord, ycoord)


def right(a):
    global xcoord
    global ycoord
    if xcoord < 1060:
        xcoord += (40 * a)
    ui.label.move(xcoord, ycoord)


def up(a):
    global xcoord
    global ycoord
    if ycoord > 10:
        ycoord -= (40 * a)
    ui.label.move(xcoord, ycoord)


def down(a):
    global xcoord
    global ycoord
    if ycoord < 850:
        ycoord += (40 * a)
    ui.label.move(xcoord, ycoord)


def color():
    global colored_cells
    global xcoord
    global ycoord
    colored_cells += 1
    exec("ui.cell_" + str(colored_cells) + " = QtWidgets.QLabel(ui.tab_2)"+ "\n"+
    "ui.cell_" + str(colored_cells) + ".setGeometry(QtCore.QRect(xcoord, ycoord, 40, 40))"+ "\n"+
    "ui.cell_" + str(colored_cells) + """.setStyleSheet("QLabel{""background-color: red;""}")"""+ "\n"+
    "ui.cell_" + str(colored_cells) + ".setObjectName('cell_' + str(colored_cells))" + "\n" +
    "ui.cell_" + str(colored_cells) + ".show()" + "\n"+
    "ui.label.show()")


def read():
    global code
    code = ui.textEdit.toPlainText()
    for i in Kumirs:
        code = code.replace(Kumirs[Kumirs.index(i)], Pythons[Kumirs.index(i)])


def launch():
    ui.label.move(500, 490)
    ui.tabWidget.setCurrentIndex(1)
    read()
    try:
        exec(code)
    finally:
        print("ubi")
    """except NameError:
        print("пиши код нормально б*лин")
    except SyntaxError:
        print("пиши код нормально б*лин")"""



ui.pushButton.clicked.connect(launch)


sys.exit(app.exec_())

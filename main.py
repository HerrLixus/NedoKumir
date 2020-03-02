from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Kumir
import sys
app = QtWidgets.QApplication(sys.argv)

Kumir = QtWidgets.QWidget()
ui = Ui_Kumir()
ui.setupUi(Kumir)
Kumir.show()


def Read():
    print(ui.textEdit.toPlainText())


ui.pushButton.clicked.connect(Read)
sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showbook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showbook(object):
    def setupUi(self, showbook):
        showbook.setObjectName("showbook")
        showbook.resize(694, 414)
        showbook.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(showbook)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 581, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:black;color:white;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 350, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setStyleSheet("color :black;\n"
"background:yellow;")
        self.back.setObjectName("back")
        showbook.setCentralWidget(self.centralwidget)

        self.retranslateUi(showbook)
        QtCore.QMetaObject.connectSlotsByName(showbook)

    def retranslateUi(self, showbook):
        _translate = QtCore.QCoreApplication.translate
        showbook.setWindowTitle(_translate("showbook", "Show Book"))
        self.back.setText(_translate("showbook", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showbook = QtWidgets.QMainWindow()
    ui = Ui_showbook()
    ui.setupUi(showbook)
    showbook.show()
    sys.exit(app.exec_())


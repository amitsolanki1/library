# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addbook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addbook(object):
    def setupUi(self, addbook):
        addbook.setObjectName("addbook")
        addbook.resize(621, 347)
        icon = QtGui.QIcon.fromTheme("dfsa")
        addbook.setWindowIcon(icon)
        addbook.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(addbook)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"")
        self.label.setObjectName("label")
        self.bookname = QtWidgets.QLabel(self.centralwidget)
        self.bookname.setGeometry(QtCore.QRect(80, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.bookname.setFont(font)
        self.bookname.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.bookname.setObjectName("bookname")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 150, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit.setObjectName("lineEdit")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(180, 280, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setStyleSheet("color :black;\n"
"background:yellow;")
        self.back.setObjectName("back")
        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(300, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("color:rgb(0, 0, 0);\n"
"background:yellow;")
        self.addbtn.setObjectName("addbtn")
        addbook.setCentralWidget(self.centralwidget)

        self.retranslateUi(addbook)
        QtCore.QMetaObject.connectSlotsByName(addbook)

    def retranslateUi(self, addbook):
        _translate = QtCore.QCoreApplication.translate
        addbook.setWindowTitle(_translate("addbook", "ADD BOOK"))
        self.label.setText(_translate("addbook", "  "))
        self.bookname.setText(_translate("addbook", " Book Name:"))
        self.back.setText(_translate("addbook", "Back"))
        self.addbtn.setText(_translate("addbook", "ADD Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addbook = QtWidgets.QMainWindow()
    ui = Ui_addbook()
    ui.setupUi(addbook)
    addbook.show()
    sys.exit(app.exec_())


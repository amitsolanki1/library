# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issuebook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_issuebook(object):
    def setupUi(self, issuebook):
        issuebook.setObjectName("issuebook")
        issuebook.resize(618, 365)
        issuebook.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(issuebook)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.bookname = QtWidgets.QLabel(self.centralwidget)
        self.bookname.setGeometry(QtCore.QRect(80, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.bookname.setFont(font)
        self.bookname.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.bookname.setObjectName("bookname")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 521, 51))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.issuebtn = QtWidgets.QPushButton(self.centralwidget)
        self.issuebtn.setGeometry(QtCore.QRect(300, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.issuebtn.setFont(font)
        self.issuebtn.setStyleSheet("color:rgb(0, 0, 0);\n"
"background:yellow;")
        self.issuebtn.setObjectName("issuebtn")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.rollno = QtWidgets.QLabel(self.centralwidget)
        self.rollno.setGeometry(QtCore.QRect(80, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.rollno.setFont(font)
        self.rollno.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.rollno.setObjectName("rollno")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(180, 300, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setStyleSheet("color :black;\n"
"background:yellow;")
        self.back.setObjectName("back")
        issuebook.setCentralWidget(self.centralwidget)

        self.retranslateUi(issuebook)
        QtCore.QMetaObject.connectSlotsByName(issuebook)

    def retranslateUi(self, issuebook):
        _translate = QtCore.QCoreApplication.translate
        issuebook.setWindowTitle(_translate("issuebook", "Issue Book"))
        self.bookname.setText(_translate("issuebook", " Book Name:"))
        self.issuebtn.setText(_translate("issuebook", "Issue Book"))
        self.rollno.setText(_translate("issuebook", " Roll NO. ;"))
        self.back.setText(_translate("issuebook", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issuebook = QtWidgets.QMainWindow()
    ui = Ui_issuebook()
    ui.setupUi(issuebook)
    issuebook.show()
    sys.exit(app.exec_())


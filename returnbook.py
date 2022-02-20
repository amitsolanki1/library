# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returnbook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_returnbook(object):
    def setupUi(self, returnbook):
        returnbook.setObjectName("returnbook")
        returnbook.resize(618, 360)
        returnbook.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(returnbook)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.returnbtn = QtWidgets.QPushButton(self.centralwidget)
        self.returnbtn.setGeometry(QtCore.QRect(310, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.returnbtn.setFont(font)
        self.returnbtn.setStyleSheet("color:rgb(0, 0, 0);\n"
"background:yellow;")
        self.returnbtn.setObjectName("returnbtn")
        self.bookname = QtWidgets.QLabel(self.centralwidget)
        self.bookname.setGeometry(QtCore.QRect(90, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.bookname.setFont(font)
        self.bookname.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.bookname.setObjectName("bookname")
        self.rollno = QtWidgets.QLabel(self.centralwidget)
        self.rollno.setGeometry(QtCore.QRect(90, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.rollno.setFont(font)
        self.rollno.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.rollno.setObjectName("rollno")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: white\n"
";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(180, 300, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.back.setFont(font)
        self.back.setStyleSheet("color :black;\n"
"background:yellow;")
        self.back.setObjectName("back")
        returnbook.setCentralWidget(self.centralwidget)

        self.retranslateUi(returnbook)
        QtCore.QMetaObject.connectSlotsByName(returnbook)

    def retranslateUi(self, returnbook):
        _translate = QtCore.QCoreApplication.translate
        returnbook.setWindowTitle(_translate("returnbook", "Return Book"))
        self.returnbtn.setText(_translate("returnbook", "Return Book"))
        self.bookname.setText(_translate("returnbook", " Book Name:"))
        self.rollno.setText(_translate("returnbook", " Roll NO. ;"))
        self.back.setText(_translate("returnbook", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    returnbook = QtWidgets.QMainWindow()
    ui = Ui_returnbook()
    ui.setupUi(returnbook)
    returnbook.show()
    sys.exit(app.exec_())


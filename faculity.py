# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faculity.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Faculity(object):
    def setupUi(self, Faculity):
        Faculity.setObjectName("Faculity")
        Faculity.resize(698, 560)
        Faculity.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(Faculity)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 60, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"background-color: rgb(255, 0, 0);\n"
"color:white;;")
        self.label.setObjectName("label")
        self.showbtn = QtWidgets.QPushButton(self.centralwidget)
        self.showbtn.setGeometry(QtCore.QRect(250, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.showbtn.setFont(font)
        self.showbtn.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.showbtn.setObjectName("showbtn")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(250, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.add.setObjectName("add")
        self.issue = QtWidgets.QPushButton(self.centralwidget)
        self.issue.setGeometry(QtCore.QRect(250, 320, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.issue.setFont(font)
        self.issue.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.issue.setObjectName("issue")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(250, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.return_2.setFont(font)
        self.return_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.return_2.setObjectName("return_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(300, 480, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color:yellow;\n"
"color:black;")
        self.back.setObjectName("back")
        Faculity.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Faculity)
        self.statusbar.setObjectName("statusbar")
        Faculity.setStatusBar(self.statusbar)

        self.retranslateUi(Faculity)
        QtCore.QMetaObject.connectSlotsByName(Faculity)

    def retranslateUi(self, Faculity):
        _translate = QtCore.QCoreApplication.translate
        Faculity.setWindowTitle(_translate("Faculity", "MainWindow"))
        self.label.setText(_translate("Faculity", "   Staff / Faculity"))
        self.showbtn.setText(_translate("Faculity", "showbtn Books"))
        self.add.setText(_translate("Faculity", "Add Books"))
        self.issue.setText(_translate("Faculity", "Issue Book"))
        self.return_2.setText(_translate("Faculity", "Return Book"))
        self.back.setText(_translate("Faculity", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Faculity = QtWidgets.QMainWindow()
    ui = Ui_Faculity()
    ui.setupUi(Faculity)
    Faculity.showbtn()
    sys.exit(app.exec_())


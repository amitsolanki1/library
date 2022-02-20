# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome_screen(object):
    def setupUi(self, welcome_screen):
        welcome_screen.setObjectName("welcome_screen")
        welcome_screen.resize(696, 435)
        welcome_screen.setStyleSheet("background:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(welcome_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 631, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color:white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 280, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color :black;\n"
"background:yellow;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 280, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color :black;\n"
"background:yellow;")
        self.pushButton_2.setObjectName("pushButton_2")
        welcome_screen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(welcome_screen)
        self.statusbar.setObjectName("statusbar")
        welcome_screen.setStatusBar(self.statusbar)

        self.retranslateUi(welcome_screen)
        QtCore.QMetaObject.connectSlotsByName(welcome_screen)

    def retranslateUi(self, welcome_screen):
        _translate = QtCore.QCoreApplication.translate
        welcome_screen.setWindowTitle(_translate("welcome_screen", "Library"))
        self.label.setText(_translate("welcome_screen", " Welcome To Python Library "))
        self.pushButton.setText(_translate("welcome_screen", "Student"))
        self.pushButton_2.setText(_translate("welcome_screen", "Faculity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome_screen = QtWidgets.QMainWindow()
    ui = Ui_welcome_screen()
    ui.setupUi(welcome_screen)
    welcome_screen.show()
    sys.exit(app.exec_())


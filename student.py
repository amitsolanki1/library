# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_student(object):
    def setupUi(self, student):
        student.setObjectName("student")
        student.resize(701, 555)
        student.setStyleSheet("background-color: balck;;")
        self.centralwidget = QtWidgets.QWidget(student)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(0, 0, 0);\n"
"background:yellow;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 470, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color :black;\n"
"background:yellow;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 621, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 360, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color:back;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 230, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 300, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 360, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:balck;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        student.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(student)
        self.statusbar.setObjectName("statusbar")
        student.setStatusBar(self.statusbar)

        self.retranslateUi(student)
        QtCore.QMetaObject.connectSlotsByName(student)

    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "MainWindow"))
        self.pushButton.setText(_translate("student", "Login"))
        self.pushButton_2.setText(_translate("student", "Back"))
        self.label.setText(_translate("student", "  Student Registration /Login"))
        self.label_2.setText(_translate("student", " Name:"))
        self.label_3.setText(_translate("student", "Roll Number:"))
        self.label_4.setText(_translate("student", "Branch:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student = QtWidgets.QMainWindow()
    ui = Ui_student()
    ui.setupUi(student)
    student.show()
    sys.exit(app.exec_())


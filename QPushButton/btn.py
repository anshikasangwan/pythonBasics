# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'btn.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(329, 244)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.btnstate)
        self.b1.setObjectName("b1")
        self.verticalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(lambda:self.chkbtn(self.b2))
        self.b2.clicked.connect(self.chkbtn)
        self.verticalLayout.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(lambda:self.chkbtn(self.b3))
        self.b3.clicked.connect(self.chkbtn)
        self.verticalLayout.addWidget(self.b3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "PushButton"))
        self.b2.setText(_translate("Form", "Button2"))
        self.b3.setText(_translate("Form", "Button3"))
    def chkbtn(self,b):
        print ("caption of pressed button :", b.text())
    def btnstate(self):
        if self.b1.isChecked():
            self.b1.setText("pressed")
        else:
            self.b1.setText("released")

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


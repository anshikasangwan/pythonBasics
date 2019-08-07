# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chkbox.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 154)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.verticalLayout.addWidget(self.t1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb1 = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.horizontalLayout.addWidget(self.cb1)
        self.cb2 = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb2.setFont(font)
        self.cb2.setObjectName("cb2")
        self.horizontalLayout.addWidget(self.cb2)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cb1.stateChanged.connect(self.checkstate)
        self.cb2.stateChanged.connect(self.checkstate)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cb1.setText(_translate("Form", "CB1"))
        self.cb2.setText(_translate("Form", "CB2"))

    def checkstate(self):
        state1='Unchecked'
        state2='Unchecked'
        if self.cb1.isChecked()==True:
            state1='Checked'
        else:
            state1='Unchecked'
        if self.cb2.isChecked()==True:
            state2='Checked'
        else:
            state2='Unchecked'
        self.t1.setText("cb1 is {} cb2 is {}".format(state1,state2))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


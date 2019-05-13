# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'componentdetails.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComponentDetailsDialog(object):
    def setupUi(self, ComponentDetailsDialog):
        ComponentDetailsDialog.setObjectName("ComponentDetailsDialog")
        ComponentDetailsDialog.resize(444, 481)
        self.formLayoutWidget = QtWidgets.QWidget(ComponentDetailsDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 391, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ComponentDetailsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 450, 336, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(ComponentDetailsDialog)
        self.buttonBox.accepted.connect(ComponentDetailsDialog.accept)
        self.buttonBox.rejected.connect(ComponentDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ComponentDetailsDialog)

    def retranslateUi(self, ComponentDetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        ComponentDetailsDialog.setWindowTitle(_translate("ComponentDetailsDialog", "Component details"))
        self.label.setText(_translate("ComponentDetailsDialog", "Name: "))
        self.label_2.setText(_translate("ComponentDetailsDialog", "Description: "))



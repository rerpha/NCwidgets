# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcomponentwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddComponentDialog(object):
    def setupUi(self, AddComponentDialog):
        AddComponentDialog.setObjectName("AddComponentDialog")
        AddComponentDialog.resize(225, 139)
        self.formLayout_2 = QtWidgets.QFormLayout(AddComponentDialog)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(AddComponentDialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(AddComponentDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(AddComponentDialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(AddComponentDialog)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_3 = QtWidgets.QLabel(AddComponentDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(AddComponentDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line = QtWidgets.QFrame(AddComponentDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line)
        self.line_2 = QtWidgets.QFrame(AddComponentDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddComponentDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(AddComponentDialog)
        QtCore.QMetaObject.connectSlotsByName(AddComponentDialog)

    def retranslateUi(self, AddComponentDialog):
        _translate = QtCore.QCoreApplication.translate
        AddComponentDialog.setWindowTitle(_translate("AddComponentDialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("AddComponentDialog", "Detector"))
        self.comboBox.setItemText(1, _translate("AddComponentDialog", "Monitor"))
        self.comboBox.setItemText(2, _translate("AddComponentDialog", "Source"))
        self.comboBox.setItemText(3, _translate("AddComponentDialog", "Slit"))
        self.comboBox.setItemText(4, _translate("AddComponentDialog", "Moderator"))
        self.comboBox.setItemText(5, _translate("AddComponentDialog", "Disk chopper"))
        self.label_2.setText(_translate("AddComponentDialog", "Geometry type: "))
        self.comboBox_2.setItemText(0, _translate("AddComponentDialog", "Mesh"))
        self.comboBox_2.setItemText(1, _translate("AddComponentDialog", "Cylinder"))
        self.comboBox_2.setItemText(2, _translate("AddComponentDialog", "None"))
        self.comboBox_3.setItemText(0, _translate("AddComponentDialog", "Single ID"))
        self.comboBox_3.setItemText(1, _translate("AddComponentDialog", "Repeatable Grid"))
        self.comboBox_3.setItemText(2, _translate("AddComponentDialog", "Face Mapped Mesh"))
        self.comboBox_3.setItemText(3, _translate("AddComponentDialog", "None"))
        self.label_3.setText(_translate("AddComponentDialog", "Pixel Type: "))
        self.label.setText(_translate("AddComponentDialog", "Component Type: "))



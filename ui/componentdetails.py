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
        ComponentDetailsDialog.resize(965, 835)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComponentDetailsDialog.sizePolicy().hasHeightForWidth())
        ComponentDetailsDialog.setSizePolicy(sizePolicy)
        self.formLayoutWidget = QtWidgets.QWidget(ComponentDetailsDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 970, 821))
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
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.listView = QtWidgets.QListView(self.formLayoutWidget)
        self.listView.setObjectName("listView")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.listView)
        self.geometryfilelabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.geometryfilelabel.setEnabled(True)
        self.geometryfilelabel.setObjectName("geometryfilelabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.geometryfilelabel)
        self.geometryfileform = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.geometryfileform.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geometryfileform.sizePolicy().hasHeightForWidth())
        self.geometryfileform.setSizePolicy(sizePolicy)
        self.geometryfileform.setMinimumSize(QtCore.QSize(800, 0))
        self.geometryfileform.setObjectName("geometryfileform")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.geometryfileform)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.geometryfilebrowse = QtWidgets.QPushButton(self.formLayoutWidget)
        self.geometryfilebrowse.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geometryfilebrowse.sizePolicy().hasHeightForWidth())
        self.geometryfilebrowse.setSizePolicy(sizePolicy)
        self.geometryfilebrowse.setMaximumSize(QtCore.QSize(300, 200))
        self.geometryfilebrowse.setObjectName("geometryfilebrowse")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.geometryfilebrowse)

        self.retranslateUi(ComponentDetailsDialog)
        self.buttonBox.accepted.connect(ComponentDetailsDialog.accept)
        self.buttonBox.rejected.connect(ComponentDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ComponentDetailsDialog)

    def retranslateUi(self, ComponentDetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        ComponentDetailsDialog.setWindowTitle(_translate("ComponentDetailsDialog", "Component details"))
        self.label.setText(_translate("ComponentDetailsDialog", "Name: "))
        self.label_2.setText(_translate("ComponentDetailsDialog", "Description: "))
        self.label_3.setText(_translate("ComponentDetailsDialog", "Transforms:"))
        self.geometryfilelabel.setText(_translate("ComponentDetailsDialog", "Geometry file:"))
        self.geometryfilebrowse.setText(_translate("ComponentDetailsDialog", "Browse"))



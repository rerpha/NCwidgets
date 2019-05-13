# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.addcomponentwindow import Ui_AddComponentDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 4, 1, 1)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout.addWidget(self.openGLWidget, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuJSON = QtWidgets.QMenu(self.menubar)
        self.menuJSON.setObjectName("menuJSON")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow_Filewriter_JSON = QtWidgets.QAction(MainWindow)
        self.actionShow_Filewriter_JSON.setObjectName("actionShow_Filewriter_JSON")
        self.actionHide_JSON_Pane = QtWidgets.QAction(MainWindow)
        self.actionHide_JSON_Pane.setObjectName("actionHide_JSON_Pane")
        self.actionOpen_NeXus_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_NeXus_file.setObjectName("actionOpen_NeXus_file")
        self.actionExport_to_NeXus_file = QtWidgets.QAction(MainWindow)
        self.actionExport_to_NeXus_file.setObjectName("actionExport_to_NeXus_file")
        self.actionExport_to_Filewriter_JSON = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Filewriter_JSON.setObjectName(
            "actionExport_to_Filewriter_JSON"
        )
        self.menuFile.addAction(self.actionOpen_NeXus_file)
        self.menuFile.addAction(self.actionExport_to_NeXus_file)
        self.menuFile.addAction(self.actionExport_to_Filewriter_JSON)
        self.menuJSON.addAction(self.actionShow_Filewriter_JSON)
        self.menuJSON.addAction(self.actionHide_JSON_Pane)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuJSON.menuAction())

        self.retranslateUi(MainWindow)

        self.addWindow = QtWidgets.QDialog()
        self.addWindow.ui = Ui_AddComponentDialog()
        self.addWindow.ui.setupUi(self.addWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_add_component_window(self):
        self.addWindow.exec_()
        self.addWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NeXus file structure"))
        self.pushButton.setText(_translate("MainWindow", "Add component"))
        self.pushButton.clicked.connect(self.show_add_component_window)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuJSON.setTitle(_translate("MainWindow", "JSON"))
        self.actionShow_Filewriter_JSON.setText(
            _translate("MainWindow", "Show Filewriter JSON")
        )
        self.actionHide_JSON_Pane.setText(_translate("MainWindow", "Hide JSON Pane"))
        self.actionOpen_NeXus_file.setText(_translate("MainWindow", "Open NeXus file"))
        self.actionExport_to_NeXus_file.setText(
            _translate("MainWindow", "Export to NeXus file")
        )
        self.actionExport_to_Filewriter_JSON.setText(
            _translate("MainWindow", "Export to Filewriter JSON")
        )

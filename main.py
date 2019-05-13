import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore
from ui.mainwindow import Ui_MainWindow
from ui.addcomponentwindow import Ui_AddComponentDialog


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.addWindow = QDialog()
        self.addWindow.ui = AddComponentDialog()
        self.addWindow.ui.setupUi(self.addWindow)

    def show_add_component_window(self):
        self.addWindow.show()


class AddComponentDialog(Ui_AddComponentDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, AddComponentDialog):
        super().setupUi(AddComponentDialog)


if __name__ == "__main__":
    app = QApplication([])
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

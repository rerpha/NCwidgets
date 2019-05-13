import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore
from ui.mainwindow import Ui_MainWindow
from ui.addcomponentwindow import Ui_AddComponentDialog


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.addWindow = QDialog()
        self.addWindow.ui = AddComponentDialog()
        self.addWindow.ui.setupUi(self.addWindow)

    def show_add_component_window(self):
        self.addWindow.exec()


class AddComponentDialog(Ui_AddComponentDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, add_component_window):
        super().setupUi(add_component_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5 import QtCore
from ui.mainwindow import Ui_MainWindow
from ui.addcomponentwindow import Ui_AddComponentDialog

NEXUS_FILE_TYPES = "NeXus Files (*.nxs,*.nex,*.nx5)"


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    file_dialog_native = QFileDialog.DontUseNativeDialog

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.addWindow = QDialog()
        self.addWindow.ui = AddComponentDialog()
        self.addWindow.ui.setupUi(self.addWindow)

        self.actionExport_to_NeXus_file.triggered.connect(self.save_to_nexus_file)
        self.actionOpen_NeXus_file.triggered.connect(self.open_nexus_file)

    def save_to_nexus_file(self):
        options = QFileDialog.Options()
        options |= self.file_dialog_native
        fileName, _ = QFileDialog.getSaveFileName(
            parent=None,
            caption="QFileDialog.getSaveFileName()",
            directory="",
            filter=f"{NEXUS_FILE_TYPES};;All Files (*)",
            options=options,
        )
        if fileName:
            print(fileName)

    def open_nexus_file(self):
        options = QFileDialog.Options()

        options |= self.file_dialog_native
        fileName, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="QFileDialog.getOpenFileName()",
            directory="",
            filter=f"{NEXUS_FILE_TYPES};;All Files (*)",
            options=options,
        )
        if fileName:
            print(fileName)

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

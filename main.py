import sys

from PyQt5.QtGui import QVector3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QWidget
from PyQt5 import QtCore
from ui.mainwindow import Ui_MainWindow
from ui.addcomponentwindow import Ui_AddComponentDialog
import h5py
from uuid import uuid4
from PyQt5.Qt3DExtras import Qt3DWindow, QFirstPersonCameraController
from PyQt5.Qt3DCore import QEntity

NEXUS_FILE_TYPES = "NeXus Files (*.nxs,*.nex,*.nx5)"


def set_up_in_memory_nexus_file():
    return h5py.File(str(uuid4()), mode="w", driver="core", backing_store=False)


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.nexus_file = set_up_in_memory_nexus_file()

    file_dialog_native = QFileDialog.DontUseNativeDialog

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.addWindow = QDialog()
        self.addWindow.ui = AddComponentDialog()
        self.addWindow.ui.setupUi(self.addWindow)

        self.widget.ui = GeometryView()

        self.pushButton.clicked.connect(self.show_add_component_window)
        self.actionExport_to_NeXus_file.triggered.connect(self.save_to_nexus_file)
        self.actionOpen_NeXus_file.triggered.connect(self.open_nexus_file)
        self.actionExport_to_Filewriter_JSON.triggered.connect(
            self.save_to_filewriter_json
        )
        self.actionHide_JSON_Pane.triggered.connect(self.hide_json_pane)
        self.actionShow_Filewriter_JSON.triggered.connect(self.show_json_pane)

    def hide_json_pane(self):
        self.listWidget.setVisible(False)

    def show_json_pane(self):
        self.listWidget.setVisible(True)

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
            file = h5py.File(fileName, mode="x")
            self.nexus_file.copy(source="/", dest=file)
            print("Saved to NeXus file")

    def save_to_filewriter_json(self):
        options = QFileDialog.Options()
        options |= self.file_dialog_native
        fileName, _ = QFileDialog.getSaveFileName(
            parent=None,
            caption="QFileDialog.getSaveFileName()",
            directory="",
            filter="JSON Files (*.json);;All Files (*)",
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
            self.nexus_file = h5py.File(
                fileName, mode="r", backing_store=False, driver="core"
            )
            print("NeXus file loaded")

    def show_add_component_window(self):
        self.addWindow.exec()


class GeometryView(QWidget):
    def __init__(self):
        super().__init__()
        self.view = Qt3DWindow()
        camera = self.view.camera()
        camera.setPosition(QVector3D(0, 0, 0))
        camera.setViewCenter(QVector3D(0.0, 0.0, 0.0))

        self.rootEntity = QEntity()
        self.camController = QFirstPersonCameraController(self.rootEntity)
        self.camController.setCamera(camera)
        self.view.setRootEntity(self.rootEntity)


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

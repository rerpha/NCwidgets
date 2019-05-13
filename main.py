import sys
import h5py
from PyQt5.QtGui import QVector3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QWidget
from PyQt5 import QtCore
from ui.mainwindow import Ui_MainWindow
from ui.componentdetails import Ui_ComponentDetailsDialog
from ui.addcomponentwindow import Ui_AddComponentDialog
from uuid import uuid4
from PyQt5.Qt3DExtras import Qt3DWindow, QFirstPersonCameraController
from PyQt5.Qt3DCore import QEntity
from component_names import component_names

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
        self.window = self.createWindowContainer(self.view)
        camera = self.view.camera()
        camera.setPosition(QVector3D(0, 0, 0))
        camera.setViewCenter(QVector3D(0.0, 0.0, 0.0))

        self.rootEntity = QEntity()
        self.camController = QFirstPersonCameraController(self.rootEntity)
        self.camController.setCamera(camera)
        self.view.setRootEntity(self.rootEntity)


class ComponentDetailsDialog(Ui_ComponentDetailsDialog):
    def __init__(self):
        super().__init__()
        self.component_name = False
        self.geometry_type = False
        self.pixel_type = False

    def setupUi(self, ComponentDetailsDialog):
        super().setupUi(ComponentDetailsDialog)

    def create_delegates(self, component_name, geometry_type, pixel_type):
        self.component_name = component_name
        self.geometry_type = geometry_type
        self.pixel_type = pixel_type


class AddComponentDialog(Ui_AddComponentDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, add_component_window):
        super().setupUi(add_component_window)
        self.buttonBox.accepted.connect(self.accepted)

        self.populate_components_box()
        self.details = QDialog()
        self.details.ui = ComponentDetailsDialog()
        self.details.ui.setupUi(self.details)

    def populate_components_box(self):
        index = 0
        for component in component_names.items():
            self.comboBox.insertItem(index, component[0])
            index += 1

    def accepted(self):
        print(f"Component selected is: {self.comboBox.currentText()}")
        print(f"Shape type selected is: {self.comboBox_2.currentText()}")
        print(f"Pixel data type selected is: {self.comboBox_3.currentText()}")
        # create the next window here and pass stuff in

        self.details.ui.create_delegates(
            self.comboBox.currentText(),
            self.comboBox_2.currentText(),
            self.comboBox_3.currentText(),
        )
        self.details.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())

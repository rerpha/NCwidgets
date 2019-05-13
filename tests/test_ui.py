from main import MainWindow, QMainWindow
from pytestqt import qtbot
from PyQt5 import QtCore


def test_main_window_title(qtbot):
    main = MainWindow()
    window = QMainWindow()
    main.setupUi(window)
    assert window.windowTitle() == "NeXus Constructor"


def test_add_component_window_title(qtbot):
    main = MainWindow()
    window = QMainWindow()
    main.setupUi(window)

    qtbot.add_widget(window)
    qtbot.add_widget(main.addWindow)

    qtbot.mouseClick(main.pushButton, QtCore.Qt.LeftButton)

    assert main.addWindow.isVisible()

    main.addWindow.close()

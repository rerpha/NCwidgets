from pytestqt import qtbot
from main import MainWindow, QMainWindow


def test_main_window_title(qtbot):
    main = MainWindow()
    window = QMainWindow()
    main.setupUi(window)
    assert window.windowTitle() == "NeXus Constructor"

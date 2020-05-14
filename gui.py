import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setMinimumSize(1280, 720)
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Fenêtre')
        self.show()



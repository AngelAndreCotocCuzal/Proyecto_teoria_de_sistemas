from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QFrame
from PyQt5 import uic


class Main_principal(QMainWindow):
    def __init__(self) -> None:

        super(Main_principal, self).__init__()
        print("Hola funciono")
#        Load Ui
        uic.loadUi('views_principal/principal.ui', self)

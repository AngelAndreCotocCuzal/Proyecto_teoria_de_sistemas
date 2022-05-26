import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from datos_de_login import Main_principal
from segunda import Ui_segunda, d
from .principal import Ui_Principal
from PyQt5 import uic
from Views import MainView_principal


class MainView_login(QMainWindow):
    def __init__(self) -> None:
        super(MainView_login, self).__init__()

        # Load Ui
        uic.loadUi('Views/login_ventana.ui', self)

        self.Login_button.clicked.connect(self.abrir)
        self.Create_Account_Button.clicked.connect(self.crear)
        # self.ventana_principal = MainView_principal()


    def abrir(self):
        if self.email.text() == d.search_correo(self.email.text()) and self.contrasenia.text() == \
                d.search_contra(self.contrasenia.text()):
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Principal()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            # self.ventana.show()
        else:
            print("No coincide")
            print(self.email.text())
            print(d.search_correo(self.email.text()))

    def crear(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

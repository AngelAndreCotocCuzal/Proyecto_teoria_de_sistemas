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
from Views.nueva_ventana_principal import Ventana_principal
from imagenes import imagenes


class MainView_login(QMainWindow):
    def __init__(self) -> None:
        super(MainView_login, self).__init__()

        # Load Ui
        self.transaparente = uic.loadUi('Views/nuevo_login.ui', self)


        self.btn_login.clicked.connect(self.abrir)
        self.btn_crear.clicked.connect(self.crear)
        self.ventana_principal = Ventana_principal()
        self.transaparente.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.transaparente.setAttribute(QtCore.Qt.WA_TranslucentBackground)


    def abrir(self):
        if self.email.text() == d.search_correo(self.email.text()) and self.contrasenia.text() == \
                d.search_contra(self.contrasenia.text()):
            # self.ventana = QtWidgets.QMainWindow()
            # self.ui = Ui_Principal()
            # self.ui.setupUi(self.ventana)
            # self.ventana.show()
            self.ventana_principal.show()
            self.hide()
        else:
            print("No coincide")
            print(self.email.text())
            print(d.search_correo(self.email.text()))

    def crear(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

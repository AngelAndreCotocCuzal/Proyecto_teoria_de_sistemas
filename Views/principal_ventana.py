import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from controladores.PrincipalController import PrincipalController
from Views.crear_producto import Ui_CreateProduct
from PyQt5 import QtCore, QtGui, QtWidgets


class MainView_principal(QMainWindow):
    def __init__(self) -> None:
        super(MainView_principal, self).__init__()

        # Load Ui
        self.principal_controller = PrincipalController(self)

        uic.loadUi('Views/principal.ui', self)

        self.l = self.btn_list.clicked.connect(lambda: self.principal_controller.listar_productos())
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.eliminar_producto())



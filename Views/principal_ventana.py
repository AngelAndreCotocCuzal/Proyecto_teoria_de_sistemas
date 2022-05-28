import sys
import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from controladores.PrincipalController import PrincipalController
from Views.crear_producto import Ui_CreateProduct
from PyQt5 import QtCore, QtGui, QtWidgets
from segunda import Ui_segunda, d

myDir = os.getcwd()


sys.path.append(myDir)


class MainView_principal(QMainWindow):
    def __init__(self) -> None:
        super(MainView_principal, self).__init__()
        self.puesto = Ui_segunda()

        uic.loadUi('Views/principal.ui', self)

        # Load Ui
        self.principal_controller = PrincipalController(self)

        self.l = self.btn_list.clicked.connect(lambda: self.principal_controller.listar_productos())
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.eliminar_producto())
        self.btn_guardar_compra.clicked.connect(self.compras_inicio)

    def deshabilitar(self):
        if self.puesto == 'Gerente':
            self.btn_read.setEnabled(False)

        elif self.puesto == 'Empleado':
            self.btn_read.setEnabled(False)

        else:
            pass

    def ventas_inicio(self):
        pass

    def compras_inicio(self):
        pass

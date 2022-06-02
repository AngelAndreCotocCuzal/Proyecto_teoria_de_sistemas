import sys
import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from controladores.PrincipalController import PrincipalController
from Views.crear_producto import Ui_CreateProduct
from Views.crear_ventana import Ventana_crear
from PyQt5 import QtCore, QtGui, QtWidgets
from segunda import Ui_segunda, d
import pandas as pd
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
        self.c = self.btn_create.clicked.connect(lambda: self.principal_controller.openCreate(Ventana_crear()))

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

        df = pd.read_csv('inver.csv')
        codigo = self.text_codigo_compra.text()
        descripcion = self.text_descripcion_compra.text()
        media = self.text_media_compra.text()
        existencia = self.text_existencia_compra.text()
        precio_costo = self.text_precio_costo_compra.text()
        precio_publico = self.text_precio_publico_compra.text()

        registro = [(codigo, descripcion, media, existencia, precio_costo, precio_publico)]

        df1 = pd.DataFrame(registro, columns=['Codigo', 'Descripcion', 'Cantidad', 'Existencias', 'Costo', 'Publico'])
        df = df.append(df1, ignore_index=True)
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('inver.csv')
        self.tabla.setColumnCount(len(df.columns))
        self.tabla.setRowCount(len(df))
        self.tabla.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tabla.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))

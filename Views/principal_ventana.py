import sys
import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

import controladores.CreateProductController
from controladores.PrincipalController import PrincipalController
from Views.crear_producto import Ui_CreateProduct
from PyQt5 import QtCore, QtGui, QtWidgets
from segunda import Ui_segunda, d
from controladores.CreateProductController import CreateProductController
import pandas as pd
from tkinter import *
myDir = os.getcwd()


sys.path.append(myDir)


class MainView_principal(QMainWindow):
    def __init__(self) -> None:
        super(MainView_principal, self).__init__()
        self.puesto = Ui_segunda()

        uic.loadUi('Views/principal.ui', self)

        # Load Ui
        self.principal_controller = PrincipalController(self)
        self.create_product = CreateProductController(self)

        self.l = self.btn_list.clicked.connect(lambda: self.principal_controller.listar_productos())
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.u = self.btn_update.clicked.connect(lambda: self.principal_controller.updateProducs())
        # Guardar informacion
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.eliminar_producto())
        self.btn_guardar_compra.clicked.connect(self.compras_inicio)
        self.btn_guardar_venta.clicked.connect(self.ventas_inicio)
        # self.btn_contratar.clicked.connect(self.contrataciones)
        self.btn_cal.clicked.connect(self.total)
        self.ingreso_planilla.clicked.connect(self.ver_planilla)
        # eliminar datos
        self.btn_eliminar_compra.clicked.connect(self.elimina_compras)
        self.btn_eliminar_venta.clicked.connect(self.elimina_ventas)
        self.btn_eliminar_empleo.clicked.connect(self.elimina_empleado)
        self.btn_eliminar_planilla.clicked.connect(self.eliminar_planilla)
        # ver sobre consummo
        self.btn_cotizar_ventas.clicked.connect(self.ver_datos)
        # recursos humanos
        self.btn_contratar.clicked.connect(self.contrataciones)
        self.ingreso_planilla_2.clicked.connect(self.guardar_planilla)
        # self.btn_op.clicked.connect(self.opc)
        # self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        # self.calendarDateChanged()
        self.btn_create.clicked.connect(lambda: self.create_product.createProduct("licuado", "licuado de banano",
                                                                                  "2lt", "2","7", "8"))

        # botones de finanzas
        self.btn_anadir_gastos.clicked.connect(self.anadir)

    def deshabilitar(self):
        if self.puesto == 'Gerente':
            self.btn_read.setEnabled(False)

        elif self.puesto == 'Empleado':
            self.btn_read.setEnabled(False)

        else:
            pass

    def ver_datos(self):
        # https://www.youtube.com/watch?v=HDjc3w1W9oA
        codigo_ver = self.text_codigo_venta.text()
        # codigo_ver = int(self.text_codigo_venta.text())
        df = pd.read_csv('inver.csv')
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('inver.csv')
        # para monstrar el codigo de solo codigo
        # problemas con el str
        # var = df.loc[[3], ['Codigo', 'Costo', 'Existencia', 'Publico']]
        # var = df.loc[[codigo_ver], ['Codigo', 'Costo', 'Existencias', 'Publico']]
        var = df[(df['Codigo'] == codigo_ver)]
        # df2 = df.copy()
        # var = df2['Codigo'] = ['ACA0009']
        self.tabla_ventas_2.setColumnCount(len(var.columns))
        self.tabla_ventas_2.setRowCount(len(var))
        self.tabla_ventas_2.setHorizontalHeaderLabels(var.columns)
        for i in range(len(var)):
            for j in range(len(var.columns)):
                self.tabla_ventas_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(var.iat[i, j])))

        # df.loc[1111:11111, ['codigo']]

    def ventas_inicio(self):
        df = pd.read_csv('factura.csv')
        nombre = self.text_nombre_venta.text()
        codigo = self.text_codigo_venta.text()
        nit = self.text_nit_venta.text()
        mayoreo = self.cb_ma.currentText()
        monto = self.text_monto_venta.text()
        cantidad = self.text_cantidad_venta.text()
        dinero = int(self.text_dinero_venta.text())
        fecha = self.text_fecha_venta.text()
        a = int(self.text_monto_venta.text())
        b = int(self.text_cantidad_venta.text())
        sub_total = a * b
        total = dinero - sub_total

        registro_2 = [(nombre, codigo, nit, mayoreo, monto, cantidad, fecha, sub_total, total)]

        df1 = pd.DataFrame(registro_2, columns=['Nombre', 'Codigo', 'NIT', 'Consumo', 'Monto', 'Cantidad', 'Fecha',
                                                'Sub_total', 'Vuelto'])
        df = df.append(df1, ignore_index=True)
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('factura.csv')
        self.tabla_ventas.setColumnCount(len(df.columns))
        self.tabla_ventas.setRowCount(len(df))
        self.tabla_ventas.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tabla_ventas.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        QMessageBox.about(self, 'Aviso', 'Vendido')

    def total(self):
        root = Tk()
        a = int(self.text_monto_venta.text())
        b = int(self.text_cantidad_venta.text())
        sub_total = a * b
        Label(root, text='Total a pagar: ').pack()
        Label(root, text=sub_total).pack()

        root.mainloop()

    def compras_inicio(self):
        df = pd.read_csv('inver.csv')

        codigo = self.text_codigo_compra.text()
        descripcion = self.text_descripcion_compra.text()
        media = self.text_media_compra.text()
        # x = int(self.text_existencia_compra.text())
        # y = int(self.text_cantidad_venta.text())
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

    def contrataciones(self):
        df = pd.read_csv('empleo.csv')
        nombre_empleado = self.nombre_empleado.text()
        edad = int(self.edad.text())
        nacimiento = self.nacimiento.text()
        genero = self.genero.currentText()
        dpi = int(self.dpi.text())
        nit_empleado = self.nit_empleado.text()
        direccion = self.direccion.text()
        telefono = int(self.cel_empleado.text())
        sangre = self.sangre.text()
        alergico = self.alergico.text()
        puesto = self.puesto_2.text()
        sueldo = int(self.sueldo.text())
        emergencia = int(self.contacto.text())
        labor = self.inicio_laboral.text()

        registro_empleados = [(nombre_empleado, edad, nacimiento, genero, dpi, nit_empleado, direccion, telefono,
                               sangre,
                               alergico, puesto, sueldo, emergencia, labor)]

        df1 = pd.DataFrame(registro_empleados, columns=['Nombre_Empleado', 'Edad', 'Nacimiento', 'Genero', 'Dpi',
                                                        'Nit_Empleado',
                                                        'Direccion', 'Telefono', 'Sangre', 'Alergico', 'Puesto',
                                                        'Sueldo',
                                                        'Emergencia', 'Labor'])
        df = df.append(df1, ignore_index=True)
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('empleo.csv')
        self.tabla_contratacion.setColumnCount(len(df.columns))
        self.tabla_contratacion.setRowCount(len(df))
        self.tabla_contratacion.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tabla_contratacion.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        QMessageBox.about(self, 'Aviso', 'Contratado')

    def elimina_compras(self):
        df = pd.read_csv('inver.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('inver.csv')
        QMessageBox.about(self, 'Aviso', 'Eliminado')

    def elimina_ventas(self):
        df = pd.read_csv('factura.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('factura.csv')
        QMessageBox.about(self, 'Aviso', 'Eliminado')

    def eliminar_producto(self):
        table = self.principal.tabla
        if table.currentItem() is not None:
            cod = table.currentItem().text()
            product = self.product.getProduct(cod)
            if product:
                self.product.eliminar_producto(cod)
        self.listar_productos()
        QMessageBox.about(self, 'Aviso', 'Eliminado')

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        # self.updateTaskList

    def ver_planilla(self):
        df = pd.read_csv('empleo.csv')
        codigo_empleado = int(self.text_ver_empleado.text())
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('empleo.csv')
        var = df.loc[[codigo_empleado], ['Nombre_Empleado', 'Sueldo', 'Puesto']]
        self.tabla_planilla.setColumnCount(len(var.columns))
        self.tabla_planilla.setRowCount(len(var))
        self.tabla_planilla.setHorizontalHeaderLabels(var.columns)
        for i in range(len(var)):
            for j in range(len(var.columns)):
                self.tabla_planilla.setItem(i, j, QtWidgets.QTableWidgetItem(str(var.iat[i, j])))

    def elimina_empleado(self):
        df = pd.read_csv('empleo.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('empleo.csv')
        QMessageBox.about(self, 'Aviso', 'Eliminado')

    def guardar_planilla(self):
        df = pd.read_csv('planilla.csv')
        clave = int(self.text_clave.text())
        x = int(self.text_sueldo_planilla.text())
        iggs = 0.0483
        sueldo = x * iggs
        anticipo = int(self.text_anticipo_planilla.text())
        extras = int(self.text_extras.text())
        dinero = 60
        y = extras * dinero
        vacaciones = int(self.text_vacaciones.text())
        bonificaciones = self.cb_bonoficaciones.currentText()
        total = (((x-sueldo) - anticipo) + y)
        # 4.83

        guardar = [(clave, sueldo, anticipo, extras, vacaciones, bonificaciones, total)]
        df1 = pd.DataFrame(guardar, columns=['Clave', 'Sueldo_IGSS', 'Anticipo', 'Extras', 'Vacaciones', 'Bonificaciones', 'Total'])
        df = df.append(df1, ignore_index=True)
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('planilla.csv')
        self.tabla_planilla_2.setColumnCount(len(df.columns))
        self.tabla_planilla_2.setRowCount(len(df))
        self.tabla_planilla_2.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tabla_planilla_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        QMessageBox.about(self, 'Aviso', 'Guardado')

    def eliminar_planilla(self):
        df = pd.read_csv('planilla.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('planilla.csv')
        QMessageBox.about(self, 'Aviso', 'Eliminado')

    def anadir(self):
        try:
            if self.cv_gastos_financiero.currentText() == 'Remuneraciones':
                text = 300
                total = text - self.monto_gastos_financiero.Text()
                def onChanged(self, total):
                    self.btn_rh_cuetas_cobrar.setText(total)
                    self.btn_rh_cuetas_cobrar.adjustSize()
            elif self.cv_gastos_financiero.currentText() == 'Proveedores':
                pass
            elif self.cv_gastos_financiero.currentText() == 'Cuentas por Pagar':
                pass
            elif self.cv_gastos_financiero.currentText() == 'Prestamos Bancarios':
                pass
            elif self.cv_gastos_financiero.currentText() == 'Pagar Socio':
                pass
        except Exception as error:
            # QMessageBox.about(self, 'Aviso', 'Usuario creado')
            QMessageBox.about(self, 'Error', str(error))

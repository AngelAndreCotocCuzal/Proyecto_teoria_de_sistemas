import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from controladores.PrincipalController import PrincipalController
from controladores.CreateProductController import CreateProductController
from Modelos.Product import Product
import pandas as pd
from tkinter import *

myDir = os.getcwd()
sys.path.append(myDir)


class Ventana_principal(QMainWindow):
    def __init__(self) -> None:
        super(Ventana_principal, self).__init__()
        # Usamos ui para leer el archivo
        self.transaparente = uic.loadUi('Views/nueva_ventana_principal.ui', self)
        # declaramos una variable para quitar los bordes y tener una interfas mas limpia
        self.transaparente.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.transaparente.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.transaparente.setWindowOpacity(1)

        # conectando los botones de dereha e izquierda
        self.btn_menu_iz.clicked.connect(self.mover_menu)
        self.btn_menu_der.clicked.connect(self.mover_menu)

        # ocultar botones para una mejor interfas
        self.btn_restaurar.hide()
        self.btn_menu_iz.hide()
        self.btn_anadir_provedores.hide()  # para ocultar el boton
        self.btn_anadir_cuentas.hide()
        self.btn_anadir_prestamo.hide()
        self.btn_anadir_pagar_socio.hide()
        self.btn_anadir_caja.hide()
        self.btn_anadir_bancos.hide()

        # Creando sombras
        self.sombra_frame(self.stackedWidget)
        self.sombra_frame(self.frame_superior)
        self.sombra_frame(self.toolBox)
        self.sombra_frame(self.toolBox_2)
        self.sombra_frame(self.btn_inicio)
        self.sombra_frame(self.btn_inventario)
        self.sombra_frame(self.btn_ventas)
        self.sombra_frame(self.btn_rh)
        self.sombra_frame(self.btn_Financiero)

        # Creando las conecciones para la barra de titulo
        self.btn_minimizar.clicked.connect(self.control_bt_minimizar)
        self.btn_restaurar.clicked.connect(self.control_bt_normal)
        self.btn_maximizar.clicked.connect(self.control_bt_maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())

        # accion para redimezionar la applicacion
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # conectar ventana con los botones
        self.btn_inicio.clicked.connect(self.pagina_ini)
        self.btn_inventario.clicked.connect(self.pagina_inve)
        self.btn_ventas.clicked.connect(self.pagina_ven)
        self.btn_rh.clicked.connect(self.pagina_r_h)
        self.btn_Financiero.clicked.connect(self.pagina_fina)

        self.btn_menu_mover_lateral.clicked.connect(self.mover_lateral)

        # medtodo de inventario ----------------------------------------------------------------
        self.principal_controller = PrincipalController(self)
        self.create_product = CreateProductController(self)


        self.l = self.btn_list.clicked.connect(lambda: self.principal_controller.listar_productos())
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.u = self.btn_update.clicked.connect(lambda: self.principal_controller.updateProducs())
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.eliminar_producto())
        self.btn_create.clicked.connect(lambda: self.create_product.createProduct(self.input_cod.text(),
                                                                                  self.input_name.text(),
                                                                                  self.input_media.text(),
                                                                                  self.input_existencia.text(),
                                                                                  self.input_precio_costo.text(),
                                                                                  self.input_precio_publico.text()))
        # Boton contratar
        # Botones de contratacion
        self.btn_contratar.clicked.connect(self.contratar_contratacion)
        self.btn_eliminar_empleo.clicked.connect(self.elimina_empleado)
        # Botones de planilla
        self.ingreso_planilla.clicked.connect(self.ver_planilla)
        self.ingreso_planilla_2.clicked.connect(self.ventana_planilla)
        self.btn_eliminar_planilla.clicked.connect(self.eliminar_planilla)

        # botones de Venta
        self.btn_guardar_venta.clicked.connect(self.ventana_ventas)
        self.btn_cotizar_ventas.clicked.connect(self.ver_datos)
        self.btn_cal.clicked.connect(self.total)
        self.btn_actualizar_ventas.clicked.connect(self.actualizar_ventas)

        # botones de Compras
        self.btn_guardar_compra.clicked.connect(self.reabastecimiento)
        self.btn_actualizar_compras.clicked.connect(self.actualizar_compras)
        self.btn_eliminar_compra.clicked.connect(self.elimina_compras)



        # mostrar financiero
        # self.monto_gastos_financiero.textChanged.connect(self.onChanged)
        # caja_finanzas
        self.btn_actualizar_gastos.clicked.connect(self.anadir_gastos)
        self.btn_actualizar_ingresos.clicked.connect(self.anadir_ingresos)
        self.total_activos_corrientes()
        self.total_activos_no_corrientes()
        self.pasivo_corriente()
        self.pasivo_no_corriente()
        self.total_activo()
        self.total_pasivos()
        self.patrimonio()

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.btn_restaurar.show()
        self.btn_maximizar.hide()

    # Metodo para mover el menu
    def mover_menu(self):
        if True:
            width = self.menu_mover.width()
            normal = 0
            if width == 0:
                extender = 350
                self.btn_menu_der.hide()
                self.btn_menu_iz.show()

            else:
                self.btn_menu_der.show()
                self.btn_menu_iz.hide()
                extender = normal

            self.animacion = QPropertyAnimation(self.menu_mover, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(500)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()

    # Creando sombras
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def mover_lateral(self):
        self.animacion_paginas()

    # Creando las conecciones
    def pagina_ini(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inicio)
        self.stackedWidget_2.setCurrentWidget(self.pagina_inicio)

    def pagina_inve(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inventario)
        self.stackedWidget_2.setCurrentWidget(self.pagina_inventario)

    def pagina_ven(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_ventas)
        self.stackedWidget_2.setCurrentWidget(self.pagina_ventas)

    def pagina_r_h(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_rh)
        self.stackedWidget_2.setCurrentWidget(self.pagina_rh)

    def pagina_fina(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_financiero)
        self.stackedWidget_2.setCurrentWidget(self.pagina_financiero)

    def contratar_contratacion(self):
        self.stackedWidget_3.setCurrentWidget(self.tabla_contratacion_conectar)
        self.contrataciones()

    def ventana_planilla(self):
        self.stackedWidget_3.setCurrentWidget(self.tabla_planilla_conectar)
        self.guardar_planilla()

    def ventana_ventas(self):
        self.stackedWidget_4.setCurrentWidget(self.conectar_tabla_ventas)
        cod = self.text_codigo_producto.text()
        cantidad = int(self.text_cantidad_venta.text())
        self.principal_controller.modificar_existencias(cod, cantidad)
        self.ingresos_inventario()
        self.ventas_inicio()

    def reabastecimiento(self):
        cod = self.text_codigo_compra.text()
        cantidad = int(self.text_existencias_nuevas.text())
        self.principal_controller.reabastecer_existencias(cod, cantidad)
        QMessageBox.about(self, 'Aviso', 'Comprado')

    def actualizar_compras(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inventario)
        self.principal_controller.updateProducs()


    def actualizar_ventas(self):
        self.stackedWidget_4.setCurrentWidget(self.conectar_tabla_ventas)
        self.principal_controller.listar_productos()

    def ventana_compra(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inventario)
        self.compras_inicio()
        self.rebastecimiento()

    def animacion_paginas(self):
        if True:
            width = self.frame_lateral.width()
            x1 = self.frame_principa_pagina.rect().right()
            normal = 50
            if width == 50:
                extender = x1
            else:
                extender = normal

            self.animacion1 = QPropertyAnimation(self.frame_lateral, b"maximumWidth")
            self.animacion1.setStartValue(width)
            self.animacion1.setEndValue(extender)
            self.animacion1.setDuration(500)
            self.animacion1.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion1.start()

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
        codigo = self.text_codigo_producto.text()
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
        x = int(self.text_ver_empleado.text())
        codigo_empleado = x - 1
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
        horas = int(self.text_extras.text())
        dinero = 60
        y = horas * dinero
        vacaciones = int(self.text_vacaciones.text())
        #bonificaciones = self.cb_bonoficaciones.currentText()

        # 4.83
        extras = x / 30
        extras = extras * 7
        extras = extras / 48
        extras = extras * 1.5
        extras = extras * horas

        # extras = ((((sueldo / 30) * 7) / 48) * 1.5)
        try:
            if self.cb_bonoficaciones.currentText() == 'Bono 14':
                bonificaciones = x * 1
                total = ((((x - sueldo) - anticipo) + y) + bonificaciones)

            elif self.cb_bonoficaciones.currentText() == 'Aguinaldo':
                bonificaciones = x * 1
                total = ((((x - sueldo) - anticipo) + y) + bonificaciones)
            elif self.cb_bonoficaciones.currentText() == 'Ninguno':
                bonificaciones = 0
                total = ((((x - sueldo) - anticipo) + y) + bonificaciones)
        except Exception as error:
            # QMessageBox.about(self, 'Aviso', 'Usuario creado')
            QMessageBox.about(self, 'Error', str(error))


        guardar = [(clave, sueldo, anticipo, extras, vacaciones, bonificaciones, total)]
        df1 = pd.DataFrame(guardar,
                           columns=['Clave', 'Sueldo_IGSS', 'Anticipo', 'Extras', 'Vacaciones', 'Bonificaciones',
                                    'Total'])
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


    def guardar_financiero(self):
        df = pd.read_csv('gastos.csv')
        descripcion_financiero = self.text_descripcion_gasto.text()
        monto_financiero = self.monto_gastos_financiero.text()
        fecha_financiero = self.text_fecha_gastos.text()
        tipo_financiero = self.cv_gastos_financiero.currentText()

        registro_3 = [(descripcion_financiero, monto_financiero, fecha_financiero, tipo_financiero)]

        df1 = pd.DataFrame(registro_3, columns=['Descripcion', 'Monto', 'Fecha', 'Tipo'])
        df = df.append(df1, ignore_index=True)
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)
        df.to_csv('gastos.csv')
        QMessageBox.about(self, 'Aviso', 'Guardado Gasto')

    def anadir_gastos(self):
        try:
            if self.cv_gastos_financiero.currentText() == 'Remuneraciones':
                self.btn_anadir_gastos.show() # para mostrar el boton
                self.btn_anadir_provedores.hide() # para ocultar el boton
                self.btn_anadir_cuentas.hide()
                self.btn_anadir_prestamo.hide()
                self.btn_anadir_pagar_socio.hide()
                self.btn_anadir_gastos.clicked.connect(self.onChanged)

            elif self.cv_gastos_financiero.currentText() == 'Proveedores':
                # show es para mostrar
                # hide para ocultar
                self.btn_anadir_gastos.hide()
                self.btn_anadir_provedores.show()
                self.btn_anadir_cuentas.hide()
                self.btn_anadir_prestamo.hide()
                self.btn_anadir_pagar_socio.hide()
                self.btn_anadir_provedores.clicked.connect(self.onChanged_provedor)

            elif self.cv_gastos_financiero.currentText() == 'Cuentas por Pagar':
                self.btn_anadir_gastos.hide()  # para mostrar el boton
                self.btn_anadir_provedores.hide()  # para ocultar el boton
                self.btn_anadir_cuentas.show()
                self.btn_anadir_prestamo.hide()
                self.btn_anadir_pagar_socio.hide()
                self.btn_anadir_cuentas.clicked.connect(self.gastos_cuentas)

            elif self.cv_gastos_financiero.currentText() == 'Prestamos Bancarios':
                self.btn_anadir_gastos.hide() # para mostrar el boton
                self.btn_anadir_provedores.hide() # para ocultar el boton
                self.btn_anadir_cuentas.hide()
                self.btn_anadir_prestamo.show()
                self.btn_anadir_pagar_socio.hide()
                self.btn_anadir_prestamo.clicked.connect(self.gastos_prestamos)

            elif self.cv_gastos_financiero.currentText() == 'Pagar Socio':
                self.btn_anadir_gastos.hide() # para mostrar el boton
                self.btn_anadir_provedores.hide() # para ocultar el boton
                self.btn_anadir_cuentas.hide()
                self.btn_anadir_prestamo.hide()
                self.btn_anadir_pagar_socio.show()

        except Exception as error:
            # QMessageBox.about(self, 'Aviso', 'Usuario creado')
            QMessageBox.about(self, 'Error', str(error))

    # gastos
    # gastos corrientes
    def anadir_ingresos(self):
        try:
            if self.combox_ingresos.currentText() == 'Cuentas por cobrar':
                self.btn_anadir_cuentas_por_cobrar.show()
                self.btn_anadir_caja.hide()
                self.btn_anadir_bancos.hide()
                self.btn_anadir_cuentas_por_cobrar.clicked.connect(self.ingresos_cuentas)

            elif self.combox_ingresos.currentText() == 'Caja':
                self.btn_anadir_cuentas_por_cobrar.hide()
                self.btn_anadir_caja.show()
                self.btn_anadir_bancos.hide()
                self.btn_anadir_caja.clicked.connect(self.ingresos_caja)


            elif self.combox_ingresos.currentText() == 'Bancos':
                self.btn_anadir_cuentas_por_cobrar.hide()
                self.btn_anadir_caja.hide()
                self.btn_anadir_bancos.show()
                self.btn_anadir_bancos.clicked.connect(self.ingresos_banco)


        except Exception as error:
            # QMessageBox.about(self, 'Aviso', 'Usuario creado')
            QMessageBox.about(self, 'Error', str(error))

    def onChanged(self):
        anterior = int(self.btn_rh_pendeintes_pago.text())
        nuevo_dato = int(self.monto_gastos_financiero.text())

        if anterior > 0:
            # si en anterior existen datos
            mostrar = nuevo_dato + anterior
            self.btn_rh_pendeintes_pago.setText(str(mostrar))
            self.btn_rh_pendeintes_pago.adjustSize()

        elif anterior == 0:
            mostrar = nuevo_dato
            self.btn_rh_pendeintes_pago.setText(str(mostrar))
            self.btn_rh_pendeintes_pago.adjustSize()

        self.monto_gastos_financiero.clear()
        self.pasivo_corriente()

    def onChanged_provedor(self):
        anterior_provedor = int(self.btn_rh_proveedores.text())
        nuevo_dato_provedor = int(self.monto_gastos_financiero.text())

        if anterior_provedor > 0:
            # si en anterior existen datos
            mostrar_provedor = nuevo_dato_provedor + anterior_provedor
            self.btn_rh_proveedores.setText(str(mostrar_provedor))
            self.btn_rh_proveedores.adjustSize()

        elif anterior_provedor == 0:
            mostrar = nuevo_dato_provedor
            self.btn_rh_proveedores.setText(str(mostrar))
            self.btn_rh_proveedores.adjustSize()

        self.monto_gastos_financiero.clear()
        self.pasivo_corriente()

    def gastos_cuentas(self):
        anterior_provedor = int(self.btn_rh_cuentas_por_pagar.text())
        nuevo_dato_provedor = int(self.monto_gastos_financiero.text())

        if anterior_provedor > 0:
            # si en anterior existen datos
            mostrar_provedor = nuevo_dato_provedor + anterior_provedor
            self.btn_rh_cuentas_por_pagar.setText(str(mostrar_provedor))
            self.btn_rh_cuentas_por_pagar.adjustSize()

        elif anterior_provedor == 0:
            mostrar = nuevo_dato_provedor
            self.btn_rh_cuentas_por_pagar.setText(str(mostrar))
            self.btn_rh_cuentas_por_pagar.adjustSize()

        self.monto_gastos_financiero.clear()
        self.pasivo_corriente()

    def gastos_prestamos(self):
        anterior = int(self.btn_rh_prestamos_bancarios.text())
        nuevo_dato = int(self.monto_gastos_financiero.text())

        if anterior > 0:
            # si en anterior existen datos
            mostrar = nuevo_dato + anterior
            self.btn_rh_prestamos_bancarios.setText(str(mostrar))
            self.btn_rh_prestamos_bancarios.adjustSize()

        elif anterior == 0:
            mostrar = nuevo_dato
            self.btn_rh_prestamos_bancarios.setText(str(mostrar))
            self.btn_rh_prestamos_bancarios.adjustSize()

        self.monto_gastos_financiero.clear()
        self.pasivo_corriente()

    def pasivo_corriente(self):
        remuneraciones = int(self.btn_rh_pendeintes_pago.text())
        provedores = int(self.btn_rh_proveedores.text())
        cuentas = int(self.btn_rh_cuentas_por_pagar.text())
        prestamos = int(self.btn_rh_prestamos_bancarios.text())

        suma = remuneraciones + provedores + cuentas + prestamos
        self.btn_rh_pasivos_corrientes.setText(str(suma))
        self.btn_rh_pasivos_corrientes.adjustSize()
        return suma

    # gastos no corrientes

    def pasivo_no_corriente(self):
        pagar_socios = int(self.btn_rh_pagar_socios.text())

        suma = pagar_socios

        self.btn_rh_pasivos_no_corrientes.setText(str(suma))
        self.btn_rh_pasivos_no_corrientes.adjustSize()
        return suma



    # ingresos
    # ingresos corrientes
    def ingresos_cuentas(self):
        anterior = int(self.btn_rh_cuetas_cobrar.text())
        nuevo_dato = int(self.text_monto_ingresos.text())

        if anterior > 0:
            # si en anterior existen datos
            mostrar = nuevo_dato + anterior
            self.btn_rh_cuetas_cobrar.setText(str(mostrar))
            self.btn_rh_cuetas_cobrar.adjustSize()

        elif anterior == 0:
            mostrar = nuevo_dato
            self.btn_rh_cuetas_cobrar.setText(str(mostrar))
            self.btn_rh_cuetas_cobrar.adjustSize()

        self.text_monto_ingresos.clear()
        self.total_activos_corrientes()

    def ingresos_inventario(self):
        print("ejecutando")
        anterior = int(self.btn_rh_inentarios.text())
        precio = int(self.text_monto_venta.text())
        cantidad = int(self.text_cantidad_venta.text())

        resultado = precio * cantidad
        resultado = resultado + anterior
        print(f"resulrado con descuento mayoreo: {resultado}")
        self.btn_rh_inentarios.setText(str(resultado))
        self.btn_rh_inentarios.adjustSize()
        self.total_activos_corrientes()

    def ingresos_caja(self):
        anterior = int(self.btn_rh_caja.text())
        nuevo_dato = int(self.text_monto_ingresos.text())

        if anterior > 0:
            # si en anterior existen datos
            mostrar = nuevo_dato + anterior
            self.btn_rh_caja.setText(str(mostrar))
            self.btn_rh_caja.adjustSize()

        elif anterior == 0:
            mostrar = nuevo_dato
            self.btn_rh_caja.setText(str(mostrar))
            self.btn_rh_caja.adjustSize()

        self.text_monto_ingresos.clear()
        self.total_activos_corrientes()

    def ingresos_banco(self):
        anterior = int(self.btn_rh_bancos.text())
        nuevo_dato = int(self.text_monto_ingresos.text())

        if anterior > 0:
            # si en anterior existen datos
            mostrar = nuevo_dato + anterior
            self.btn_rh_bancos.setText(str(mostrar))
            self.btn_rh_bancos.adjustSize()

        elif anterior == 0:
            mostrar = nuevo_dato
            self.btn_rh_bancos.setText(str(mostrar))
            self.btn_rh_bancos.adjustSize()

        self.text_monto_ingresos.clear()
        self.total_activos_corrientes()

    def total_activos_corrientes(self):
        cuentas_cobrar = int(self.btn_rh_cuetas_cobrar.text())
        inventario = int(self.btn_rh_inentarios.text())
        caja = int(self.btn_rh_caja.text())
        bancos = int(self.btn_rh_bancos.text())

        suma = cuentas_cobrar + inventario + caja + bancos

        self.btn_rh_activos_corriete.setText(str(suma))
        self.btn_rh_activos_corriete.adjustSize()
        self.total_activo()
        return suma

    # ingresos no corrientes

    def total_activos_no_corrientes(self):
        vehiculo = int(self.btn_rh_vehiculos.text())
        computo = int(self.btn_rh_computo.text())

        suma = vehiculo + computo

        self.btn_rh_activos_no_corriente.setText(str(suma))
        self.btn_rh_activos_no_corriente.adjustSize()
        self.total_activo()
        return suma
    #
    def total_activo(self):
        a_corriente = int(self.btn_rh_activos_corriete.text())
        a_no_corriente = int(self.btn_rh_activos_no_corriente.text())

        total = a_corriente + a_no_corriente

        self.btn_rh_total_activos.setText(str(total))
        self.btn_rh_total_activos.adjustSize()
        self.patrimonio()

    def total_pasivos(self):
        p_corriente = self.pasivo_corriente()
        p_no_corriente = self.pasivo_no_corriente()

        total = p_corriente + p_no_corriente

        self.btn_rh_total_pasivos.setText(str(total))
        self.btn_rh_total_pasivos.adjustSize()
        self.patrimonio()

    def patrimonio(self):
        a = int(self.btn_rh_total_activos.text())
        p = int(self.btn_rh_total_pasivos.text())

        total = a + p
        self.btn_rh_total_patrimonio.setText(str(total))
        self.btn_rh_total_patrimonio.adjustSize()





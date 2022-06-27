import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Base_de_datos.Connection import connection
from Modelos.Product import Product


class PrincipalController():

    def __init__(self, principal):
        self.product = Product(connection())
        self.principal = principal

    def modificar_existencias(self, codigo, modificar: int):
        product = self.product.getProduct(codigo)
        producto_acutal: int = product[3]

        nuevo_producto: int = producto_acutal - modificar
        self.product.modificar_inventario(codigo, nuevo_producto)


    def listar_productos(self):
        table = self.principal.table_product
        productos = self.product.obtener_producto()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # def showProduct(self):
    #    table = self.principal.table_product
    #    if table.currentItem() != None:
    #        cod = table.currentItem().text()
    #        print(cod)

    def showProduct(self):
        table = self.principal.table_product
        if table.currentItem() != None:
            cod = table.currentItem().text()
            print(cod)
            product = self.product.getProduct(cod)
            if product:
                print(product)
                msg = QMessageBox()
                msg.setWindowTitle(product[1])
                msg.setText(product[1])

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText(f"Codigo: {product[0]} \nDescripcion: {product[1]} \nMedia: {product[2]}"
                                       f" \nExistencia {product[3]} \nPrecio(cosoto) {product[4]}"
                                       f" \nPrecio(publico) {product[5]}")

                x = msg.exec_()

    def updateProducs(self):
        table = self.principal.table_product
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number, column_number) != None:
                    fila.append(table.item(row_number, column_number).text())
            if len(fila) > 0:
                products.append(fila)
            fila = []

        self.listar_productos()

    def eliminar_producto(self):
        table = self.principal.table_product
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.product.getProduct(cod)
            if product:
                self.product.eliminar_producto(cod)
        self.listar_productos()

    def openCreate(self, Ui_CreateProduct):
        self.ventana = Ui_CreateProduct
        self.ventana.show()




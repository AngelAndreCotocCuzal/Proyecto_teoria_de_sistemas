import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controladores.PrincipalController import PrincipalController
from Views.crear_producto import Ui_CreateProduct
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def __init__(self):
        self.principal_controller = PrincipalController(self)

    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(1096, 681)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.base_datos_ventana = QtWidgets.QTabWidget(self.centralwidget)
        self.base_datos_ventana.setGeometry(QtCore.QRect(0, 0, 1131, 631))
        self.base_datos_ventana.setObjectName("base_datos_ventana")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.table_product = QtWidgets.QTableWidget(self.tab_6)
        self.table_product.setGeometry(QtCore.QRect(50, 90, 801, 391))
        self.table_product.setStyleSheet("")
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(50, 20, 416, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_list = QtWidgets.QPushButton(self.tab_6)
        self.btn_list.setGeometry(QtCore.QRect(80, 500, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_list.setFont(font)
        self.btn_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_list.setObjectName("btn_list")
        self.btn_update = QtWidgets.QPushButton(self.tab_6)
        self.btn_update.setGeometry(QtCore.QRect(180, 500, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setObjectName("btn_update")
        self.btn_create = QtWidgets.QPushButton(self.tab_6)
        self.btn_create.setGeometry(QtCore.QRect(300, 500, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.btn_read = QtWidgets.QPushButton(self.tab_6)
        self.btn_read.setGeometry(QtCore.QRect(410, 500, 126, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_read.setFont(font)
        self.btn_read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read.setObjectName("btn_read")
        self.btn_delete = QtWidgets.QPushButton(self.tab_6)
        self.btn_delete.setGeometry(QtCore.QRect(540, 500, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(-10, -10, 1111, 821))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.532, y2:1, stop:0.174129 rgba(232, 173, 35), stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.table_product.raise_()
        self.label.raise_()
        self.btn_list.raise_()
        self.btn_update.raise_()
        self.btn_create.raise_()
        self.btn_read.raise_()
        self.btn_delete.raise_()
        self.base_datos_ventana.addTab(self.tab_6, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.base_datos_ventana.addTab(self.tab_8, "")
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        self.base_datos_ventana.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Principal)

        self.l = self.btn_list.clicked.connect(lambda: self.principal_controller.listar_productos())
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.eliminar_producto())

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "CODIGO"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "DESCRIBCION"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "CODMEDIDAINV"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "EXISTENCIA"))
        item = self.table_product.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "PRECIO(costo)"))
        item = self.table_product.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "PRECIO(publico)"))
        self.label.setText(_translate("Principal", "Ventana Principal"))
        self.btn_list.setText(_translate("Principal", "Listar"))
        self.btn_update.setText(_translate("Principal", "Actualizar"))
        self.btn_create.setText(_translate("Principal", "Crear"))
        self.btn_read.setText(_translate("Principal", "Seleccionar"))
        self.btn_delete.setText(_translate("Principal", "Eliminar"))
        self.base_datos_ventana.setTabText(self.base_datos_ventana.indexOf(self.tab_6), _translate("Principal", "Tab 1"))
        self.base_datos_ventana.setTabText(self.base_datos_ventana.indexOf(self.tab_8), _translate("Principal", "Tab 2"))



from PyQt5 import QtCore, QtGui, QtWidgets
from user import Asociado
from typing import TypeVar
from random import randint

T = TypeVar('T')
d: Asociado[T] = Asociado()
d.crear_cuenta('admin', 'admin123', 1234, 'Empleado',  'Angel Andre Cotoc Cuzal')


class Ui_segunda(object):
    def setupUi(self, segunda):
        segunda.setObjectName("segunda")
        segunda.resize(489, 665)
        self.centralwidget = QtWidgets.QWidget(segunda)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 491, 691))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, "
                                   "x1:0.512, y1:0, x2:0.532, y2:1, stop:0.174129 rgba(17, 37, 232, 255), "
                                   "stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.email_crear = QtWidgets.QLineEdit(self.centralwidget)
        self.email_crear.setGeometry(QtCore.QRect(70, 140, 341, 41))
        self.email_crear.setText("")
        self.email_crear.setAlignment(QtCore.Qt.AlignCenter)
        self.email_crear.setObjectName("email_crear")
        self.contrasenia_crear = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasenia_crear.setGeometry(QtCore.QRect(70, 210, 341, 41))
        self.contrasenia_crear.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia_crear.setAlignment(QtCore.Qt.AlignCenter)
        self.contrasenia_crear.setObjectName("contrasenia_crear")
        self.Nombre_crear = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre_crear.setGeometry(QtCore.QRect(70, 280, 341, 41))
        self.Nombre_crear.setText("")
        self.Nombre_crear.setAlignment(QtCore.Qt.AlignCenter)
        self.Nombre_crear.setObjectName("Nombre_crear")
        self.Puesto = QtWidgets.QComboBox(self.centralwidget)
        self.Puesto.setGeometry(QtCore.QRect(70, 340, 341, 41))
        self.Puesto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Puesto.setObjectName("Puesto")
        self.Puesto.addItem("")
        self.Puesto.addItem("")
        self.Puesto.addItem("")
        self.Codigo_Gerente = QtWidgets.QLineEdit(self.centralwidget)
        self.Codigo_Gerente.setGeometry(QtCore.QRect(70, 410, 341, 41))
        self.Codigo_Gerente.setText("")
        self.Codigo_Gerente.setAlignment(QtCore.Qt.AlignCenter)
        self.Codigo_Gerente.setObjectName("Codigo_Gerente")
        self.Create_Account_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Account_Button_2.setGeometry(QtCore.QRect(90, 480, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Create_Account_Button_2.setFont(font)
        self.Create_Account_Button_2.setStyleSheet("background-color: rgb(69, 87, 255);\n"
"color: rgb(255, 255, 255);")
        self.Create_Account_Button_2.setObjectName("Create_Account_Button_2")
        segunda.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(segunda)
        self.statusbar.setObjectName("statusbar")
        segunda.setStatusBar(self.statusbar)

        self.retranslateUi(segunda)
        QtCore.QMetaObject.connectSlotsByName(segunda)
        self.Create_Account_Button_2.clicked.connect(self.guardar)
        # self.Create_Account_Button_2.quit()

    def retranslateUi(self, segunda):
        _translate = QtCore.QCoreApplication.translate
        segunda.setWindowTitle(_translate("segunda", "MainWindow"))
        self.label.setText(_translate("segunda", "Crear Cuenta"))
        self.email_crear.setPlaceholderText(_translate("segunda", "Correo Electronico"))
        self.contrasenia_crear.setPlaceholderText(_translate("segunda", "Contraseña"))
        self.Nombre_crear.setPlaceholderText(_translate("segunda", "Nombre Completo"))
        self.Puesto.setItemText(0, _translate("segunda", "PUESTO"))
        self.Puesto.setItemText(1, _translate("segunda", "Gerente"))
        self.Puesto.setItemText(2, _translate("segunda", "Empleado"))
        self.Codigo_Gerente.setPlaceholderText(_translate("segunda", "Codigo Gerente (Si es Empleado Codigo: 1234)"))
        self.Create_Account_Button_2.setText(_translate("segunda", "Crear cuenta"))

    def guardar(self):
        self.correo = self.email_crear.text()
        self.contrasena = self.contrasenia_crear.text()
        self.nombre = self.Nombre_crear.text()
        self.puesto = self.Puesto.currentText()
        # self.codigo = self.Codigo_Gerente.text()
        self.codigo = randint(1000, 9999)
        self.codigo_gerente = self.Codigo_Gerente.text()

        if self.puesto == "Gerente" and self.codigo_gerente == "1202":
            d.crear_cuenta(self.correo, self.contrasena, self.codigo, self.puesto, self.nombre)
            print("Se ha guardado")
        elif self.puesto == "Empleado" and self.codigo_gerente == "1234":
            d.crear_cuenta(self.correo, self.contrasena, self.codigo, self.puesto, self.nombre)
            print("Se ha guardado")
        else:
            print("Ingrese un codigo correcto")

from PyQt5 import QtCore, QtGui, QtWidgets
from principal import Main_principal
from segunda import Ui_segunda, d

# d = Ui_segunda()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 491, 141))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(7, 52, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 30, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Login_button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_button.setGeometry(QtCore.QRect(100, 360, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Login_button.setFont(font)
        self.Login_button.setStyleSheet("background-color: rgb(69, 87, 255);\n"
"color: rgb(255, 255, 255);")
        self.Login_button.setObjectName("Login_button")
        self.Create_Account_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Account_Button.setGeometry(QtCore.QRect(100, 440, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Create_Account_Button.setFont(font)
        self.Create_Account_Button.setStyleSheet("background-color: rgb(69, 87, 255);\n"
"color: rgb(255, 255, 255);")
        self.Create_Account_Button.setObjectName("Create_Account_Button")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(80, 240, 341, 41))
        self.email.setText("")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.contrasenia = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasenia.setGeometry(QtCore.QRect(80, 290, 341, 41))
        self.contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia.setAlignment(QtCore.Qt.AlignCenter)
        self.contrasenia.setObjectName("contrasenia")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 620, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 491, 531))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.532,"
                                   " y2:1, stop:0.174129 rgba(17, 37, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 140, 491, 8))
        self.label_5.setStyleSheet("background-color: qconicalgradient(cx:0.426, cy:0.522727,"
                                   " angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.109453 rgba(166, 140, 41, 255),"
                                   " stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255),"
                                   " stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255),"
                                   " stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255),"
                                   " stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255),"
                                   " stop:0.950249 rgba(202, 174, 68, 255));")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.Alerta_Login = QtWidgets.QLabel(self.centralwidget)
        self.Alerta_Login.setGeometry(QtCore.QRect(60, 540, 361, 41))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Alerta_Login.setFont(font)
        self.Alerta_Login.setStyleSheet("color: rgb(255, 0, 4);")
        self.Alerta_Login.setText("")
        self.Alerta_Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Alerta_Login.setObjectName("Alerta_Login")
        self.label_4.raise_()
        self.groupBox.raise_()
        self.Login_button.raise_()
        self.Create_Account_Button.raise_()
        self.email.raise_()
        self.contrasenia.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Alerta_Login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # probar = self.email.text()
        # contra = self.contrasenia.text()

        self.Login_button.clicked.connect(self.abrir)
        self.Create_Account_Button.clicked.connect(self.crear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cooperativa"))
        self.label_2.setText(_translate("MainWindow", "Cochito Seguro"))
        self.Login_button.setText(_translate("MainWindow", "Entrar"))
        self.Create_Account_Button.setText(_translate("MainWindow", "Crear cuenta"))
        self.email.setPlaceholderText(_translate("MainWindow", "Correo Electronico"))
        self.contrasenia.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.label_3.setText(_translate("MainWindow", "Designed By: Angel Cotoc, Diego Abdo, Gerardo Ortiz"))

    def abrir(self):
        if self.email.text() == d.search_correo(self.email.text()) and self.contrasenia.text() == \
                d.search_contra(self.contrasenia.text()):
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Main_principal()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
        else:
            print("No coincide")
            print(self.email.text())
            print(d.search_correo(self.email.text()))

    def crear(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    # def probar(self):
    #    probar = self.email.text()
    #    contra = self.contrasenia.text()
    #    if d.correo == probar and d.contrasena == contra:
    #        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
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
        self.btn_menu_der.hide()

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

    # Creando las conecciones
    def pagina_ini(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inicio)
        self.stackedWidget_2.setCurrentWidget(self.pagina_inicio)
        self.animacion_paginas()

    def pagina_inve(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_inventario)
        self.stackedWidget_2.setCurrentWidget(self.pagina_inventario)
        self.animacion_paginas()

    def pagina_ven(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_ventas)
        self.stackedWidget_2.setCurrentWidget(self.pagina_ventas)
        self.animacion_paginas()

    def pagina_r_h(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_rh)
        self.stackedWidget_2.setCurrentWidget(self.pagina_rh)
        self.animacion_paginas()

    def pagina_fina(self):
        self.stackedWidget.setCurrentWidget(self.page_lateral_financiero)
        self.stackedWidget_2.setCurrentWidget(self.pagina_financiero)
        self.animacion_paginas()


    def animacion_paginas(self):
        if True:
            width = self.stackedWidget.width()
            x1 = self.frame_principa_pagina.rect().right()
            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = normal

            self.animacion1 = QPropertyAnimation(self.stackedWidget, b"maximumWidth")
            self.animacion1.setStartValue(width)
            self.animacion1.setEndValue(extender)
            self.animacion1.setDuration(500)
            self.animacion1.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion1.start()

import sys
import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from imagenes import imagenes


myDir = os.getcwd()
sys.path.append(myDir)


class Ventana_crear(QMainWindow):
    def __init__(self) -> None:
        super(Ventana_crear, self).__init__()

        uic.loadUi('Views/crear_producto.ui', self)

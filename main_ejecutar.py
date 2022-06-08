from PyQt5.QtWidgets import QApplication
from Views import MainView_login
from Views import Ventana_principal


import sys

app = QApplication(sys.argv)
window = MainView_login()
window.show()


sys.exit(app.exec_())

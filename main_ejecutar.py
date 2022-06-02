from PyQt5.QtWidgets import QApplication
from Views import MainView_principal
from Views import MainView_login



import sys

app = QApplication(sys.argv)
window = MainView_login()
window.show()


sys.exit(app.exec_())

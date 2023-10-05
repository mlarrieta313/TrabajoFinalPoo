import sys
#from Controlador.controlador_login import ControladorLogin
from Vista.vista_login import VistaLogin
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow (QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = VistaLogin()
        self.ui.setupUi(self)
        
        
        self.show()
        


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())


from ui_principal import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("principal")
        self.stack = self.MultiVentanas_Widget
        
        self.Nombres_Widget.setHidden(True)

        self.panel_nombre.clicked.connect(self.cambio_hacia_panel)
        self.Panel_icono.clicked.connect(self.cambio_hacia_panel)
        
        self.perfil_nombre.clicked.connect(self.cambio_hacia_perfil)
        self.Perfil_icono.clicked.connect(self.cambio_hacia_perfil)
        
        self.analizis_nombre.clicked.connect(self.cambio_hacia_analizis)
        self.Analizis_icono.clicked.connect(self.cambio_hacia_analizis)
        
        self.noticias_nombre.clicked.connect(self.cambio_hacia_noticias)
        self.Noticias_icono.clicked.connect(self.cambio_hacia_noticias)
        
        self.ajustes_nombre.clicked.connect(self.cambio_hacia_ajustes)
        self.Ajustes_icono.clicked.connect(self.cambio_hacia_ajustes)
        
    def cambio_hacia_panel(self):
        self.stack.setCurrentIndex(0) 
        
    def cambio_hacia_perfil(self):
        self.stack.setCurrentIndex(1) 
        
    def cambio_hacia_analizis(self):
        self.stack.setCurrentIndex(2) 
        
    def cambio_hacia_noticias(self):
        self.stack.setCurrentIndex(3) 
        
    def cambio_hacia_ajustes(self):
        self.stack.setCurrentIndex(4) 

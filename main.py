from PySide6.QtWidgets import QApplication
import sys
from principal import Principal

app = QApplication(sys.argv)

usuario = {
    "id_usuario": 1,
    "username": "admin",
    "nombre": "Administrador",
    "email": "admin@tesis.com",
}

principal_window = Principal(usuario)
principal_window.show()

app.exec()

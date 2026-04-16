from PySide6.QtWidgets import QApplication
import sys
from principal import Principal
from UI.theme.theme import get_theme_manager

app = QApplication(sys.argv)

# Inicializar y aplicar tema
theme_manager = get_theme_manager()
theme_manager.load_preference()
theme_manager.apply_theme()

usuario = {
    "id_usuario": 1,
    "username": "admin",
    "nombre": "Administrador",
    "email": "admin@tesis.com",
}

principal_window = Principal(usuario)
principal_window.show()

app.exec()

from PySide6.QtWidgets import QApplication
import sys
from principal import Principal

app = QApplication(sys.argv)

QSS = """
QMainWindow {
    background-color: #f5f5f5;
}
QPushButton {
    background-color: #e0e0e0;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 8px 16px;
}
QPushButton:hover {
    background-color: #d0d0d0;
}
QLineEdit {
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
}
QListWidget {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 5px;
}
QTableWidget {
    border: 1px solid #ccc;
    border-radius: 5px;
}
QLabel {
    color: #333;
}
"""
app.setStyleSheet(QSS)

usuario = {
    "id_usuario": 1,
    "username": "admin",
    "nombre": "Administrador",
    "email": "admin@tesis.com",
}

principal_window = Principal(usuario)
principal_window.show()

app.exec()

from UI.ui_login import Ui_LoginWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from database import Database
from principal import Principal
import hashlib


class Login(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Gestion de Tesis - Login")
        self.setFixedSize(400, 500)

        self.db = Database()
        self.principal_window = None

        self.login_button.clicked.connect(self.attempt_login)
        self.password_input.returnPressed.connect(self.attempt_login)

    def attempt_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            self.error_label.setText("Complete todos los campos")
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if self.db.connect():
            query = "SELECT * FROM usuarios WHERE username = %s AND password_hash = %s"
            result = self.db.fetch_one(query, (username, password_hash))

            if result:
                self.hide()
                if (
                    self.principal_window is None
                    or not self.principal_window.isVisible()
                ):
                    self.principal_window = Principal(result)
                    self.principal_window.closed.connect(self.on_principal_closed)
                    self.principal_window.show()
                self.db.disconnect()
            else:
                self.error_label.setText("Usuario o contrasena incorrectos")
                self.db.disconnect()
        else:
            self.error_label.setText("Error de conexion a la base de datos")

    def on_principal_closed(self):
        self.principal_window = None
        self.show()

    def closeEvent(self, event):
        if self.principal_window and self.principal_window.isVisible():
            self.principal_window.close()
        event.accept()
        QApplication.quit()

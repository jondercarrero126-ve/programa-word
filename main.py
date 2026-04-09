from PySide6.QtWidgets import QApplication
import sys
from login import Login

app = QApplication(sys.argv)

login_window = Login()
login_window.show()

app.exec()

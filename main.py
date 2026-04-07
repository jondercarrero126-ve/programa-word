from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from principal import Principal

app = QApplication(sys.argv)


window = Principal()


window.show()
app.exec()
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(400, 500)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(140, 40, 120, 120))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(50, 170, 300, 40))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: #333;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.username_input = QLineEdit(self.centralwidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(50, 230, 300, 45))
        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(50, 290, 300, 45))
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(50, 360, 300, 45))
        self.login_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(25, 120, 200);\n"
"}")
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(50, 420, 300, 30))
        self.error_label.setStyleSheet(u"color: red;")
        self.error_label.setAlignment(Qt.AlignCenter)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.login_button.clicked.connect(LoginWindow.attempt_login)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Gesti\u00f3n de Tesis - Login", None))
        self.logo_label.setText(QCoreApplication.translate("LoginWindow", u"\U0001f4da", None))
        self.title_label.setText(QCoreApplication.translate("LoginWindow", u"Gesti\u00f3n de Tesis", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Usuario", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.login_button.setText(QCoreApplication.translate("LoginWindow", u"Iniciar Sesi\u00f3n", None))
        self.error_label.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Icono_Widget = QWidget(self.centralwidget)
        self.Icono_Widget.setObjectName(u"Icono_Widget")
        self.Icono_Widget.setStyleSheet(u"QWidget{\n"
"     \n"
"	background-color: rgb(155, 155, 221);\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
"	color: white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"	\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.Icono_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Persona = QLabel(self.Icono_Widget)
        self.Persona.setObjectName(u"Persona")
        self.Persona.setMinimumSize(QSize(40, 40))
        self.Persona.setMaximumSize(QSize(40, 40))
        self.Persona.setPixmap(QPixmap(u":/Iconos/person_50dp_000000_FILL0_wght400_GRAD0_opsz48.png"))
        self.Persona.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Persona)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Panel_icono = QPushButton(self.Icono_Widget)
        self.Panel_icono.setObjectName(u"Panel_icono")
        icon = QIcon()
        icon.addFile(u":/Iconos/dashboard_customize_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Iconos/dashboard_customize_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Panel_icono.setIcon(icon)
        self.Panel_icono.setCheckable(True)
        self.Panel_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Panel_icono)

        self.Perfil_icono = QPushButton(self.Icono_Widget)
        self.Perfil_icono.setObjectName(u"Perfil_icono")
        icon1 = QIcon()
        icon1.addFile(u":/Iconos/person_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Iconos/person_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Perfil_icono.setIcon(icon1)
        self.Perfil_icono.setCheckable(True)
        self.Perfil_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Perfil_icono)

        self.Analizis_icono = QPushButton(self.Icono_Widget)
        self.Analizis_icono.setObjectName(u"Analizis_icono")
        icon2 = QIcon()
        icon2.addFile(u":/Iconos/analytics_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Iconos/analytics_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Analizis_icono.setIcon(icon2)
        self.Analizis_icono.setCheckable(True)
        self.Analizis_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Analizis_icono)

        self.Noticias_icono = QPushButton(self.Icono_Widget)
        self.Noticias_icono.setObjectName(u"Noticias_icono")
        icon3 = QIcon()
        icon3.addFile(u":/Iconos/notifications_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Iconos/notifications_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Noticias_icono.setIcon(icon3)
        self.Noticias_icono.setCheckable(True)
        self.Noticias_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Noticias_icono)

        self.Ajustes_icono = QPushButton(self.Icono_Widget)
        self.Ajustes_icono.setObjectName(u"Ajustes_icono")
        icon4 = QIcon()
        icon4.addFile(u":/Iconos/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Iconos/settings_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Ajustes_icono.setIcon(icon4)
        self.Ajustes_icono.setCheckable(True)
        self.Ajustes_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Ajustes_icono)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.Barra_Espacio = QSpacerItem(20, 104, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.Barra_Espacio)

        self.cerrar_sesion_Icono = QPushButton(self.Icono_Widget)
        self.cerrar_sesion_Icono.setObjectName(u"cerrar_sesion_Icono")
        icon5 = QIcon()
        icon5.addFile(u":/Iconos/power_settings_new_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cerrar_sesion_Icono.setIcon(icon5)
        self.cerrar_sesion_Icono.setCheckable(True)
        self.cerrar_sesion_Icono.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.cerrar_sesion_Icono)


        self.gridLayout.addWidget(self.Icono_Widget, 0, 0, 1, 1)

        self.Nombres_Widget = QWidget(self.centralwidget)
        self.Nombres_Widget.setObjectName(u"Nombres_Widget")
        self.Nombres_Widget.setStyleSheet(u"QWidget{\n"
"     \n"
"	background-color: rgb(155, 155, 221);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"	\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.Nombres_Widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 20, -1)
        self.Perfil_nombre = QLabel(self.Nombres_Widget)
        self.Perfil_nombre.setObjectName(u"Perfil_nombre")
        self.Perfil_nombre.setMinimumSize(QSize(40, 40))
        self.Perfil_nombre.setMaximumSize(QSize(40, 40))
        self.Perfil_nombre.setPixmap(QPixmap(u":/Iconos/person_50dp_000000_FILL0_wght400_GRAD0_opsz48.png"))
        self.Perfil_nombre.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.Perfil_nombre)

        self.Nombre_usuarios = QLabel(self.Nombres_Widget)
        self.Nombre_usuarios.setObjectName(u"Nombre_usuarios")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.Nombre_usuarios.setFont(font)

        self.horizontalLayout_3.addWidget(self.Nombre_usuarios)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, -1, -1)
        self.panel_nombre = QPushButton(self.Nombres_Widget)
        self.panel_nombre.setObjectName(u"panel_nombre")
        self.panel_nombre.setIcon(icon)
        self.panel_nombre.setCheckable(True)
        self.panel_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.panel_nombre)

        self.perfil_nombre = QPushButton(self.Nombres_Widget)
        self.perfil_nombre.setObjectName(u"perfil_nombre")
        self.perfil_nombre.setIcon(icon1)
        self.perfil_nombre.setCheckable(True)
        self.perfil_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.perfil_nombre)

        self.analizis_nombre = QPushButton(self.Nombres_Widget)
        self.analizis_nombre.setObjectName(u"analizis_nombre")
        self.analizis_nombre.setIcon(icon2)
        self.analizis_nombre.setCheckable(True)
        self.analizis_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.analizis_nombre)

        self.noticias_nombre = QPushButton(self.Nombres_Widget)
        self.noticias_nombre.setObjectName(u"noticias_nombre")
        self.noticias_nombre.setIcon(icon3)
        self.noticias_nombre.setCheckable(True)
        self.noticias_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.noticias_nombre)

        self.ajustes_nombre = QPushButton(self.Nombres_Widget)
        self.ajustes_nombre.setObjectName(u"ajustes_nombre")
        self.ajustes_nombre.setIcon(icon4)
        self.ajustes_nombre.setCheckable(True)
        self.ajustes_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.ajustes_nombre)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 164, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.cerrar_sesion = QPushButton(self.Nombres_Widget)
        self.cerrar_sesion.setObjectName(u"cerrar_sesion")
        self.cerrar_sesion.setIcon(icon5)
        self.cerrar_sesion.setCheckable(True)
        self.cerrar_sesion.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.cerrar_sesion)


        self.gridLayout.addWidget(self.Nombres_Widget, 0, 1, 1, 1)

        self.Main_principal_Widget = QWidget(self.centralwidget)
        self.Main_principal_Widget.setObjectName(u"Main_principal_Widget")
        self.Main_principal_Widget.setStyleSheet(u"background-color: rgb(189, 180, 222);")
        self.verticalLayout_6 = QVBoxLayout(self.Main_principal_Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Encabezado = QWidget(self.Main_principal_Widget)
        self.Encabezado.setObjectName(u"Encabezado")
        self.verticalLayout_5 = QVBoxLayout(self.Encabezado)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Menu_icono = QPushButton(self.Encabezado)
        self.Menu_icono.setObjectName(u"Menu_icono")
        self.Menu_icono.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/Iconos/menu_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Menu_icono.setIcon(icon6)
        self.Menu_icono.setIconSize(QSize(20, 20))
        self.Menu_icono.setCheckable(True)
        self.Menu_icono.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.Menu_icono)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Buscador_Qline = QLineEdit(self.Encabezado)
        self.Buscador_Qline.setObjectName(u"Buscador_Qline")

        self.horizontalLayout.addWidget(self.Buscador_Qline)

        self.Buscador_icono = QPushButton(self.Encabezado)
        self.Buscador_icono.setObjectName(u"Buscador_icono")
        icon7 = QIcon()
        icon7.addFile(u":/Iconos/search_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Buscador_icono.setIcon(icon7)
        self.Buscador_icono.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Buscador_icono)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.perfil_buscador_icono = QPushButton(self.Encabezado)
        self.perfil_buscador_icono.setObjectName(u"perfil_buscador_icono")
        self.perfil_buscador_icono.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/Iconos/account_circle_48dp_000000_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.perfil_buscador_icono.setIcon(icon8)
        self.perfil_buscador_icono.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.perfil_buscador_icono)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addWidget(self.Encabezado)

        self.MultiVentanas_Widget = QStackedWidget(self.Main_principal_Widget)
        self.MultiVentanas_Widget.setObjectName(u"MultiVentanas_Widget")
        self.MultiVentanas_Widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Panel = QWidget()
        self.Panel.setObjectName(u"Panel")
        self.label_4 = QLabel(self.Panel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 140, 49, 16))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        self.label_4.setFont(font1)
        self.MultiVentanas_Widget.addWidget(self.Panel)
        self.Noticias = QWidget()
        self.Noticias.setObjectName(u"Noticias")
        self.label_3 = QLabel(self.Noticias)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 130, 49, 16))
        self.label_3.setFont(font1)
        self.MultiVentanas_Widget.addWidget(self.Noticias)
        self.Ajustes = QWidget()
        self.Ajustes.setObjectName(u"Ajustes")
        self.label = QLabel(self.Ajustes)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 130, 49, 16))
        self.label.setFont(font1)
        self.MultiVentanas_Widget.addWidget(self.Ajustes)
        self.Analizis = QWidget()
        self.Analizis.setObjectName(u"Analizis")
        self.label_2 = QLabel(self.Analizis)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 160, 49, 16))
        self.label_2.setFont(font1)
        self.MultiVentanas_Widget.addWidget(self.Analizis)
        self.Perfil = QWidget()
        self.Perfil.setObjectName(u"Perfil")
        self.label_5 = QLabel(self.Perfil)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 170, 49, 16))
        self.label_5.setFont(font1)
        self.MultiVentanas_Widget.addWidget(self.Perfil)

        self.verticalLayout_6.addWidget(self.MultiVentanas_Widget)


        self.gridLayout.addWidget(self.Main_principal_Widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cerrar_sesion.toggled.connect(MainWindow.close)
        self.cerrar_sesion_Icono.toggled.connect(MainWindow.close)
        self.panel_nombre.toggled.connect(self.Panel_icono.setChecked)
        self.perfil_nombre.toggled.connect(self.Perfil_icono.setChecked)
        self.analizis_nombre.toggled.connect(self.Analizis_icono.setChecked)
        self.noticias_nombre.toggled.connect(self.Noticias_icono.setChecked)
        self.ajustes_nombre.toggled.connect(self.Ajustes_icono.setChecked)
        self.Ajustes_icono.toggled.connect(self.ajustes_nombre.setChecked)
        self.Noticias_icono.toggled.connect(self.noticias_nombre.setChecked)
        self.Analizis_icono.toggled.connect(self.analizis_nombre.setChecked)
        self.Perfil_icono.toggled.connect(self.perfil_nombre.setChecked)
        self.Panel_icono.toggled.connect(self.panel_nombre.setChecked)
        self.Menu_icono.toggled.connect(self.Icono_Widget.setHidden)
        self.Menu_icono.toggled.connect(self.Nombres_Widget.setVisible)

        self.MultiVentanas_Widget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Persona.setText("")
        self.Panel_icono.setText("")
        self.Perfil_icono.setText("")
        self.Analizis_icono.setText("")
        self.Noticias_icono.setText("")
        self.Ajustes_icono.setText("")
        self.cerrar_sesion_Icono.setText("")
        self.Perfil_nombre.setText("")
        self.Nombre_usuarios.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.panel_nombre.setText(QCoreApplication.translate("MainWindow", u"Panel", None))
        self.perfil_nombre.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.analizis_nombre.setText(QCoreApplication.translate("MainWindow", u"Analizis", None))
        self.noticias_nombre.setText(QCoreApplication.translate("MainWindow", u"Noticias", None))
        self.ajustes_nombre.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.Menu_icono.setText("")
        self.Buscador_icono.setText("")
        self.perfil_buscador_icono.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Panel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Noticias", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Analizis", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
    # retranslateUi


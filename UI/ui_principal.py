# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import UI.recursos_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Icono_Widget = QWidget(self.centralwidget)
        self.Icono_Widget.setObjectName("Icono_Widget")
        self.Icono_Widget.setStyleSheet(
            "QWidget{background-color: rgb(155, 155, 221);}QPushButton {color: white;height:30px;border:none;border-radius:10px;}QPushButton:checked{background-color: #F5FAFE;color:#1F95EF;font-weight:bold;}"
        )
        self.verticalLayout_2 = QVBoxLayout(self.Icono_Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Persona = QLabel(self.Icono_Widget)
        self.Persona.setObjectName("Persona")
        self.Persona.setMinimumSize(QSize(40, 40))
        self.Persona.setMaximumSize(QSize(40, 40))
        self.Persona.setPixmap(
            QPixmap(":/Iconos/person_50dp_000000_FILL0_wght400_GRAD0_opsz48.png")
        )
        self.Persona.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Persona)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Panel_icono = QPushButton(self.Icono_Widget)
        self.Panel_icono.setObjectName("Panel_icono")
        icon = QIcon()
        icon.addFile(
            ":/Iconos/dashboard_customize_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon.addFile(
            ":/Iconos/dashboard_customize_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.On,
        )
        self.Panel_icono.setIcon(icon)
        self.Panel_icono.setCheckable(True)
        self.Panel_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Panel_icono)

        self.Personalizado_icono = QPushButton(self.Icono_Widget)
        self.Personalizado_icono.setObjectName("Personalizado_icono")
        icon1 = QIcon()
        icon1.addFile(
            ":/Iconos/person_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon1.addFile(
            ":/Iconos/person_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.On,
        )
        self.Personalizado_icono.setIcon(icon1)
        self.Personalizado_icono.setCheckable(True)
        self.Personalizado_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Personalizado_icono)

        self.Analizis_icono = QPushButton(self.Icono_Widget)
        self.Analizis_icono.setObjectName("Analizis_icono")
        icon2 = QIcon()
        icon2.addFile(
            ":/Iconos/analytics_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon2.addFile(
            ":/Iconos/analytics_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.On,
        )
        self.Analizis_icono.setIcon(icon2)
        self.Analizis_icono.setCheckable(True)
        self.Analizis_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Analizis_icono)

        self.Noticias_icono = QPushButton(self.Icono_Widget)
        self.Noticias_icono.setObjectName("Noticias_icono")
        icon3 = QIcon()
        icon3.addFile(
            ":/Iconos/notifications_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon3.addFile(
            ":/Iconos/notifications_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.On,
        )
        self.Noticias_icono.setIcon(icon3)
        self.Noticias_icono.setCheckable(True)
        self.Noticias_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Noticias_icono)

        self.Ajustes_icono = QPushButton(self.Icono_Widget)
        self.Ajustes_icono.setObjectName("Ajustes_icono")
        icon4 = QIcon()
        icon4.addFile(
            ":/Iconos/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon4.addFile(
            ":/Iconos/settings_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.On,
        )
        self.Ajustes_icono.setIcon(icon4)
        self.Ajustes_icono.setCheckable(True)
        self.Ajustes_icono.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Ajustes_icono)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.Barra_Espacio = QSpacerItem(
            20, 104, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.Barra_Espacio)

        self.cerrar_sesion_Icono = QPushButton(self.Icono_Widget)
        self.cerrar_sesion_Icono.setObjectName("cerrar_sesion_Icono")
        icon5 = QIcon()
        icon5.addFile(
            ":/Iconos/power_settings_new_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.cerrar_sesion_Icono.setIcon(icon5)
        self.cerrar_sesion_Icono.setCheckable(True)
        self.cerrar_sesion_Icono.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.cerrar_sesion_Icono)

        self.gridLayout.addWidget(self.Icono_Widget, 0, 0, 1, 1)

        self.Nombres_Widget = QWidget(self.centralwidget)
        self.Nombres_Widget.setObjectName("Nombres_Widget")
        self.Nombres_Widget.setStyleSheet(
            "QWidget{background-color: rgb(155, 155, 221);color:white;}QPushButton {color:white;text-align:left;height:30px;border:none;padding-left:10px;border-top-left-radius:10px;border-bottom-left-radius:10px;}QPushButton:checked{background-color: #F5FAFE;color:#1F95EF;font-weight:bold;}"
        )
        self.verticalLayout_4 = QVBoxLayout(self.Nombres_Widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 20, -1)
        self.Perfil_nombre = QLabel(self.Nombres_Widget)
        self.Perfil_nombre.setObjectName("Perfil_nombre")
        self.Perfil_nombre.setMinimumSize(QSize(40, 40))
        self.Perfil_nombre.setMaximumSize(QSize(40, 40))
        self.Perfil_nombre.setPixmap(
            QPixmap(":/Iconos/person_50dp_000000_FILL0_wght400_GRAD0_opsz48.png")
        )
        self.Perfil_nombre.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.Perfil_nombre)

        self.Nombre_usuarios = QLabel(self.Nombres_Widget)
        self.Nombre_usuarios.setObjectName("Nombre_usuarios")
        font = QFont()
        font.setFamilies(["Inter"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.Nombre_usuarios.setFont(font)

        self.horizontalLayout_3.addWidget(self.Nombre_usuarios)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, -1, -1)
        self.panel_nombre = QPushButton(self.Nombres_Widget)
        self.panel_nombre.setObjectName("panel_nombre")
        self.panel_nombre.setIcon(icon)
        self.panel_nombre.setCheckable(True)
        self.panel_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.panel_nombre)

        self.perfil_nombre = QPushButton(self.Nombres_Widget)
        self.perfil_nombre.setObjectName("perfil_nombre")
        self.perfil_nombre.setIcon(icon1)
        self.perfil_nombre.setCheckable(True)
        self.perfil_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.perfil_nombre)

        self.analizis_nombre = QPushButton(self.Nombres_Widget)
        self.analizis_nombre.setObjectName("analizis_nombre")
        self.analizis_nombre.setIcon(icon2)
        self.analizis_nombre.setCheckable(True)
        self.analizis_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.analizis_nombre)

        self.noticias_nombre = QPushButton(self.Nombres_Widget)
        self.noticias_nombre.setObjectName("noticias_nombre")
        self.noticias_nombre.setIcon(icon3)
        self.noticias_nombre.setCheckable(True)
        self.noticias_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.noticias_nombre)

        self.ajustes_nombre = QPushButton(self.Nombres_Widget)
        self.ajustes_nombre.setObjectName("ajustes_nombre")
        self.ajustes_nombre.setIcon(icon4)
        self.ajustes_nombre.setCheckable(True)
        self.ajustes_nombre.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.ajustes_nombre)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 164, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.cerrar_sesion = QPushButton(self.Nombres_Widget)
        self.cerrar_sesion.setObjectName("cerrar_sesion")
        self.cerrar_sesion.setIcon(icon5)
        self.cerrar_sesion.setCheckable(True)
        self.cerrar_sesion.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.cerrar_sesion)

        self.gridLayout.addWidget(self.Nombres_Widget, 0, 1, 1, 1)

        self.Main_principal_Widget = QWidget(self.centralwidget)
        self.Main_principal_Widget.setObjectName("Main_principal_Widget")
        self.Main_principal_Widget.setStyleSheet(
            "background-color: rgb(189, 180, 222);"
        )
        self.verticalLayout_6 = QVBoxLayout(self.Main_principal_Widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Encabezado = QWidget(self.Main_principal_Widget)
        self.Encabezado.setObjectName("Encabezado")
        self.verticalLayout_5 = QVBoxLayout(self.Encabezado)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Menu_icono = QPushButton(self.Encabezado)
        self.Menu_icono.setObjectName("Menu_icono")
        self.Menu_icono.setStyleSheet("border:none;")
        icon6 = QIcon()
        icon6.addFile(
            ":/Iconos/menu_24dp_000000_FILL0_wght400_GRAD0_opsz24.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.Menu_icono.setIcon(icon6)
        self.Menu_icono.setIconSize(QSize(20, 20))
        self.Menu_icono.setCheckable(True)
        self.Menu_icono.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.Menu_icono)

        self.horizontalSpacer = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.perfil_buscador_icono = QPushButton(self.Encabezado)
        self.perfil_buscador_icono.setObjectName("perfil_buscador_icono")
        self.perfil_buscador_icono.setStyleSheet("border:none;")
        icon7 = QIcon()
        icon7.addFile(
            ":/Iconos/account_circle_48dp_000000_FILL0_wght400_GRAD0_opsz48.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.perfil_buscador_icono.setIcon(icon7)
        self.perfil_buscador_icono.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.perfil_buscador_icono)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.addWidget(self.Encabezado)

        self.MultiVentanas_Widget = QStackedWidget(self.Main_principal_Widget)
        self.MultiVentanas_Widget.setObjectName("MultiVentanas_Widget")
        self.MultiVentanas_Widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Panel = QWidget()
        self.Panel.setObjectName("Panel")
        self.panel_layout = QVBoxLayout(self.Panel)
        self.panel_layout.setObjectName("panel_layout")
        self.panel_layout.setContentsMargins(20, 20, 20, 20)
        self.titulo_panel = QLabel(self.Panel)
        self.titulo_panel.setObjectName("titulo_panel")
        font1 = QFont()
        font1.setFamilies(["Inter"])
        font1.setPointSize(20)
        self.titulo_panel.setFont(font1)

        self.panel_layout.addWidget(self.titulo_panel)

        self.busqueda_layout = QHBoxLayout()
        self.busqueda_layout.setObjectName("busqueda_layout")
        self.buscador_input = QLineEdit(self.Panel)
        self.buscador_input.setObjectName("buscador_input")
        self.buscador_input.setMinimumSize(QSize(0, 40))

        self.busqueda_layout.addWidget(self.buscador_input)

        self.btn_importar = QPushButton(self.Panel)
        self.btn_importar.setObjectName("btn_importar")
        self.btn_importar.setMinimumSize(QSize(150, 40))

        self.busqueda_layout.addWidget(self.btn_importar)

        self.panel_layout.addLayout(self.busqueda_layout)

        self.tabla_tesis = QTableWidget(self.Panel)
        if self.tabla_tesis.columnCount() < 5:
            self.tabla_tesis.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_tesis.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_tesis.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_tesis.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_tesis.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_tesis.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_tesis.setObjectName("tabla_tesis")
        self.tabla_tesis.setAlternatingRowColors(True)
        self.tabla_tesis.setColumnCount(5)

        self.panel_layout.addWidget(self.tabla_tesis)

        self.botones_tesis_layout = QHBoxLayout()
        self.botones_tesis_layout.setObjectName("botones_tesis_layout")
        self.horizontalSpacer_botones = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.botones_tesis_layout.addItem(self.horizontalSpacer_botones)

        self.btn_editar_tesis = QPushButton(self.Panel)
        self.btn_editar_tesis.setObjectName("btn_editar_tesis")
        self.btn_editar_tesis.setMinimumSize(QSize(120, 35))
        self.btn_editar_tesis.setEnabled(False)
        self.btn_editar_tesis.setStyleSheet(
            "background-color: #FF9800; color: white; padding: 8px 16px; border: none; border-radius: 5px; font-weight: bold;"
        )

        self.botones_tesis_layout.addWidget(self.btn_editar_tesis)

        self.btn_eliminar_tesis = QPushButton(self.Panel)
        self.btn_eliminar_tesis.setObjectName("btn_eliminar_tesis")
        self.btn_eliminar_tesis.setMinimumSize(QSize(120, 35))
        self.btn_eliminar_tesis.setEnabled(False)
        self.btn_eliminar_tesis.setStyleSheet(
            "background-color: #F44336; color: white; padding: 8px 16px; border: none; border-radius: 5px; font-weight: bold;"
        )

        self.botones_tesis_layout.addWidget(self.btn_eliminar_tesis)

        self.panel_layout.addLayout(self.botones_tesis_layout)

        self.MultiVentanas_Widget.addWidget(self.Panel)
        self.Perfil = QWidget()
        self.Perfil.setObjectName("Perfil")
        self.perfil_layout = QVBoxLayout(self.Perfil)
        self.perfil_layout.setObjectName("perfil_layout")
        self.perfil_layout.setContentsMargins(20, 20, 20, 20)
        self.titulo_perfil = QLabel(self.Perfil)
        self.titulo_perfil.setObjectName("titulo_perfil")
        self.titulo_perfil.setFont(font1)

        self.perfil_layout.addWidget(self.titulo_perfil)

        self.info_frame = QFrame(self.Perfil)
        self.info_frame.setObjectName("info_frame")
        self.info_frame.setMinimumSize(QSize(0, 180))
        self.info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.info_layout = QVBoxLayout(self.info_frame)
        self.info_layout.setObjectName("info_layout")
        self.avatar_label = QLabel(self.info_frame)
        self.avatar_label.setObjectName("avatar_label")
        self.avatar_label.setMinimumSize(QSize(80, 80))
        self.avatar_label.setMaximumSize(QSize(80, 80))
        self.avatar_label.setStyleSheet(
            "background-color: #9B9BDD;border-radius: 40px;"
        )
        self.avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_layout.addWidget(self.avatar_label)

        self.valor_nombre = QLabel(self.info_frame)
        self.valor_nombre.setObjectName("valor_nombre")

        self.info_layout.addWidget(self.valor_nombre)

        self.valor_usuario = QLabel(self.info_frame)
        self.valor_usuario.setObjectName("valor_usuario")

        self.info_layout.addWidget(self.valor_usuario)

        self.valor_email = QLabel(self.info_frame)
        self.valor_email.setObjectName("valor_email")

        self.info_layout.addWidget(self.valor_email)

        self.perfil_layout.addWidget(self.info_frame)

        self.stats_group = QGroupBox(self.Perfil)
        self.stats_group.setObjectName("stats_group")
        self.stats_layout = QVBoxLayout(self.stats_group)
        self.stats_layout.setObjectName("stats_layout")
        self.valor_tesis = QLabel(self.stats_group)
        self.valor_tesis.setObjectName("valor_tesis")

        self.stats_layout.addWidget(self.valor_tesis)

        self.valor_capitulos = QLabel(self.stats_group)
        self.valor_capitulos.setObjectName("valor_capitulos")

        self.stats_layout.addWidget(self.valor_capitulos)

        self.valor_refs = QLabel(self.stats_group)
        self.valor_refs.setObjectName("valor_refs")

        self.stats_layout.addWidget(self.valor_refs)

        self.perfil_layout.addWidget(self.stats_group)

        self.MultiVentanas_Widget.addWidget(self.Perfil)
        self.Analizis = QWidget()
        self.Analizis.setObjectName("Analizis")
        self.analisis_layout = QVBoxLayout(self.Analizis)
        self.analisis_layout.setObjectName("analisis_layout")
        self.analisis_layout.setContentsMargins(20, 20, 20, 20)
        self.titulo_analisis = QLabel(self.Analizis)
        self.titulo_analisis.setObjectName("titulo_analisis")
        self.titulo_analisis.setFont(font1)

        self.analisis_layout.addWidget(self.titulo_analisis)

        self.resumen_group = QGroupBox(self.Analizis)
        self.resumen_group.setObjectName("resumen_group")
        self.resumen_layout = QVBoxLayout(self.resumen_group)
        self.resumen_layout.setObjectName("resumen_layout")
        self.resumen_valor_tesis = QLabel(self.resumen_group)
        self.resumen_valor_tesis.setObjectName("resumen_valor_tesis")

        self.resumen_layout.addWidget(self.resumen_valor_tesis)

        self.resumen_valor_autores = QLabel(self.resumen_group)
        self.resumen_valor_autores.setObjectName("resumen_valor_autores")

        self.resumen_layout.addWidget(self.resumen_valor_autores)

        self.resumen_valor_refs = QLabel(self.resumen_group)
        self.resumen_valor_refs.setObjectName("resumen_valor_refs")

        self.resumen_layout.addWidget(self.resumen_valor_refs)

        self.analisis_layout.addWidget(self.resumen_group)

        self.tabla_anio = QTableWidget(self.Analizis)
        if self.tabla_anio.columnCount() < 2:
            self.tabla_anio.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_anio.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_anio.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tabla_anio.setObjectName("tabla_anio")
        self.tabla_anio.setMinimumSize(QSize(0, 150))
        self.tabla_anio.setAlternatingRowColors(True)
        self.tabla_anio.setColumnCount(2)

        self.analisis_layout.addWidget(self.tabla_anio)

        self.MultiVentanas_Widget.addWidget(self.Analizis)
        self.Noticias = QWidget()
        self.Noticias.setObjectName("Noticias")
        self.noticias_layout = QVBoxLayout(self.Noticias)
        self.noticias_layout.setObjectName("noticias_layout")
        self.noticias_layout.setContentsMargins(20, 20, 20, 20)
        self.titulo_noticias = QLabel(self.Noticias)
        self.titulo_noticias.setObjectName("titulo_noticias")
        self.titulo_noticias.setFont(font1)

        self.noticias_layout.addWidget(self.titulo_noticias)

        self.historial_scroll = QScrollArea(self.Noticias)
        self.historial_scroll.setObjectName("historial_scroll")
        self.historial_scroll.setMinimumSize(QSize(0, 350))
        self.historial_scroll.setStyleSheet("QScrollArea {border: none;}")
        self.historial_scroll.setWidgetResizable(True)
        self.historial_container = QWidget()
        self.historial_container.setObjectName("historial_container")
        self.historial_container.setGeometry(QRect(0, 0, 441, 377))
        self.historial_layout = QVBoxLayout(self.historial_container)
        self.historial_layout.setObjectName("historial_layout")
        self.historial_scroll.setWidget(self.historial_container)

        self.noticias_layout.addWidget(self.historial_scroll)

        self.MultiVentanas_Widget.addWidget(self.Noticias)
        self.Ajustes = QWidget()
        self.Ajustes.setObjectName("Ajustes")
        self.ajustes_layout = QVBoxLayout(self.Ajustes)
        self.ajustes_layout.setObjectName("ajustes_layout")
        self.ajustes_layout.setContentsMargins(20, 20, 20, 20)
        self.titulo_ajustes = QLabel(self.Ajustes)
        self.titulo_ajustes.setObjectName("titulo_ajustes")
        self.titulo_ajustes.setFont(font1)

        self.ajustes_layout.addWidget(self.titulo_ajustes)

        self.db_group = QGroupBox(self.Ajustes)
        self.db_group.setObjectName("db_group")
        self.db_layout = QFormLayout(self.db_group)
        self.db_layout.setObjectName("db_layout")
        self.label_host = QLabel(self.db_group)
        self.label_host.setObjectName("label_host")

        self.db_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_host)

        self.host_input = QLineEdit(self.db_group)
        self.host_input.setObjectName("host_input")

        self.db_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.host_input)

        self.label_user = QLabel(self.db_group)
        self.label_user.setObjectName("label_user")

        self.db_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_user)

        self.user_input = QLineEdit(self.db_group)
        self.user_input.setObjectName("user_input")

        self.db_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.user_input)

        self.label_pass = QLabel(self.db_group)
        self.label_pass.setObjectName("label_pass")

        self.db_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_pass)

        self.pass_input = QLineEdit(self.db_group)
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.db_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pass_input)

        self.label_puerto = QLabel(self.db_group)
        self.label_puerto.setObjectName("label_puerto")

        self.db_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_puerto)

        self.puerto_input = QLineEdit(self.db_group)
        self.puerto_input.setObjectName("puerto_input")

        self.db_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.puerto_input)

        self.ajustes_layout.addWidget(self.db_group)

        self.db_buttons_layout = QHBoxLayout()
        self.db_buttons_layout.setObjectName("db_buttons_layout")
        self.btn_test = QPushButton(self.Ajustes)
        self.btn_test.setObjectName("btn_test")

        self.db_buttons_layout.addWidget(self.btn_test)

        self.btn_guardar = QPushButton(self.Ajustes)
        self.btn_guardar.setObjectName("btn_guardar")

        self.db_buttons_layout.addWidget(self.btn_guardar)

        self.ajustes_layout.addLayout(self.db_buttons_layout)

        self.user_group = QGroupBox(self.Ajustes)
        self.user_group.setObjectName("user_group")
        self.user_layout = QVBoxLayout(self.user_group)
        self.user_layout.setObjectName("user_layout")
        self.btn_cambiar_pass = QPushButton(self.user_group)
        self.btn_cambiar_pass.setObjectName("btn_cambiar_pass")

        self.user_layout.addWidget(self.btn_cambiar_pass)

        self.btn_editar_perfil = QPushButton(self.user_group)
        self.btn_editar_perfil.setObjectName("btn_editar_perfil")

        self.user_layout.addWidget(self.btn_editar_perfil)

        self.ajustes_layout.addWidget(self.user_group)

        self.about_group = QGroupBox(self.Ajustes)
        self.about_group.setObjectName("about_group")
        self.about_layout = QVBoxLayout(self.about_group)
        self.about_layout.setObjectName("about_layout")
        self.about_label = QLabel(self.about_group)
        self.about_label.setObjectName("about_label")
        self.about_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.about_layout.addWidget(self.about_label)

        self.ajustes_layout.addWidget(self.about_group)

        self.MultiVentanas_Widget.addWidget(self.Ajustes)

        self.verticalLayout_6.addWidget(self.MultiVentanas_Widget)

        self.gridLayout.addWidget(self.Main_principal_Widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 728, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cerrar_sesion.toggled.connect(MainWindow.close)
        self.cerrar_sesion_Icono.toggled.connect(MainWindow.close)
        self.panel_nombre.toggled.connect(self.Panel_icono.setChecked)
        self.perfil_nombre.toggled.connect(self.Personalizado_icono.setChecked)
        self.analizis_nombre.toggled.connect(self.Analizis_icono.setChecked)
        self.noticias_nombre.toggled.connect(self.Noticias_icono.setChecked)
        self.ajustes_nombre.toggled.connect(self.Ajustes_icono.setChecked)
        self.Ajustes_icono.toggled.connect(self.ajustes_nombre.setChecked)
        self.Noticias_icono.toggled.connect(self.noticias_nombre.setChecked)
        self.Analizis_icono.toggled.connect(self.analizis_nombre.setChecked)
        self.Personalizado_icono.toggled.connect(self.perfil_nombre.setChecked)
        self.Panel_icono.toggled.connect(self.panel_nombre.setChecked)
        self.Menu_icono.toggled.connect(self.Icono_Widget.setHidden)
        self.Menu_icono.toggled.connect(self.Nombres_Widget.setVisible)

        self.MultiVentanas_Widget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Gestion de Tesis", None)
        )
        self.Persona.setText("")
        self.Panel_icono.setText("")
        self.Personalizado_icono.setText("")
        self.Analizis_icono.setText("")
        self.Noticias_icono.setText("")
        self.Ajustes_icono.setText("")
        self.cerrar_sesion_Icono.setText("")
        self.Perfil_nombre.setText("")
        self.Nombre_usuarios.setText(
            QCoreApplication.translate("MainWindow", "Nombre", None)
        )
        self.panel_nombre.setText(
            QCoreApplication.translate("MainWindow", "Panel", None)
        )
        self.perfil_nombre.setText(
            QCoreApplication.translate("MainWindow", "Personalizado", None)
        )
        self.analizis_nombre.setText(
            QCoreApplication.translate("MainWindow", "Analizis", None)
        )
        self.noticias_nombre.setText(
            QCoreApplication.translate("MainWindow", "Noticias", None)
        )
        self.ajustes_nombre.setText(
            QCoreApplication.translate("MainWindow", "Ajustes", None)
        )
        self.cerrar_sesion.setText(
            QCoreApplication.translate("MainWindow", "Cerrar Sesion", None)
        )
        self.Menu_icono.setText("")
        self.perfil_buscador_icono.setText("")
        self.titulo_panel.setText(
            QCoreApplication.translate("MainWindow", "Gestion de Tesis", None)
        )
        self.buscador_input.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Buscar tesis por titulo o autor...", None
            )
        )
        self.btn_importar.setText(
            QCoreApplication.translate("MainWindow", "Importar Word", None)
        )
        ___qtablewidgetitem = self.tabla_tesis.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "ID", None)
        )
        ___qtablewidgetitem1 = self.tabla_tesis.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Titulo", None)
        )
        ___qtablewidgetitem2 = self.tabla_tesis.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Autor", None)
        )
        ___qtablewidgetitem3 = self.tabla_tesis.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "Anio", None)
        )
        ___qtablewidgetitem4 = self.tabla_tesis.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "Estado", None)
        )
        self.btn_editar_tesis.setText(
            QCoreApplication.translate("MainWindow", "Editar", None)
        )
        self.btn_eliminar_tesis.setText(
            QCoreApplication.translate("MainWindow", "Eliminar", None)
        )
        self.titulo_perfil.setText(
            QCoreApplication.translate(
                "MainWindow", "B\u00fasquedas Personalizadas", None
            )
        )
        self.avatar_label.setText("")
        self.valor_nombre.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.valor_usuario.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.valor_email.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.stats_group.setTitle(
            QCoreApplication.translate("MainWindow", "Estadisticas Personales", None)
        )
        self.valor_tesis.setText(
            QCoreApplication.translate("MainWindow", "Tesis creadas: 0", None)
        )
        self.valor_capitulos.setText(
            QCoreApplication.translate("MainWindow", "Capitulos: 0", None)
        )
        self.valor_refs.setText(
            QCoreApplication.translate("MainWindow", "Referencias: 0", None)
        )
        self.titulo_analisis.setText(
            QCoreApplication.translate("MainWindow", "Analisis de Datos", None)
        )
        self.resumen_group.setTitle(
            QCoreApplication.translate("MainWindow", "Resumen General", None)
        )
        self.resumen_valor_tesis.setText(
            QCoreApplication.translate("MainWindow", "Total tesis: 0", None)
        )
        self.resumen_valor_autores.setText(
            QCoreApplication.translate("MainWindow", "Total autores: 0", None)
        )
        self.resumen_valor_refs.setText(
            QCoreApplication.translate("MainWindow", "Total referencias: 0", None)
        )
        ___qtablewidgetitem5 = self.tabla_anio.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", "Anio", None)
        )
        ___qtablewidgetitem6 = self.tabla_anio.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", "Cantidad", None)
        )
        self.titulo_noticias.setText(
            QCoreApplication.translate("MainWindow", "Historial de Actividad", None)
        )
        self.titulo_ajustes.setText(
            QCoreApplication.translate("MainWindow", "Configuracion", None)
        )
        self.db_group.setTitle(
            QCoreApplication.translate("MainWindow", "Base de Datos", None)
        )
        self.label_host.setText(QCoreApplication.translate("MainWindow", "Host:", None))
        self.host_input.setText(
            QCoreApplication.translate("MainWindow", "localhost", None)
        )
        self.label_user.setText(
            QCoreApplication.translate("MainWindow", "Usuario:", None)
        )
        self.user_input.setText(QCoreApplication.translate("MainWindow", "root", None))
        self.label_pass.setText(
            QCoreApplication.translate("MainWindow", "Contrasena:", None)
        )
        self.pass_input.setText(
            QCoreApplication.translate("MainWindow", "admin123", None)
        )
        self.label_puerto.setText(
            QCoreApplication.translate("MainWindow", "Puerto:", None)
        )
        self.puerto_input.setText(
            QCoreApplication.translate("MainWindow", "3306", None)
        )
        self.btn_test.setText(
            QCoreApplication.translate("MainWindow", "Probar Conexion", None)
        )
        self.btn_guardar.setText(
            QCoreApplication.translate("MainWindow", "Guardar", None)
        )
        self.user_group.setTitle(
            QCoreApplication.translate("MainWindow", "Usuario", None)
        )
        self.btn_cambiar_pass.setText(
            QCoreApplication.translate("MainWindow", "Cambiar Contrasena", None)
        )
        self.btn_editar_perfil.setText(
            QCoreApplication.translate("MainWindow", "Editar Perfil", None)
        )
        self.about_group.setTitle(
            QCoreApplication.translate("MainWindow", "Acerca de", None)
        )
        self.about_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Sistema de Gestion de Tesis v1.0", None
            )
        )

    # retranslateUi

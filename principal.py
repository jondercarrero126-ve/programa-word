from UI.ui_principal import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QFrame,
    QScrollArea,
)
from PySide6.QtCore import Qt, QThread, Signal, QObject
from PySide6.QtGui import QFont
from database import Database
from word_extractor.extractor import WordExtractor
import os


class ImportWorker(QThread):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, filepath, parent=None):
        super().__init__(parent)
        self.filepath = filepath

    def run(self):
        try:
            extractor = WordExtractor(self.filepath)
            datos = extractor.extract_all()
            self.finished.emit(datos)
        except Exception as e:
            self.error.emit(str(e))


class TesisController(QObject):
    tesis_changed = Signal(list)
    error_occurred = Signal(str)
    import_success = Signal(str)
    import_error = Signal(str)

    def __init__(self, db: Database, usuario: dict):
        super().__init__()
        self.db = db
        self.usuario = usuario
        self._tesis_cache = []

    def cargar_tesis(self):
        if self.db.connect():
            try:
                tesis = self.db.fetch_all(
                    "SELECT * FROM tesis ORDER BY fecha_creacion DESC"
                )
                self._tesis_cache = tesis if tesis else []
                self.db.disconnect()
                self.tesis_changed.emit(self._tesis_cache)
            except Exception as e:
                self.db.disconnect()
                self.error_occurred.emit(f"Error al cargar tesis: {str(e)}")
        else:
            self.error_occurred.emit("No se pudo conectar a la base de datos")

    def buscar_tesis(self, texto: str):
        if not texto:
            self.tesis_changed.emit(self._tesis_cache)
            return

        filtradas = [
            t
            for t in self._tesis_cache
            if texto.lower() in str(t.get("titulo", "")).lower()
            or texto.lower() in str(t.get("autor_principal", "")).lower()
        ]
        self.tesis_changed.emit(filtradas)

    def importar_tesis(self, datos: dict):
        if self.db.connect():
            try:
                query = """
                    INSERT INTO tesis (titulo, autor_principal, resumen, palabras_clave, anio, id_usuario, estado)
                    VALUES (%s, %s, %s, %s, %s, %s, 'borrador')
                """
                cursor = self.db.execute(
                    query,
                    (
                        datos["titulo"],
                        datos["autor_principal"],
                        datos["resumen"],
                        datos["palabras_clave"],
                        datos["anio"],
                        self.usuario["id_usuario"],
                    ),
                )

                if cursor:
                    tesis_id = cursor.lastrowid

                    for i, cap in enumerate(datos["capitulos"], 1):
                        self.db.execute(
                            """INSERT INTO capitulos (id_tesis, numero_capitulo, titulo, contenido, orden)
                               VALUES (%s, %s, %s, %s, %s)""",
                            (tesis_id, i, cap["titulo"], cap["contenido"][:5000], i),
                        )

                    for ref in datos["referencias"]:
                        self.db.execute(
                            """INSERT INTO referencias (id_tesis, tipo, autor, titulo, anio, url)
                               VALUES (%s, %s, %s, %s, %s, %s)""",
                            (
                                tesis_id,
                                ref["tipo"],
                                ref["autor"],
                                ref["titulo"],
                                ref["anio"],
                                ref["url"],
                            ),
                        )

                    self.db.disconnect()
                    self.import_success.emit(datos["titulo"])
                    self.cargar_tesis()
            except Exception as e:
                self.db.disconnect()
                self.import_error.emit(f"Error al importar: {str(e)}")
        else:
            self.import_error.emit("No se pudo conectar a la base de datos")

    def obtener_estadisticas(self) -> dict:
        if self.db.connect():
            try:
                stats = {}
                result = self.db.fetch_one("SELECT COUNT(*) as total FROM tesis")
                stats["total_tesis"] = result["total"] if result else 0
                result = self.db.fetch_one("SELECT COUNT(*) as total FROM capitulos")
                stats["total_capitulos"] = result["total"] if result else 0
                result = self.db.fetch_one("SELECT COUNT(*) as total FROM referencias")
                stats["total_referencias"] = result["total"] if result else 0
                tesis = self.db.fetch_all(
                    "SELECT YEAR(fecha_creacion) as anio, COUNT(*) as cantidad FROM tesis GROUP BY YEAR(fecha_creacion)"
                )
                stats["tesis_por_anio"] = tesis if tesis else []
                self.db.disconnect()
                return stats
            except Exception:
                self.db.disconnect()
        return {
            "total_tesis": 0,
            "total_capitulos": 0,
            "total_referencias": 0,
            "tesis_por_anio": [],
        }


class Principal(QMainWindow, Ui_MainWindow):
    closed = Signal()

    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.db = Database()
        self.controller = TesisController(self.db, usuario)

        self.setupUi(self)
        self.setWindowTitle("Gestion de Tesis")

        self.Nombres_Widget.setHidden(True)
        self.Nombre_usuarios.setText(usuario.get("nombre", "Usuario"))

        self._conectar_navegacion()
        self._conectar_widgets()
        self._conectar_signals()
        self._actualizar_perfil()

        self.controller.cargar_tesis()

    def _conectar_navegacion(self):
        self.panel_nombre.clicked.connect(lambda: self._cambiar_pagina(0))
        self.Panel_icono.clicked.connect(lambda: self._cambiar_pagina(0))
        self.perfil_nombre.clicked.connect(lambda: self._cambiar_pagina(1))
        self.Perfil_icono.clicked.connect(lambda: self._cambiar_pagina(1))
        self.analizis_nombre.clicked.connect(lambda: self._cambiar_pagina(2))
        self.Analizis_icono.clicked.connect(lambda: self._cambiar_pagina(2))
        self.noticias_nombre.clicked.connect(lambda: self._cambiar_pagina(3))
        self.Noticias_icono.clicked.connect(lambda: self._cambiar_pagina(3))
        self.ajustes_nombre.clicked.connect(lambda: self._cambiar_pagina(4))
        self.Ajustes_icono.clicked.connect(lambda: self._cambiar_pagina(4))
        self.cerrar_sesion.clicked.connect(self.cerrar_sesion_accion)
        self.cerrar_sesion_Icono.clicked.connect(self.cerrar_sesion_accion)

    def _conectar_widgets(self):
        self.buscador_input.textChanged.connect(self.controller.buscar_tesis)
        self.btn_importar.clicked.connect(self._importar_tesis)
        self.btn_test.clicked.connect(self._probar_conexion)
        self.btn_guardar.clicked.connect(self._guardar_config)

    def _conectar_signals(self):
        self.controller.tesis_changed.connect(self._actualizar_tabla_tesis)
        self.controller.error_occurred.connect(self._mostrar_error)
        self.controller.import_success.connect(self._mostrar_exito)
        self.controller.import_error.connect(self._mostrar_error)

    def _cambiar_pagina(self, index: int):
        self.MultiVentanas_Widget.setCurrentIndex(index)
        if index == 2:
            self._actualizar_analisis()

    def _actualizar_perfil(self):
        self.valor_nombre.setText(f"Nombre: {self.usuario.get('nombre', 'N/A')}")
        self.valor_usuario.setText(f"Usuario: {self.usuario.get('username', 'N/A')}")
        self.valor_email.setText(f"Email: {self.usuario.get('email', 'N/A')}")

        stats = self.controller.obtener_estadisticas()
        self.valor_tesis.setText(f"Tesis creadas: {stats.get('total_tesis', 0)}")
        self.valor_capitulos.setText(f"Capitulos: {stats.get('total_capitulos', 0)}")
        self.valor_refs.setText(f"Referencias: {stats.get('total_referencias', 0)}")

    def _actualizar_tabla_tesis(self, tesis):
        self.tabla_tesis.setRowCount(len(tesis))
        for i, t in enumerate(tesis):
            self.tabla_tesis.setItem(i, 0, QTableWidgetItem(str(t["id_tesis"])))
            self.tabla_tesis.setItem(
                i,
                1,
                QTableWidgetItem(
                    t["titulo"][:50] + "..." if len(t["titulo"]) > 50 else t["titulo"]
                ),
            )
            self.tabla_tesis.setItem(i, 2, QTableWidgetItem(t["autor_principal"] or ""))
            self.tabla_tesis.setItem(
                i, 3, QTableWidgetItem(str(t["anio"]) if t["anio"] else "")
            )
            self.tabla_tesis.setItem(i, 4, QTableWidgetItem(t["estado"]))

        self._actualizar_perfil()

    def _actualizar_analisis(self):
        stats = self.controller.obtener_estadisticas()

        self.resumen_valor_tesis.setText(f"Total tesis: {stats.get('total_tesis', 0)}")
        self.resumen_valor_autores.setText(
            f"Total autores: {len(set([t['autor_principal'] for t in self.controller._tesis_cache if t.get('autor_principal')]))}"
        )
        self.resumen_valor_refs.setText(
            f"Total referencias: {stats.get('total_referencias', 0)}"
        )

        tesis_por_anio = stats.get("tesis_por_anio", [])
        self.tabla_anio.setRowCount(len(tesis_por_anio))
        for i, row in enumerate(tesis_por_anio):
            self.tabla_anio.setItem(i, 0, QTableWidgetItem(str(row.get("anio", ""))))
            self.tabla_anio.setItem(i, 1, QTableWidgetItem(str(row.get("cantidad", 0))))

    def _importar_tesis(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo Word", "", "Documentos Word (*.docx *.doc)"
        )

        if archivo:
            self._agregar_evento_historial(
                "Importando tesis...", f"Archivo: {os.path.basename(archivo)}", "info"
            )

            self.worker = ImportWorker(archivo)
            self.worker.finished.connect(
                lambda datos: self.controller.importar_tesis(datos)
            )
            self.worker.error.connect(lambda err: self._mostrar_error(err))
            self.worker.start()

    def _agregar_evento_historial(
        self, titulo: str, descripcion: str, tipo: str = "info"
    ):
        color_map = {
            "success": "#4CAF50",
            "error": "#F44336",
            "warning": "#FF9800",
            "info": "#2196F3",
        }
        color = color_map.get(tipo, "#666")

        frame = QFrame()
        frame.setStyleSheet(
            f"background-color: #f5f5f5; border-radius: 5px; padding: 10px; border-left: 4px solid {color};"
        )

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 5, 10, 5)

        titulo_label = QLabel(titulo)
        titulo_label.setStyleSheet("font-weight: bold;")
        desc_label = QLabel(descripcion)
        desc_label.setStyleSheet("color: #666; font-size: 11px;")

        layout.addWidget(titulo_label)
        layout.addWidget(desc_label)

        self.historial_layout.insertWidget(0, frame)

    def _probar_conexion(self):
        self.db.host = self.host_input.text()
        self.db.user = self.user_input.text()
        self.db.password = self.pass_input.text()

        if self.db.connect():
            QMessageBox.information(
                self, "Exito", "Conexion exitosa a la base de datos"
            )
            self.db.disconnect()
        else:
            QMessageBox.critical(
                self, "Error", "No se pudo conectar a la base de datos"
            )

    def _guardar_config(self):
        QMessageBox.information(
            self, "Guardado", "Configuracion guardada correctamente"
        )

    def _mostrar_error(self, mensaje: str):
        QMessageBox.critical(self, "Error", mensaje)
        self._agregar_evento_historial("Error", mensaje, "error")

    def _mostrar_exito(self, mensaje: str):
        QMessageBox.information(
            self, "Exito", f"Tesis '{mensaje}' importada correctamente"
        )
        self._agregar_evento_historial("Tesis importada", mensaje, "success")

    def cerrar_sesion_accion(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

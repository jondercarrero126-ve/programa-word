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
    QLineEdit,
    QRadioButton,
    QListWidget,
    QGroupBox,
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
    categorias_changed = Signal(list)
    filtro_aplicado = Signal(str, int)

    def __init__(self, db: Database, usuario: dict):
        super().__init__()
        self.db = db
        self.usuario = usuario
        self._tesis_cache = []
        self._categorias_cache = []

    def cargar_categorias(self):
        if self.db.connect():
            try:
                categorias = self.db.fetch_all(
                    "SELECT * FROM categorias WHERE id_usuario = %s ORDER BY fecha_creacion DESC",
                    (self.usuario["id_usuario"],),
                )
                self._categorias_cache = categorias if categorias else []
                self.db.disconnect()
                self.categorias_changed.emit(self._categorias_cache)
            except Exception as e:
                self.db.disconnect()
                self.error_occurred.emit(f"Error al cargar categorías: {str(e)}")
        else:
            self.error_occurred.emit("No se pudo conectar a la base de datos")

    def crear_categoria(self, nombre: str, patron: str, tipo: str = "any"):
        if self.db.connect():
            try:
                self.db.execute(
                    """INSERT INTO categorias (nombre, patron_busqueda, tipo_busqueda, id_usuario)
                       VALUES (%s, %s, %s, %s)""",
                    (nombre, patron, tipo, self.usuario["id_usuario"]),
                )
                self.db.disconnect()
                self.cargar_categorias()
            except Exception as e:
                self.db.disconnect()
                self.error_occurred.emit(f"Error al crear categoría: {str(e)}")
        else:
            self.error_occurred.emit("No se pudo conectar a la base de datos")

    def eliminar_categoria(self, id_categoria: int):
        if self.db.connect():
            try:
                self.db.execute(
                    "DELETE FROM categorias WHERE id_categoria = %s", (id_categoria,)
                )
                self.db.disconnect()
                self.cargar_categorias()
            except Exception as e:
                self.db.disconnect()
                self.error_occurred.emit(f"Error al eliminar categoría: {str(e)}")
        else:
            self.error_occurred.emit("No se pudo conectar a la base de datos")

    def actualizar_categoria(
        self, id_categoria: int, nombre: str, patron: str, tipo: str
    ):
        if self.db.connect():
            try:
                self.db.execute(
                    """UPDATE categorias SET nombre = %s, patron_busqueda = %s, tipo_busqueda = %s
                       WHERE id_categoria = %s""",
                    (nombre, patron, tipo, id_categoria),
                )
                self.db.disconnect()
                self.cargar_categorias()
            except Exception as e:
                self.db.disconnect()
                self.error_occurred.emit(f"Error al actualizar categoría: {str(e)}")
        else:
            self.error_occurred.emit("No se pudo conectar a la base de datos")

    def aplicar_filtro_categoria(self, categoria: dict):
        patron = categoria["patron_busqueda"]
        tipo = categoria["tipo_busqueda"]

        if not patron:
            self.tesis_changed.emit(self._tesis_cache)
            self.filtro_aplicado.emit("", 0)
            return

        palabras = [p.strip() for p in patron.split() if p.strip()]

        def matches(tesis):
            texto = (
                str(tesis.get("titulo", ""))
                + " "
                + str(tesis.get("autor_principal", ""))
                + " "
                + str(tesis.get("resumen", ""))
                + " "
                + str(tesis.get("palabras_clave", ""))
            ).lower()

            if tipo == "all":
                return all(p.lower() in texto for p in palabras)
            else:
                return any(p.lower() in texto for p in palabras)

        filtradas = [t for t in self._tesis_cache if matches(t)]
        self.tesis_changed.emit(filtradas)
        self.filtro_aplicado.emit(categoria["nombre"], len(filtradas))

    def preview_filtro(self, patron: str, tipo: str = "any") -> int:
        if not patron or not self._tesis_cache:
            return len(self._tesis_cache)

        palabras = [p.strip() for p in patron.split() if p.strip()]

        def matches(tesis):
            texto = (
                str(tesis.get("titulo", ""))
                + " "
                + str(tesis.get("autor_principal", ""))
                + " "
                + str(tesis.get("resumen", ""))
                + " "
                + str(tesis.get("palabras_clave", ""))
            ).lower()

            if tipo == "all":
                return all(p.lower() in texto for p in palabras)
            else:
                return any(p.lower() in texto for p in palabras)

        return len([t for t in self._tesis_cache if matches(t)])

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
        self._filtro_activo = None

        self.setupUi(self)
        self.setWindowTitle("Gestion de Tesis")

        self.Nombres_Widget.setHidden(True)
        self.Nombre_usuarios.setText(usuario.get("nombre", "Usuario"))

        if not hasattr(self, "input_nombre_categoria"):
            self._crear_widgets_busquedas()

        self._conectar_navegacion()
        self._conectar_widgets()
        self._conectar_signals()
        self._actualizar_estadisticas()

        self.controller.cargar_tesis()
        self.controller.cargar_categorias()

    def _crear_widgets_busquedas(self):
        self.input_nombre_categoria = QLineEdit()
        self.input_nombre_categoria.setPlaceholderText("Nombre de la categoría")
        self.perfil_layout.addWidget(self.input_nombre_categoria)

        self.input_patron = QLineEdit()
        self.input_patron.setPlaceholderText(
            "Palabras a buscar (separadas por espacio)"
        )
        self.perfil_layout.addWidget(self.input_patron)

        tipo_group = QGroupBox("Tipo de búsqueda")
        tipo_layout = QHBoxLayout()
        self.radio_cualquiera = QRadioButton("Cualquiera de estas palabras (OR)")
        self.radio_cualquiera.setChecked(True)
        self.radio_todas = QRadioButton("Todas estas palabras (AND)")
        tipo_layout.addWidget(self.radio_cualquiera)
        tipo_layout.addWidget(self.radio_todas)
        tipo_group.setLayout(tipo_layout)
        self.perfil_layout.addWidget(tipo_group)

        botones_layout = QHBoxLayout()
        self.btn_crear_categoria = QPushButton("Crear Categoría")
        self.btn_preview = QPushButton("Vista Previa")
        botones_layout.addWidget(self.btn_crear_categoria)
        botones_layout.addWidget(self.btn_preview)

        botones_widget = QWidget()
        botones_widget.setLayout(botones_layout)
        self.perfil_layout.addWidget(botones_widget)

        self.lista_categorias = QListWidget()
        self.perfil_layout.addWidget(self.lista_categorias)

        acciones_layout = QHBoxLayout()
        btn_aplicar = QPushButton("Aplicar")
        btn_aplicar.clicked.connect(self._aplicar_categoria)
        btn_editar = QPushButton("Editar")
        btn_editar.clicked.connect(self._editar_categoria)
        btn_eliminar = QPushButton("Eliminar")
        btn_eliminar.clicked.connect(self._eliminar_categoria)
        acciones_layout.addWidget(btn_aplicar)
        acciones_layout.addWidget(btn_editar)
        acciones_layout.addWidget(btn_eliminar)

        acciones_widget = QWidget()
        acciones_widget.setLayout(acciones_layout)
        self.perfil_layout.addWidget(acciones_widget)

        self.label_filtro_activo = QLabel()
        self.label_filtro_activo.setStyleSheet(
            "color: #2196F3; font-weight: bold; padding: 10px;"
        )
        self.label_filtro_activo.setVisible(False)
        self.perfil_layout.addWidget(self.label_filtro_activo)

        self.btn_quitar_filtro = QPushButton("Quitar Filtro")
        self.btn_quitar_filtro.setVisible(False)
        self.btn_quitar_filtro.clicked.connect(self._quitar_filtro)
        self.perfil_layout.addWidget(self.btn_quitar_filtro)

        self._conectar_widgets_categorias()

    def _conectar_widgets_categorias(self):
        if hasattr(self, "btn_crear_categoria"):
            self.btn_crear_categoria.clicked.connect(self._crear_categoria)
            self.btn_preview.clicked.connect(self._preview_categoria)

    def _editar_categoria(self):
        current_item = self.lista_categorias.currentItem()
        if not current_item:
            QMessageBox.warning(
                self, "Advertencia", "Seleccione una categoría para editar"
            )
            return

        datos = current_item.text().split("|")
        if len(datos) >= 4:
            nombre, patron, tipo, cat_id = datos[0], datos[1], datos[2], datos[3]
            self.input_nombre_categoria.setText(nombre)
            self.input_patron.setText(patron)
            if tipo == "any":
                self.radio_cualquiera.setChecked(True)
            else:
                self.radio_todas.setChecked(True)

            self.controller.eliminar_categoria(int(cat_id))

    def _eliminar_categoria(self):
        current_item = self.lista_categorias.currentItem()
        if not current_item:
            QMessageBox.warning(
                self, "Advertencia", "Seleccione una categoría para eliminar"
            )
            return

        datos = current_item.text().split("|")
        if len(datos) >= 4:
            respuesta = QMessageBox.question(
                self,
                "Confirmar",
                "¿Está seguro de eliminar esta categoría?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if respuesta == QMessageBox.Yes:
                self.controller.eliminar_categoria(int(datos[3]))

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

    def _conectar_widgets(self):
        self.buscador_input.textChanged.connect(self.controller.buscar_tesis)
        self.btn_importar.clicked.connect(self._importar_tesis)
        self.btn_test.clicked.connect(self._probar_conexion)
        self.btn_guardar.clicked.connect(self._guardar_config)
        if hasattr(self, "btn_crear_categoria"):
            self.btn_crear_categoria.clicked.connect(self._crear_categoria)
            self.btn_preview.clicked.connect(self._preview_categoria)
            self.btn_quitar_filtro.clicked.connect(self._quitar_filtro)

    def _conectar_signals(self):
        self.controller.tesis_changed.connect(self._actualizar_tabla_tesis)
        self.controller.error_occurred.connect(self._mostrar_error)
        self.controller.import_success.connect(self._mostrar_exito)
        self.controller.import_error.connect(self._mostrar_error)
        if hasattr(self, "lista_categorias"):
            self.controller.categorias_changed.connect(
                self._actualizar_lista_categorias
            )
            self.controller.filtro_aplicado.connect(self._mostrar_filtro_activo)

    def _cambiar_pagina(self, index: int):
        self.MultiVentanas_Widget.setCurrentIndex(index)
        if index == 2:
            self._actualizar_analisis()
        elif index == 1:
            self._actualizar_lista_categorias(self.controller._categorias_cache)

    def _actualizar_estadisticas(self):
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

        self._actualizar_estadisticas()

    def _actualizar_lista_categorias(self, categorias):
        if not hasattr(self, "lista_categorias"):
            return
        self.lista_categorias.clear()
        for cat in categorias:
            item_text = f"{cat['nombre']}|{cat['patron_busqueda']}|{cat['tipo_busqueda']}|{cat['id_categoria']}"
            self.lista_categorias.addItem(item_text)

    def _mostrar_filtro_activo(self, nombre: str, cantidad: int):
        if not hasattr(self, "label_filtro_activo"):
            return
        self._filtro_activo = nombre
        if nombre:
            self.label_filtro_activo.setText(
                f"Filtrado por: {nombre} ({cantidad} resultados)"
            )
            self.btn_quitar_filtro.setVisible(True)
        else:
            self.label_filtro_activo.setText("")
            self.btn_quitar_filtro.setVisible(False)

    def _quitar_filtro(self):
        if not hasattr(self, "label_filtro_activo"):
            return
        self._filtro_activo = None
        self.buscador_input.clear()
        self.controller.buscar_tesis("")
        self._mostrar_filtro_activo("", 0)

    def _crear_categoria(self):
        if not hasattr(self, "input_nombre_categoria"):
            return
        nombre = self.input_nombre_categoria.text().strip()
        patron = self.input_patron.text().strip()
        tipo = "any" if self.radio_cualquiera.isChecked() else "all"

        if not nombre or not patron:
            QMessageBox.warning(self, "Advertencia", "Complete todos los campos")
            return

        self.controller.crear_categoria(nombre, patron, tipo)
        self.input_nombre_categoria.clear()
        self.input_patron.clear()
        self.radio_cualquiera.setChecked(True)
        QMessageBox.information(self, "Exito", "Categoria creada correctamente")

    def _preview_categoria(self):
        if not hasattr(self, "input_patron"):
            return
        patron = self.input_patron.text().strip()
        tipo = "any" if self.radio_cualquiera.isChecked() else "all"

        if not patron:
            QMessageBox.warning(self, "Advertencia", "Ingrese un patron de busqueda")
            return

        cantidad = self.controller.preview_filtro(patron, tipo)
        QMessageBox.information(
            self, "Vista Previa", f"Se encontraron {cantidad} tesis con ese filtro"
        )

    def _aplicar_categoria(self):
        if not hasattr(self, "lista_categorias"):
            return
        current_item = self.lista_categorias.currentItem()
        if not current_item:
            return

        datos = current_item.text().split("|")
        if len(datos) >= 4:
            categoria = {
                "nombre": datos[0],
                "patron_busqueda": datos[1],
                "tipo_busqueda": datos[2],
                "id_categoria": int(datos[3]),
            }
            self.controller.aplicar_filtro_categoria(categoria)
            self.buscador_input.setText(categoria["patron_busqueda"])

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

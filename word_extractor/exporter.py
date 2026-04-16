from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os


class WordExporter:
    """Exporta tesis almacenadas a documento Word (.docx).

    Es la operación inversa de WordExtractor - toma datos de la base de datos
    y genera un documento Word con estructura completa.
    """

    def __init__(self):
        self.doc = None

    def crear_documento(
        self, tesis: dict, capitulos: list, referencias: list
    ) -> Document:
        """Crea un documento Word con la estructura completa de la tesis.

        Args:
            tesis: Diccionario con datos de la tesis (titulo, autor, anio, resumen, palabras_clave, etc.)
            capitulos: Lista de diccionarios con datos de capítulos (titulo, contenido)
            referencias: Lista de diccionarios con datos de referencias (tipo, autor, titulo, anio, url)

        Returns:
            Document: Objeto Document de python-docx listo para guardar
        """
        self.doc = Document()

        # Título de la tesis
        titulo = tesis.get("titulo", "Sin título")
        titulo_paragraph = self.doc.add_heading(titulo, level=0)
        titulo_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Autor
        autor = tesis.get("autor_principal", "Autor desconocido")
        autor_paragraph = self.doc.add_paragraph(autor)
        autor_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Universidad (si existe)
        if tesis.get("universidad"):
            uni_paragraph = self.doc.add_paragraph(tesis["universidad"])
            uni_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Año
        anio = tesis.get("anio")
        if anio:
            anio_paragraph = self.doc.add_paragraph(str(anio))
            anio_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        self.doc.add_paragraph("")  # Espacio

        # Resumen
        if tesis.get("resumen"):
            self.doc.add_heading("Resumen", level=1)
            self.doc.add_paragraph(tesis["resumen"])

        # Palabras clave
        if tesis.get("palabras_clave"):
            self.doc.add_heading("Palabras Clave", level=1)
            self.doc.add_paragraph(tesis["palabras_clave"])

        # Capítulos
        if capitulos:
            self.doc.add_heading("Desarrollo", level=1)
            for i, cap in enumerate(capitulos, 1):
                cap_titulo = cap.get("titulo", f"Capítulo {i}")
                self.doc.add_heading(cap_titulo, level=2)

                contenido = cap.get("contenido", "")
                if contenido:
                    # Dividir contenido en párrafos
                    for parrafo in contenido.split("\n"):
                        if parrafo.strip():
                            self.doc.add_paragraph(parrafo)

        # Referencias
        if referencias:
            self.doc.add_heading("Referencias", level=1)
            for ref in referencias:
                ref_text = self._formatear_referencia(ref)
                self.doc.add_paragraph(ref_text, style="List Bullet")

        return self.doc

    def _formatear_referencia(self, ref: dict) -> str:
        """Formatea una referencia según su tipo.

        Args:
            ref: Diccionario con datos de la referencia

        Returns:
            str: Referencia formateada
        """
        autor = ref.get("autor", "")
        titulo = ref.get("titulo", "")
        anio = ref.get("anio")
        url = ref.get("url", "")
        tipo = ref.get("tipo", "libro")

        # Construir referencia básica
        parts = []
        if autor:
            parts.append(autor)
        if titulo:
            parts.append(titulo)
        if anio:
            parts.append(f"({anio})")

        ref_text = ". ".join(parts)

        # Agregar URL si existe
        if url:
            ref_text += f". Disponible en: {url}"

        return ref_text

    def guardar_documento(self, doc: Document, filepath: str) -> bool:
        """Guarda el documento en la ruta especificada.

        Args:
            doc: Objeto Document de python-docx
            filepath: Ruta donde se guardará el archivo

        Returns:
            bool: True si se guardó exitosamente
        """
        try:
            # Asegurar que la extensión sea .docx
            if not filepath.lower().endswith(".docx"):
                filepath += ".docx"

            doc.save(filepath)
            return True
        except Exception as e:
            print(f"Error al guardar documento: {e}")
            return False

    def exportar(
        self, tesis: dict, capitulos: list, referencias: list, filepath: str
    ) -> bool:
        """Exporta una tesis completa a documento Word.

        Es el método principal que combina crear y guardar.

        Args:
            tesis: Diccionario con datos de la tesis
            capitulos: Lista de capítulos
            referencias: Lista de referencias
            filepath: Ruta donde se guardará el archivo

        Returns:
            bool: True si la exportación fue exitosa
        """
        doc = self.crear_documento(tesis, capitulos, referencias)
        return self.guardar_documento(doc, filepath)

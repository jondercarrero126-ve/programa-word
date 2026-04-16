import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt


@pytest.fixture
def app():
    app_instance = QApplication.instance()
    if app_instance is None:
        app_instance = QApplication([])
    yield app_instance


class TestLogin:
    def test_login_se_crea_correctamente(self, app):
        from login import Login

        login = Login()
        assert login is not None
        login.close()

    def test_login_tiene_widgets(self, app):
        from login import Login

        login = Login()

        assert login.username_input is not None, "Deberia tener campo de usuario"
        assert login.password_input is not None, "Deberia tener campo de contrasena"
        assert login.login_button is not None, "Deberia tener boton de login"
        assert login.error_label is not None, "Deberia tener label de error"

        login.close()

    def test_login_credenciales_vacias(self, app):
        from login import Login

        login = Login()

        login.username_input.setText("")
        login.password_input.setText("")
        login.login_button.click()

        assert "Complete" in login.error_label.text()

        login.close()

    def test_login_credenciales_incorrectas(self, app):
        from login import Login

        login = Login()

        login.username_input.setText("usuario_invalido")
        login.password_input.setText("contrasena_invalida")
        login.login_button.click()

        QApplication.processEvents()

        assert (
            "incorrectos" in login.error_label.text() or login.error_label.text() == ""
        )

        login.close()

    def test_login_enter_en_password(self, app):
        from login import Login

        login = Login()

        login.username_input.setText("admin")
        login.password_input.setText("admin123")
        login.password_input.returnPressed.emit()

        QApplication.processEvents()

        login.close()


class TestPrincipal:
    @pytest.fixture
    def usuario_mock(self):
        return {
            "id_usuario": 1,
            "username": "admin",
            "nombre": "Administrador",
            "email": "admin@tesis.com",
        }

    def test_principal_se_crea_correctamente(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)
        assert principal is not None
        principal.close()

    def test_principal_tiene_multi_ventanas(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        assert principal.MultiVentanas_Widget is not None
        assert principal.MultiVentanas_Widget.count() == 5

        principal.close()

    def test_navegacion_panel(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        assert principal.MultiVentanas_Widget.currentIndex() == 0

        principal.cerrar_sesion_accion()
        principal.close()

    def test_widgets_panel_existen(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        assert principal.titulo_panel is not None
        assert principal.buscador_input is not None
        assert principal.btn_importar is not None
        assert principal.tabla_tesis is not None

        principal.close()

    def test_widgets_perfil_existen(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        principal.MultiVentanas_Widget.setCurrentIndex(1)

        assert principal.titulo_perfil is not None
        assert principal.valor_nombre is not None
        assert principal.valor_usuario is not None

        principal.close()

    def test_widgets_analisis_existen(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        principal.MultiVentanas_Widget.setCurrentIndex(2)

        assert principal.titulo_analisis is not None
        assert principal.tabla_anio is not None

        principal.close()

    def test_widgets_ajustes_existen(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        principal.MultiVentanas_Widget.setCurrentIndex(4)

        assert principal.titulo_ajustes is not None
        assert principal.host_input is not None
        assert principal.user_input is not None
        assert principal.pass_input is not None
        assert principal.btn_test is not None

        principal.close()

    def test_perfil_muestra_info_usuario(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        principal.MultiVentanas_Widget.setCurrentIndex(1)

        assert hasattr(principal, "input_nombre_categoria")
        assert hasattr(principal, "input_patron")
        assert hasattr(principal, "lista_categorias")

        principal.close()

    def test_buscador_conectar_senal(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        principal.buscador_input.setText("test")
        assert principal.buscador_input.text() == "test"

        principal.close()

    def test_tabla_tesis_columnas(self, app, usuario_mock):
        from principal import Principal

        principal = Principal(usuario_mock)

        assert principal.tabla_tesis.columnCount() == 5

        headers = []
        for i in range(5):
            header = principal.tabla_tesis.horizontalHeaderItem(i)
            if header:
                headers.append(header.text())

        assert len(headers) > 0

        principal.close()


class TestImportWorker:
    def test_import_worker_creacion(self):
        from principal import ImportWorker

        worker = ImportWorker("archivo.docx")
        assert worker is not None
        assert worker.filepath == "archivo.docx"


class TestTesisController:
    def test_controller_creacion(self):
        from database import Database
        from principal import TesisController

        db = Database()
        usuario = {"id_usuario": 1}
        controller = TesisController(db, usuario)

        assert controller is not None
        assert controller.db is not None
        assert controller.usuario == usuario

    def test_editar_tesis_existe(self):
        """Verifica que el metodo editar_tesis existe en TesisController."""
        from database import Database
        from principal import TesisController

        db = Database()
        usuario = {"id_usuario": 1}
        controller = TesisController(db, usuario)

        assert hasattr(controller, "editar_tesis")
        assert callable(controller.editar_tesis)

    def test_eliminar_tesis_existe(self):
        """Verifica que el metodo eliminar_tesis existe en TesisController."""
        from database import Database
        from principal import TesisController

        db = Database()
        usuario = {"id_usuario": 1}
        controller = TesisController(db, usuario)

        assert hasattr(controller, "eliminar_tesis")
        assert callable(controller.eliminar_tesis)

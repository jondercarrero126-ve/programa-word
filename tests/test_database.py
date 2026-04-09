import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Database


class TestDatabase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database(
            host="localhost", user="root", password="admin123", database="gestion_tesis"
        )
        yield
        if self.db.connection and self.db.connection.is_connected():
            self.db.disconnect()

    def test_conexion_exitosa(self):
        resultado = self.db.connect()
        assert resultado is True, "La conexion a la base de datos deberia ser exitosa"
        self.db.disconnect()

    def test_conexion_fallida_credenciales_invalidas(self):
        db_mala = Database(
            host="localhost", user="root", password="contrasena_incorrecta"
        )
        resultado = db_mala.connect()
        assert resultado is False, (
            "La conexion deberia fallar con credenciales incorrectas"
        )

    def test_conexion_fallida_host_invalido(self):
        db_mala = Database(host="host_invalido_12345", user="root", password="admin123")
        resultado = db_mala.connect()
        assert resultado is False, "La conexion deberia fallar con host invalido"

    def test_fetch_one_existe(self):
        self.db.connect()
        resultado = self.db.fetch_one(
            "SELECT * FROM usuarios WHERE username = %s", ("admin",)
        )
        assert resultado is not None, "Deberia encontrar el usuario admin"
        assert resultado["username"] == "admin"
        self.db.disconnect()

    def test_fetch_one_no_existe(self):
        self.db.connect()
        resultado = self.db.fetch_one(
            "SELECT * FROM usuarios WHERE username = %s", ("usuario_inexistente_xyz",)
        )
        assert resultado is None, "No deberia encontrar un usuario inexistente"
        self.db.disconnect()

    def test_fetch_all(self):
        self.db.connect()
        resultado = self.db.fetch_all("SELECT * FROM tesis")
        assert isinstance(resultado, list), "El resultado deberia ser una lista"
        self.db.disconnect()

    def test_execute_insert_y_select(self):
        self.db.connect()
        cursor = self.db.execute(
            "INSERT INTO tesis (titulo, autor_principal, id_usuario, estado) VALUES (%s, %s, %s, %s)",
            ("Test Tesis", "Test Autor", 1, "borrador"),
        )
        assert cursor is not None, "El insert deberia ejecutarse correctamente"

        resultado = self.db.fetch_one(
            "SELECT * FROM tesis WHERE titulo = %s", ("Test Tesis",)
        )
        assert resultado is not None, "Deberia encontrar la tesis insertada"

        self.db.execute("DELETE FROM tesis WHERE titulo = %s", ("Test Tesis",))
        self.db.disconnect()

    def test_disconnect_sin_conexion(self):
        db_nueva = Database()
        db_nueva.disconnect()

    def test_hash_password(self):
        hash1 = Database.hash_password("admin123")
        hash2 = Database.hash_password("admin123")
        assert hash1 == hash2, "El mismo password deberia generar el mismo hash"

        hash3 = Database.hash_password("otra_password")
        assert hash1 != hash3, "Passwords diferentes deberian generar hashes diferentes"

    def test_verify_password(self):
        password = "admin123"
        hash_correcto = Database.hash_password(password)
        hash_incorrecto = Database.hash_password("wrong")

        assert self.db.verify_password(password, hash_correcto) is True
        assert self.db.verify_password(password, hash_incorrecto) is False

    def test_execute_con_rollback(self):
        self.db.connect()
        cursor = self.db.execute("SELECT * FROM tabla_inexistente_xyz")
        assert cursor is None, "Deberia retornar None para consultas invalidas"
        self.db.disconnect()

    def test_fetch_all_sin_conexion(self):
        resultado = self.db.fetch_all("SELECT * FROM tesis")
        assert resultado is None, "Deberia retornar None sin conexion"

    def test_fetch_one_sin_conexion(self):
        resultado = self.db.fetch_one("SELECT * FROM tesis")
        assert resultado is None, "Deberia retornar None sin conexion"


class TestDatabaseTablas:
    def test_existen_todas_las_tablas(self):
        db = Database(
            host="localhost", user="root", password="admin123", database="gestion_tesis"
        )
        db.connect()

        cursor = db.connection.cursor()
        cursor.execute("SHOW TABLES")
        tablas = [t[0] for t in cursor.fetchall()]
        cursor.close()
        db.disconnect()

        assert "usuarios" in tablas, "Tabla 'usuarios' deberia existir"
        assert "tesis" in tablas, "Tabla 'tesis' deberia existir"
        assert "capitulos" in tablas, "Tabla 'capitulos' deberia existir"
        assert "referencias" in tablas, "Tabla 'referencias' deberia existir"

    def test_usuario_admin_existe(self):
        db = Database()
        db.connect()
        resultado = db.fetch_one("SELECT * FROM usuarios WHERE username = 'admin'")
        db.disconnect()

        assert resultado is not None, "El usuario admin deberia existir"
        assert resultado["username"] == "admin"

    def test_estructura_tesis(self):
        db = Database()
        db.connect()
        cursor = db.connection.cursor()
        cursor.execute("DESCRIBE tesis")
        columnas = [col[0] for col in cursor.fetchall()]
        cursor.close()
        db.disconnect()

        assert "id_tesis" in columnas
        assert "titulo" in columnas
        assert "autor_principal" in columnas
        assert "anio" in columnas
        assert "estado" in columnas

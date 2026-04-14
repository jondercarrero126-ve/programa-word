import pytest
import sys
import os
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Database


class TestDatabase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db_file = tempfile.mktemp(suffix=".db")
        self.db = Database(self.db_file)
        yield
        if self.db.connection:
            self.db.disconnect()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_conexion_exitosa(self):
        resultado = self.db.connect()
        assert resultado is True, "La conexion deberia ser exitosa"
        self.db.disconnect()

    def test_conexion_fallida_archivo_invalido(self):
        db_mala = Database("test.db")
        db_mala.database = "/ruta/inexistente/test.db"
        resultado = db_mala.connect()
        assert resultado is False, "La conexion deberia fallar con archivo invalido"

    def test_fetch_one_existe(self):
        self.db.connect()
        self.db.execute(
            "INSERT INTO usuarios (username, password_hash, nombre) VALUES (?, ?, ?)",
            ("testuser", "hash123", "Test User"),
        )
        resultado = self.db.fetch_one(
            "SELECT * FROM usuarios WHERE username = ?", ("testuser",)
        )
        assert resultado is not None, "El usuario deberia existir"
        assert resultado["username"] == "testuser"
        self.db.disconnect()

    def test_fetch_one_no_existe(self):
        self.db.connect()
        resultado = self.db.fetch_one(
            "SELECT * FROM usuarios WHERE username = ?", ("noexiste",)
        )
        assert resultado is None, "No deberia encontrar el usuario"
        self.db.disconnect()

    def test_fetch_all(self):
        self.db.connect()
        self.db.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
            ("user1", "hash1"),
        )
        self.db.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
            ("user2", "hash2"),
        )
        resultados = self.db.fetch_all("SELECT * FROM usuarios")
        assert len(resultados) >= 2, "Deberia haber al menos 2 usuarios"
        self.db.disconnect()

    def test_execute_insert_y_select(self):
        self.db.connect()
        self.db.execute(
            "INSERT INTO tesis (titulo, autor_principal, anio) VALUES (?, ?, ?)",
            ("Test Tesis", "Autor Test", 2024),
        )
        resultado = self.db.fetch_one(
            "SELECT * FROM tesis WHERE titulo = ?", ("Test Tesis",)
        )
        assert resultado is not None, "La tesis deberia existir"
        assert resultado["titulo"] == "Test Tesis"
        self.db.disconnect()

    def test_disconnect_sin_conexion(self):
        db_nueva = Database(self.db_file)
        db_nueva.disconnect()

    def test_hash_password(self):
        hashed = Database.hash_password("admin123")
        assert hashed == Database.hash_password("admin123")
        assert len(hashed) == 64

    def test_verify_password(self):
        password = "admin123"
        hashed = Database.hash_password(password)
        assert self.db.verify_password(password, hashed) is True
        assert self.db.verify_password("wrong", hashed) is False

    def test_execute_con_rollback(self):
        self.db.connect()
        self.db.execute("INSERT INTO usuarios (username) VALUES (?)", ("userdup",))
        resultado = self.db.execute(
            "SELECT * FROM usuarios WHERE username = ?", ("userdup",)
        )
        self.db.disconnect()

    def test_fetch_one_no_existe(self):
        self.db.connect()
        resultado = self.db.fetch_one(
            "SELECT * FROM usuarios WHERE username = ?", ("noexiste",)
        )
        assert resultado is None, "No deberia encontrar el usuario"
        self.db.disconnect()

    def test_fetch_all(self):
        self.db.connect()
        self.db.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
            ("user1", "hash1"),
        )
        self.db.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
            ("user2", "hash2"),
        )
        resultados = self.db.fetch_all("SELECT * FROM usuarios")
        assert len(resultados) >= 2, "Deberia haber al menos 2 usuarios"
        self.db.disconnect()

    def test_execute_insert_y_select(self):
        self.db.connect()
        self.db.execute(
            "INSERT INTO tesis (titulo, autor_principal, anio) VALUES (?, ?, ?)",
            ("Test Tesis", "Autor Test", 2024),
        )
        resultado = self.db.fetch_one(
            "SELECT * FROM tesis WHERE titulo = ?", ("Test Tesis",)
        )
        assert resultado is not None, "La tesis deberia existir"
        assert resultado["titulo"] == "Test Tesis"
        self.db.disconnect()

    def test_disconnect_sin_conexion(self):
        db_nueva = Database(self.db_file)
        db_nueva.disconnect()

    def test_hash_password(self):
        hashed = Database.hash_password("test123")
        assert hashed == "ecd71870dace771f6d4cfe3fc3e00b3a1ad04e2ade46a7027b1c0db"

    def test_verify_password(self):
        password = "admin123"
        hashed = Database.hash_password(password)
        assert self.db.verify_password(password, hashed) is True
        assert self.db.verify_password("wrong", hashed) is False

    def test_execute_con_rollback(self):
        self.db.connect()
        self.db.execute("INSERT INTO usuarios (username) VALUES (?)", ("userdup",))
        resultado = self.db.execute(
            "SELECT * FROM usuarios WHERE username = ?", ("userdup",)
        )
        self.db.disconnect()


class TestDatabaseTablas:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db_file = tempfile.mktemp(suffix=".db")
        self.db = Database(self.db_file)
        self.db.connect()
        yield
        self.db.disconnect()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_existen_todas_las_tablas(self):
        self.db.connect()
        resultado = self.db.fetch_all(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        nombres = [r["name"] for r in resultado]
        assert "usuarios" in nombres
        assert "tesis" in nombres
        assert "capitulos" in nombres
        assert "referencias" in nombres
        assert "categorias" in nombres

    def test_estructura_tesis(self):
        self.db.connect()
        resultado = self.db.fetch_all("PRAGMA table_info(tesis)")
        columnas = [r["name"] for r in resultado]
        assert "id_tesis" in columnas
        assert "titulo" in columnas
        assert "autor_principal" in columnas
        assert "estado" in columnas

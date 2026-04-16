import sqlite3
import hashlib
import os


class Database:
    def __init__(self, database="tesis.db"):
        self.database = database
        self.connection = None
        self._verificar_y_crear_bd()

    def _verificar_y_crear_bd(self):
        if not os.path.exists(self.database):
            self._crear_esquema()

    def _crear_esquema(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                nombre TEXT,
                email TEXT,
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tesis (
                id_tesis INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor_principal TEXT,
                coautores TEXT,
                universidad TEXT,
                anio INTEGER,
                resumen TEXT,
                palabras_clave TEXT,
                estado TEXT DEFAULT 'borrador',
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_usuario INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS capitulos (
                id_capitulo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tesis INTEGER,
                numero_capitulo INTEGER,
                titulo TEXT,
                contenido TEXT,
                orden INTEGER,
                FOREIGN KEY (id_tesis) REFERENCES tesis(id_tesis) ON DELETE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS referencias (
                id_referencia INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tesis INTEGER,
                tipo TEXT NOT NULL,
                autor TEXT,
                titulo TEXT,
                anio INTEGER,
                fuente TEXT,
                url TEXT,
                FOREIGN KEY (id_tesis) REFERENCES tesis(id_tesis) ON DELETE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                patron_busqueda TEXT NOT NULL,
                tipo_busqueda TEXT DEFAULT 'any',
                id_usuario INTEGER,
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            )
        """)

        password_hash = hashlib.sha256("admin123".encode()).hexdigest()
        cursor.execute(
            "INSERT OR IGNORE INTO usuarios (username, password_hash, nombre, email) VALUES (?, ?, ?, ?)",
            ("admin", password_hash, "Administrador", "admin@tesis.com"),
        )

        conn.commit()
        conn.close()

    def connect(self):
        try:
            db_path = os.path.abspath(self.database)
            self.connection = sqlite3.connect(db_path)
            return True
        except Exception as e:
            print(f"Error de conexion: {e}")
            self.connection = None
            return False

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except Exception as e:
            print(f"Error en consulta: {e}")
            self.connection.rollback()
            return None
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        if self.connection is None:
            return None
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            columns = (
                [description[0] for description in cursor.description]
                if cursor.description
                else []
            )
            if columns:
                return [dict(zip(columns, row)) for row in rows]
            return rows
        except Exception as e:
            print(f"Error en consulta: {e}")
            return None
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        if self.connection is None:
            return None
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            row = cursor.fetchone()
            if row:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, row))
            return None
        except Exception as e:
            print(f"Error en consulta: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password, stored_hash):
        return self.hash_password(password) == stored_hash

    # Métodos de estadísticas para gráficos
    def get_tesis_por_estado(self):
        """Obtiene la cantidad de tesis agrupadas por estado.

        Returns:
            list: Lista de diccionarios con 'estado' y 'cantidad'
        """
        if self.connection is None:
            return []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                SELECT estado, COUNT(*) as cantidad 
                FROM tesis 
                GROUP BY estado
                ORDER BY cantidad DESC
            """)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            print(f"Error en consulta: {e}")
            return []
        finally:
            cursor.close()

    def get_tesis_por_autor(self, limite=10):
        """Obtiene los autores con más tesis.

        Args:
            limite: Número máximo de autores a devolver (default 10)

        Returns:
            list: Lista de diccionarios con 'autor_principal' y 'cantidad'
        """
        if self.connection is None:
            return []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
                SELECT autor_principal, COUNT(*) as cantidad 
                FROM tesis 
                WHERE autor_principal IS NOT NULL AND autor_principal != ''
                GROUP BY autor_principal
                ORDER BY cantidad DESC
                LIMIT ?
            """,
                (limite,),
            )
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            print(f"Error en consulta: {e}")
            return []
        finally:
            cursor.close()


db = Database()

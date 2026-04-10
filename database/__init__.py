import sqlite3
import hashlib
import os


class Database:
    def __init__(self, database="tesis.db"):
        self.database = database
        self.connection = None

    def connect(self):
        try:
            db_path = os.path.abspath(self.database)
            self.connection = sqlite3.connect(db_path)
            return True
        except Exception as e:
            print(f"Error de conexión: {e}")
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


db = Database()

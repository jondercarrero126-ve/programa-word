import mysql.connector
from mysql.connector import Error
import hashlib
import os


class Database:
    def __init__(
        self,
        host="localhost",
        user="root",
        password="admin123",
        database="gestion_tesis",
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            return True
        except (Error, RuntimeError, Exception) as e:
            print(f"Error de conexión: {e}")
            self.connection = None
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Error en consulta: {e}")
            self.connection.rollback()
            return None
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        if self.connection is None:
            return None
        cursor = self.connection.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error en consulta: {e}")
            return None
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        if self.connection is None:
            return None
        cursor = self.connection.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        except Error as e:
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

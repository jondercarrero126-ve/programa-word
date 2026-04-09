import hashlib
import mysql.connector
from mysql.connector import Error


def crear_base_datos():
    host = "localhost"
    user = "root"
    password = "admin123"

    try:
        print(f"Conectando a MariaDB en {host}...")
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()

        print("Creando base de datos 'gestion_tesis'...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS gestion_tesis")
        cursor.execute("USE gestion_tesis")

        print("Creando tabla 'usuarios'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                nombre VARCHAR(100),
                email VARCHAR(100),
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        print("Creando tabla 'tesis'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tesis (
                id_tesis INT PRIMARY KEY AUTO_INCREMENT,
                titulo VARCHAR(500) NOT NULL,
                autor_principal VARCHAR(200),
                coautores TEXT,
                universidad VARCHAR(200),
                anio YEAR,
                resumen TEXT,
                palabras_clave VARCHAR(500),
                estado ENUM('borrador', 'completada', 'publicada') DEFAULT 'borrador',
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion DATETIME ON UPDATE CURRENT_TIMESTAMP,
                id_usuario INT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE SET NULL
            )
        """)

        print("Creando tabla 'capitulos'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS capitulos (
                id_capitulo INT PRIMARY KEY AUTO_INCREMENT,
                id_tesis INT,
                numero_capitulo INT,
                titulo VARCHAR(300),
                contenido TEXT,
                orden INT,
                FOREIGN KEY (id_tesis) REFERENCES tesis(id_tesis) ON DELETE CASCADE
            )
        """)

        print("Creando tabla 'referencias'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS referencias (
                id_referencia INT PRIMARY KEY AUTO_INCREMENT,
                id_tesis INT,
                tipo ENUM('libro', 'articulo', 'web', 'tesis') NOT NULL,
                autor VARCHAR(300),
                titulo VARCHAR(500),
                anio YEAR,
                fuente VARCHAR(500),
                url VARCHAR(500),
                FOREIGN KEY (id_tesis) REFERENCES tesis(id_tesis) ON DELETE CASCADE
            )
        """)

        password_hash = hashlib.sha256("admin123".encode()).hexdigest()
        cursor.execute(
            """
            INSERT INTO usuarios (username, password_hash, nombre, email)
            VALUES ('admin', %s, 'Administrador', 'admin@tesis.com')
            ON DUPLICATE KEY UPDATE password_hash = %s
        """,
            (password_hash, password_hash),
        )

        conn.commit()
        print("\n¡Base de datos creada exitosamente!")
        print("Usuario: admin")
        print("Contraseña: admin123")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    crear_base_datos()

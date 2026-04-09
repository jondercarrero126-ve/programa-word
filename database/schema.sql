-- Base de datos para Gestión de Tesis
-- Ejecutar este script en MariaDB

CREATE DATABASE IF NOT EXISTS gestion_tesis;
USE gestion_tesis;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre VARCHAR(100),
    email VARCHAR(100),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de tesis
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
);

-- Tabla de capítulos
CREATE TABLE IF NOT EXISTS capitulos (
    id_capitulo INT PRIMARY KEY AUTO_INCREMENT,
    id_tesis INT,
    numero_capitulo INT,
    titulo VARCHAR(300),
    contenido TEXT,
    orden INT,
    FOREIGN KEY (id_tesis) REFERENCES tesis(id_tesis) ON DELETE CASCADE
);

-- Tabla de referencias
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
);

-- Insertar usuario admin por defecto (contraseña: admin123)
INSERT INTO usuarios (username, password_hash, nombre, email)
VALUES ('admin', 'pbkdf2:sha256:600000$salt$hash', 'Administrador', 'admin@tesis.com');

-- Actualizar con hash real (se hará desde Python)
UPDATE usuarios SET password_hash = 'admin123' WHERE username = 'admin';

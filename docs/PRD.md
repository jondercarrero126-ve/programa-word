# PRD - Sistema de Gestión de Tesis

## 1. Información General

| Campo | Valor |
|-------|-------|
| **Nombre del Proyecto** | Sistema de Gestión de Tesis |
| **Versión** | 1.1 |
| **Fecha de Creación** | 09/04/2026 |
| **Última Actualización** | 16/04/2026 |
| **Tecnología Principal** | Python + PySide6 + SQLite |
| **Tipo de Usuario** | SINGLE-USER (único usuario, sin registro) |
| **Estado** | Funcional - En pruebas |

---

## 2. Descripción del Producto

Sistema de gestión de tesis que permite importar documentos Word, extraer automáticamente su contenido (título, autor, capítulos, referencias) y almacenarlos en una base de datos SQLite para su organización y consulta. Aplicación para UNICO USUARIO.

---

## 3. Stakeholders

| Rol | Descripción |
|-----|-------------|
| **Usuario Final** | Investigadores, estudiantes, académicos |
| **Desarrollador** | Responsable del mantenimiento y mejoras |

---

## 4. Funcionalidades

### 4.1 Funcionalidades Implementadas

| # | Funcionalidad | Prioridad | Estado |
|---|---------------|-----------|--------|
| 1 | Login con usuario/contraseña | Alta | Implementado |
| 2 | Panel principal con lista de tesis | Alta | Implementado |
| 3 | Importar tesis desde archivo Word (.docx) | Alta | Implementado |
| 4 | Extracción automática de datos (título, autor, resumen) | Alta | Implementado |
| 5 | Extracción de capítulos | Media | Implementado |
| 6 | Extracción de referencias bibliográficas | Media | Implementado |
| 7 | Búsqueda de tesis por título/autor | Alta | Implementado |
| 8 | Perfil de usuario con estadísticas | Baja | Implementado |
| 9 | Panel de análisis de datos | Baja | Implementado |
| 10 | Historial de actividad | Baja | Implementado |
| 11 | Configuración de conexión a BD | Alta | Implementado |

### 4.2 Funcionalidades Pendientes (Actualizado 16/04/2026)

| # | Funcionalidad | Prioridad | Fase |
|---|---------------|-----------|------|
| 1 | Editar tesis importada | Alta | 1 |
| 2 | Eliminar tesis | Alta | 1 |
| 3 | Exportar tesis a Word/PDF | Media | 2 |
| 4 | Gráficos de análisis reales | Media | 2 |
| 5 | Tema oscuro/claro | Baja | 3 |

**REMOVIDOS (single-user, no necesario):**
- Registrar nuevos usuarios
- Cambiar contraseña

---

## 5. Arquitectura del Sistema

### 5.1 Diagrama de Componentes

```
+-------------------------------------------------------------+
|                        FRONTEND (PySide6)                    |
|  +---------+ +---------+ +---------+ +---------+          |
|  |  Login  | |  Panel  | | Perfil  | |Analisis|          |
|  +----+----+ +----+----+ +----+----+ +----+----+          |
|       |           |           |           |                 |
|       +-----------+-----------+-----------+                 |
|                         |                                  |
|                   TesisController                           |
|                   (Signal/Slot MVC)                         |
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                     BACKEND (Python)                         |
|  +--------------+  +----------------+  +---------------+    |
|  |   Database   |  | WordExtractor  |  | ImportWorker  |    |
|  |  (SQLite)   |  |  (python-docx) |  |   (QThread)  |    |
|  +--------------+  +----------------+  +---------------+    |
+-------------------------------------------------------------+
```

### 5.2 Estructura de Archivos

```
Proyecto python/
|
+-- main.py                    # Punto de entrada
+-- login.py                   # Ventana de login
+-- principal.py               # Ventana principal (View + Controller)
+-- ui_principal.py           # Interfaz generada (NO EDITAR)
+-- ui_login.py               # Interfaz login generada (NO EDITAR)
+-- recursos_rc.py            # Recursos compilados (NO EDITAR)
+-- init_database.py          # Script de inicializacion BD
+-- test_completo.py          # Script de pruebas
+-- PRD.md                    # Este documento
|
+-- database/
|   +-- __init__.py          # Clase Database (Modelo)
|   +-- schema.sql           # Script SQL de referencia
|
+-- word_extractor/
|   +-- __init__.py
|   +-- extractor.py          # Clase WordExtractor
|
+-- UI/
|   +-- principal.ui          # Diseno Qt Designer (EDITAR AQUI)
|   +-- login.ui             # Diseno login
|   +-- recursos.qrc         # Recursos Qt
|   +-- recursos_rc.py       # Recursos compilados
|   +-- Iconos/              # Iconos de la aplicacion
```

---

## 6. Base de Datos

### 6.1 Diagrama Entidad-Relacion

```
+-------------+         +--------------+        +-------------+
|   usuarios  | 1---N  |    tesis     | 1---N  |  capitulos  |
+-------------+         +--------------+        +-------------+
| id_usuario  |-------->| id_tesis     |<-------| id_capitulo |
| username    |         | titulo       |        | numero      |
| password    |         | autor        |        | titulo      |
| nombre      |         | universidad  |        | contenido   |
| email       |         | resumen      |        +-------------+
+-------------+         | anio         |
                        | estado       |         +-------------+
                        | fecha_creacion| 1---N  | referencias |
                        +--------------+-------->|+-------------+
                                                  | id_referencia|
                                                  | tipo        |
                                                  | autor       |
                                                  | titulo      |
                                                  | anio        |
                                                  | url         |
                                                  +-------------+
```

### 6.2 Tablas

| Tabla | Campos | Relaciones |
|-------|--------|------------|
| `usuarios` | id_usuario, username, password_hash, nombre, email, fecha_creacion | 1:N con tesis |
| `tesis` | id_tesis, titulo, autor_principal, coautores, universidad, anio, resumen, palabras_clave, estado, fecha_creacion, id_usuario | 1:N con capitulos, referencias |
| `capitulos` | id_capitulo, id_tesis, numero_capitulo, titulo, contenido, orden | N:1 con tesis |
| `referencias` | id_referencia, id_tesis, tipo, autor, titulo, anio, fuente, url | N:1 con tesis |

---

## 7. Interfaz de Usuario

### 7.1 Pantallas

| Pantalla | Descripcion | Widgets Principales |
|----------|-------------|---------------------|
| Login | Autenticacion de usuario | username_input, password_input, login_button |
| Panel | Lista de tesis, busqueda, importar | buscador_input, btn_importar, tabla_tesis |
| Perfil | Info del usuario, estadisticas | avatar, info_labels, stats_labels |
| Analisis | Estadisticas generales | resumen_group, tabla_anio, estado_labels |
| Noticias | Historial de actividad | scroll, historial_layout |
| Ajustes | Configuracion BD | host_input, user_input, pass_input, btn_test |

### 7.2 Navegacion

```
+------------------------------------------------------+
|  +----+ +--------+                                   |
|  |Avatar| | Administrador |                        |
|  +----+ +--------+                                   |
|  +------+ +----+ +----+ +----+ +----+ +------+      |
|  |Panel | |Perfil| |Anal| |Noti| |Ajust| |Cerrar|      |
|  +------+ +----+ +----+ +----+ +----+ +------+      |
+------------------------------------------------------+
```

---

## 8. Requisitos Tecnicos

### 8.1 Dependencias

| Paquete | Version | Proposito |
|---------|---------|-----------|
| PySide6 | latest | Framework GUI |
| sqlite3 | (built-in) | Base de datos SQLite |
| python-docx | latest | Extraccion de Word |

### 8.2 Requisitos del Sistema

- Windows 10/11
- Python 3.8+
- No requiere servidor de base de datos (SQLite local)
- 4GB RAM minimo

---

## 9. Credenciales

| Campo | Valor |
|-------|-------|
| **Usuario BD** | root |
| **Contrasena BD** | admin123 |
| **Base de Datos** | gestion_tesis |
| **Usuario App** | admin |
| **Contrasena App** | admin123 |

---

## 10. Roadmap (Actualizado 16/04/2026)

### Fase 1: CRUD Tesis (Q2 2026) — PRIORIDAD ALTA
- [ ] Editar tesis importada
- [ ] Eliminar tesis

### Fase 2: Export y Análisis (Q3 2026) — PRIORIDAD MEDIA
- [ ] Exportar tesis a Word/PDF
- [ ] Gráficos reales de estadísticas

### Fase 3: UI/Theme (Q4 2026) — PRIORIDAD BAJA
- [ ] Tema oscuro/claro
- [ ] Aplicacion movil (futuro)
- [ ] Sincronizacion en la nube (futuro)

---

## 11. Known Issues / Limitaciones

| # | Issue | Solucion/Workaround |
|---|-------|---------------------|
| 1 | El extractor no detecta capitulos sin estilos de Heading | Mejorar regex en extractor.py |
| 2 | Ano no se extrae del documento | Anadir mas patrones de busqueda |
| 3 | No hay validacion de formato de referencias | Mejorar parser de referencias |

---

## 12. Pruebas Realizadas

### 12.1 Resultado de Pruebas (09/04/2026)

| # | Prueba | Estado |
|---|--------|--------|
| 1 | Librerias instaladas (PySide6, docx) | PASS |
| 2 | Conexion a SQLite | PASS |
| 3 | Estructura de base de datos (5 tablas) | PASS |
| 4 | Usuario admin en base de datos | PASS |
| 5 | Login con credenciales correctas | PASS |
| 6 | Login con credenciales incorrectas | PASS |
| 7 | Archivo Word de tesis existe | PASS |
| 8 | Extractor de Word | PASS |
| 9 | Importar modulo principal | PASS |
| 10 | Importar modulo login | PASS |
| 11 | Crear widgets Qt | PASS |
| 12 | Operaciones CRUD basicas | PASS |

**Resultado: 12/12 PRUEBAS PASARON**

---

## 13. Glosario

| Termino | Definicion |
|---------|------------|
| PRD | Product Requirements Document - Documento de Requisitos del Producto |
| MVC | Modelo-Vista-Controlador - Patron de diseno de software |
| Signal/Slot | Mecanismo de comunicacion en Qt para eventos |
| QThread | Clase de PySide6 para ejecutar operaciones en segundo plano |
| QSS | Qt Style Sheets - Hojas de estilo para aplicaciones Qt |
| CRUD | Create, Read, Update, Delete - Operaciones basicas de base de datos |
| SQLite | Sistema de base de datos local embebido |

---

*Documento creado el 09/04/2026*
*Ultima actualizacion: 16/04/2026*

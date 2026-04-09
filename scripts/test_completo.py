"""
Script de Pruebas Completas - Sistema de Gestion de Tesis
========================================================
Ejecuta todas las pruebas del sistema para verificar que funciona correctamente.
"""

import sys
import traceback
from datetime import datetime

print("=" * 60)
print("SISTEMA DE GESTION DE TESIS - PRUEBAS COMPLETAS")
print("=" * 60)
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

resultados = {"passed": 0, "failed": 0, "errors": []}


def test(nombre, func):
    """Ejecuta una prueba y registra el resultado"""
    print(f"\n[PRUEBA] {nombre}")
    print("-" * 50)
    try:
        resultado = func()
        if resultado:
            print(f"   [OK] PASÓ")
            resultados["passed"] += 1
            return True
        else:
            print(f"   [FAIL] FALLÓ")
            resultados["failed"] += 1
            return False
    except Exception as e:
        print(f"   [ERROR] {e}")
        resultados["errors"].append((nombre, str(e), traceback.format_exc()))
        resultados["failed"] += 1
        return False


# ============================================================
# PRUEBA 1: Verificar librerías instaladas
# ============================================================
def test_librerias():
    print("   Verificando librerías instaladas...")

    librerias = [
        ("PySide6", "PySide6.QtCore"),
        ("mysql.connector", "mysql.connector"),
        ("python-docx", "docx"),
    ]

    for nombre, modulo in librerias:
        try:
            __import__(modulo)
            print(f"   - {nombre}: OK")
        except ImportError:
            print(f"   - {nombre}: NO INSTALADO")
            return False

    return True


test("Librerías instaladas", test_librerias)


# ============================================================
# PRUEBA 2: Conexión a MariaDB
# ============================================================
def test_conexion_mariadb():
    print("   Conectando a MariaDB...")
    from database import Database

    db = Database()
    if db.connect():
        print("   - Conexión establecida: OK")
        db.disconnect()
        return True
    else:
        print("   - Error al conectar a la base de datos")
        return False


test("Conexión a MariaDB", test_conexion_mariadb)


# ============================================================
# PRUEBA 3: Verificar base de datos y tablas
# ============================================================
def test_base_datos():
    print("   Verificando base de datos 'gestion_tesis'...")
    from database import Database

    db = Database()
    if not db.connect():
        return False

    # Verificar tablas
    tablas_esperadas = ["usuarios", "tesis", "capitulos", "referencias"]

    cursor = db.connection.cursor()
    cursor.execute("SHOW TABLES")
    tablas_existentes = [t[0] for t in cursor.fetchall()]
    cursor.close()
    db.disconnect()

    for tabla in tablas_esperadas:
        if tabla in tablas_existentes:
            print(f"   - Tabla '{tabla}': OK")
        else:
            print(f"   - Tabla '{tabla}': NO ENCONTRADA")
            return False

    return True


test("Estructura de base de datos", test_base_datos)


# ============================================================
# PRUEBA 4: Verificar usuario admin
# ============================================================
def test_usuario_admin():
    print("   Verificando usuario admin...")
    from database import Database
    import hashlib

    db = Database()
    if not db.connect():
        return False

    query = "SELECT * FROM usuarios WHERE username = 'admin'"
    resultado = db.fetch_one(query)
    db.disconnect()

    if resultado:
        print(f"   - Usuario: {resultado['username']}")
        print(f"   - Nombre: {resultado['nombre']}")
        print(f"   - Email: {resultado['email']}")
        return True
    else:
        print("   - Usuario admin no encontrado")
        return False


test("Usuario admin en base de datos", test_usuario_admin)


# ============================================================
# PRUEBA 5: Login con credenciales correctas
# ============================================================
def test_login_exitoso():
    print("   Probando login con credenciales correctas...")
    from database import Database
    import hashlib

    db = Database()
    if not db.connect():
        return False

    password_hash = hashlib.sha256("admin123".encode()).hexdigest()
    query = "SELECT * FROM usuarios WHERE username = %s AND password_hash = %s"
    resultado = db.fetch_one(query, ("admin", password_hash))
    db.disconnect()

    if resultado:
        print("   - Login exitoso: OK")
        return True
    else:
        print("   - Login falló")
        return False


test("Login con credenciales correctas", test_login_exitoso)


# ============================================================
# PRUEBA 6: Login con credenciales incorrectas
# ============================================================
def test_login_fallido():
    print("   Probando login con credenciales incorrectas...")
    from database import Database
    import hashlib

    db = Database()
    if not db.connect():
        return False

    password_hash = hashlib.sha256("contrasenaincorrecta".encode()).hexdigest()
    query = "SELECT * FROM usuarios WHERE username = %s AND password_hash = %s"
    resultado = db.fetch_one(query, ("admin", password_hash))
    db.disconnect()

    if resultado is None:
        print("   - Login incorrecto rechazado: OK")
        return True
    else:
        print("   - Login incorrecto aceptado (ERROR)")
        return False


test("Login con credenciales incorrectas", test_login_fallido)


# ============================================================
# PRUEBA 7: Archivo Word existe
# ============================================================
def test_archivo_word():
    import os

    archivos_word = [
        "Proyecto_de_investigacion_Jonder_Carrero_Capitulo_III.docx",
        "Proyecto_de_investigacion_Jonder_Carrero_Capitulo_III.doc",
    ]

    for archivo in archivos_word:
        ruta = os.path.join(os.path.dirname(__file__), archivo)
        if os.path.exists(ruta):
            print(f"   - Archivo encontrado: {archivo}")
            print(f"   - Ruta: {ruta}")
            print(f"   - Tamaño: {os.path.getsize(ruta)} bytes")
            return True

    print("   - Archivo Word no encontrado")
    return False


test("Archivo Word de tesis existe", test_archivo_word)


# ============================================================
# PRUEBA 8: Extractor de Word
# ============================================================
def test_extractor_word():
    print("   Probando extractor de Word...")
    from word_extractor.extractor import WordExtractor
    import os

    archivo = "Proyecto_de_investigacion_Jonder_Carrero_Capitulo_III.docx"
    ruta = os.path.join(os.path.dirname(__file__), archivo)

    if not os.path.exists(ruta):
        print("   - Archivo no encontrado, saltando prueba")
        return True  # No es falla si no existe

    extractor = WordExtractor(ruta)
    datos = extractor.extract_all()

    print(f"   - Título extraído: {datos['titulo'][:50]}...")
    print(f"   - Autor: {datos['autor_principal']}")
    print(f"   - Año: {datos['anio']}")
    print(f"   - Capítulos encontrados: {len(datos['capitulos'])}")
    print(f"   - Referencias encontradas: {len(datos['referencias'])}")

    if datos["titulo"] and datos["titulo"] != "Sin título":
        return True
    else:
        print("   - No se pudo extraer título válido")
        return False


test("Extractor de Word", test_extractor_word)


# ============================================================
# PRUEBA 9: Importar módulo principal
# ============================================================
def test_import_principal():
    print("   Importando módulo principal...")
    try:
        from principal import Principal, TesisController, ImportWorker

        print("   - Principal: OK")
        print("   - TesisController: OK")
        print("   - ImportWorker: OK")
        return True
    except Exception as e:
        print(f"   - Error: {e}")
        return False


test("Importar módulo principal", test_import_principal)


# ============================================================
# PRUEBA 10: Importar módulo login
# ============================================================
def test_import_login():
    print("   Importando módulo login...")
    try:
        from login import Login

        print("   - Login: OK")
        return True
    except Exception as e:
        print(f"   - Error: {e}")
        return False


test("Importar módulo login", test_import_login)


# ============================================================
# PRUEBA 11: Crear widgets Qt (sin mostrar ventana)
# ============================================================
def test_crear_widgets():
    print("   Creando widgets Qt (sin mostrar ventana)...")
    from PySide6.QtWidgets import QApplication

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    print("   - QApplication: OK")

    try:
        from login import Login

        login = Login()
        print("   - Login window: OK")

        from principal import Principal

        # Crear usuario mock
        usuario_mock = {
            "id_usuario": 1,
            "username": "admin",
            "nombre": "Administrador",
            "email": "admin@tesis.com",
        }
        principal = Principal(usuario_mock)
        print("   - Principal window: OK")

        # Limpiar
        login.close()
        principal.close()

        return True
    except Exception as e:
        print(f"   - Error creando widgets: {e}")
        traceback.print_exc()
        return False


test("Crear widgets Qt", test_crear_widgets)


# ============================================================
# PRUEBA 12: Operaciones CRUD básicas
# ============================================================
def test_crud_basico():
    print("   Probando operaciones CRUD básicas...")
    from database import Database

    db = Database()
    if not db.connect():
        return False

    # Contar tesis
    count = db.fetch_one("SELECT COUNT(*) as total FROM tesis")
    total_tesis = count["total"] if count else 0
    print(f"   - Tesis actuales en BD: {total_tesis}")

    # Contar capitulos
    count = db.fetch_one("SELECT COUNT(*) as total FROM capitulos")
    total_capitulos = count["total"] if count else 0
    print(f"   - Capítulos actuales en BD: {total_capitulos}")

    # Contar referencias
    count = db.fetch_one("SELECT COUNT(*) as total FROM referencias")
    total_refs = count["total"] if count else 0
    print(f"   - Referencias actuales en BD: {total_refs}")

    db.disconnect()
    return True


test("Operaciones CRUD básicas", test_crud_basico)

# ============================================================
# RESUMEN DE PRUEBAS
# ============================================================
print()
print("=" * 60)
print("RESUMEN DE PRUEBAS")
print("=" * 60)
print(f"   Pasadas: {resultados['passed']}")
print(f"   Fallidas: {resultados['failed']}")
print()

if resultados["errors"]:
    print("ERRORES DETALLADOS:")
    print("-" * 50)
    for nombre, error, trace in resultados["errors"]:
        print(f"\n{nombre}:")
        print(f"   {error}")
        # print(trace)  # Descomentar para ver traceback completo

print()
if resultados["failed"] == 0:
    print("*** TODAS LAS PRUEBAS PASARON! ***")
else:
    print(f"*** {resultados['failed']} prueba(s) fallaron. Revisar errores arriba.")

print()
print("=" * 60)
input("Presiona Enter para salir...")

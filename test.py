import sqlite3 

class Conexion ():
    try:
        self.con =sqlite3.connect("banco.db")
        self.crearTablas()
    except Exception as ex:
        print(ex)

    def crearTablas(self
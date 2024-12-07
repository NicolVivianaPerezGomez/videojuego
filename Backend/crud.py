import mysql.connector
import json

# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

# CRUD
def RegistrarJugador():
    if db:
        try:
            cursor = db.cursor()
            jug_nombre = input("Nombre del jugador: ")
            nivel = int(input("Nivel del jugador: "))
            puntuacion = int(input("Puntuación del jugador: "))
            equipo = input("Equipo del jugador: ")
            inventario = input("Inventario (en formato JSON): ")
            cursor.callproc('RegistraJugador', [jug_nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("Jugador registrado con éxito.")
        finally:
            cursor.close()
            db.close()

# Consultar jugadores
def ConsultarJugadores():
    if db:
        try:
            cursor = db.cursor()
            cursor.callproc('ConsultarJugadores')
            for result in cursor.stored_results():
                jugadores = result.fetchall()
                for jugador in jugadores:
                    print(jugador)
        finally:
                cursor.close()
                db.close()

# Modificar jugador
def ModificadorJugadores():
    if db:
        try:
            cursor = db.cursor()
            id_jugador = int(input("ID del jugador a modificar: "))
            nombre = input("Nuevo nombre del jugador: ")
            nivel = int(input("Nuevo nivel del jugador: "))
            puntuacion = int(input("Nueva puntuación del jugador: "))
            equipo = input("Nuevo equipo del jugador: ")
            inventario = input("Nuevo inventario (en formato JSON): ")
            cursor.callproc('ModificarJugador', [id_jugador, nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("Jugador modificado con éxito.")
        finally:
            cursor.close()
            db.close()

# Eliminar jugador
def EliminarJugador():
    if db:
        try:
            cursor = db.cursor()
            id_jugador = int(input("ID del jugador a eliminar: "))
            cursor.callproc('EliminarJugador', [id_jugador])
            db.commit()
            print("Jugador eliminado con éxito.")
        finally:
            cursor.close()
            db.close()

# Menú principal
def menu():
    while True:
        print("\n**** REGISTRAR JUGADORES ****")
        print("1. Crear jugador")
        print("2. Consultar jugadores")
        print("3. Modificar jugador")
        print("4. Eliminar jugador")
        print("5. Salir")
        opcion = input("\nELIJE UNA OPCIÓN: ")

        if opcion == "1":
            RegistrarJugador()
            break
        elif opcion == "2":
            ConsultarJugadores()
            break
        elif opcion == "3":
            ModificadorJugadores()
            break
        elif opcion == "4":
            EliminarJugador()
            break
        elif opcion == "5":
            print("Cerrando Registros........")
        else:
            print("ESTA OPCIÓN NO ES VÁLIDA")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
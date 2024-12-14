import mysql.connector
import json
import mysql.connector

def conectar_db():
    return mysql.connector.connect( host="localhost", user="root",  password="1234",database="videojuego" )

def agregar_jugador(conexion):
    cursor = conexion.cursor()
    nombre = input("Nombre del jugador: ")
    nivel = input("Nivel del jugador (por defecto 1): ") or 1
    puntuacion = input("Puntuación del jugador (por defecto 0): ") or 0
    equipo = input("Equipo del jugador (Equipo 1 y 2): ") or None
    inventario = input("Inventario en formato JSON (opcional): ") or None

    try:
        query = """
        INSERT INTO jugadores (jug_nombre, nivel, puntuación, equipo, inventario)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, nivel, puntuacion, equipo, inventario))
        conexion.commit()
        print("Jugador agregado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def ver_jugadores(conexion):
    cursor = conexion.cursor(dictionary=True)
    try:
        query = "SELECT * FROM jugadores"
        cursor.execute(query)
        jugadores = cursor.fetchall()

        if not jugadores:
            print("No hay jugadores registrados.")
        else:
            for jugador in jugadores:
                print(f"ID: {jugador['id_jugador']}, Nombre: {jugador['jug_nombre']}, Nivel: {jugador['nivel']}, Puntuación: {jugador['puntuación']}, Equipo: {jugador['equipo']}, Inventario: {jugador['inventario']}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def main():
    conexion = conectar_db()
    while True:
        print("\nCREAR JUGADORES:")
        print("1. Agregar jugador")
        print("2. Ver jugadores")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_jugador(conexion)
        elif opcion == "2":
            ver_jugadores(conexion)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

    conexion.close()

if __name__ == "__main__":
    main()

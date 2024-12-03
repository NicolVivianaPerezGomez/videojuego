import mysql.connector

# Configuración de la conexión
def conectar():
        conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="SistemaDeJuego"
        )

# CRUD para la tabla jugadores

# Crear un jugador
def crear_jugador(nombre, nivel, puntuacion, equipo, inventario):
    conexion = conectar()
    if conexion:
            cursor = conexion.cursor()
            query = """
                INSERT INTO jugadores (nombre, nivel, puntuacion, equipo, inventario)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, nivel, puntuacion, equipo, inventario))
            conexion.commit()
            print(f"Jugador '{nombre}' creado exitosamente")

# Leer jugadores
def leer_jugadores():
    conexion = conectar()
    if conexion:
            cursor = conexion.cursor()
            query = "SELECT * FROM jugadores"
            cursor.execute(query)
            jugadores = cursor.fetchall()
            print("Jugadores registrados:")
            for jugador in jugadores:
                print(jugador)


# Actualizar un jugador
def actualizar_jugador(id_jugador, nombre=None, nivel=None, puntuacion=None, equipo=None, inventario=None):
    conexion = conectar()
    if conexion:
            cursor = conexion.cursor()
            query = "UPDATE jugadores SET "
            updates = []
            valores = []

            if nombre:
                updates.append("nombre = %s")
                valores.append(nombre)
            if nivel:
                updates.append("nivel = %s")
                valores.append(nivel)
            if puntuacion:
                updates.append("puntuacion = %s")
                valores.append(puntuacion)
            if equipo:
                updates.append("equipo = %s")
                valores.append(equipo)
            if inventario:
                updates.append("inventario = %s")
                valores.append(inventario)

            query += ", ".join(updates) + " WHERE id_jugador = %s"
            valores.append(id_jugador)

            cursor.execute(query, valores)
            conexion.commit()
            print(f"Jugador con ID {id_jugador} actualizado exitosamente")


# Eliminar un jugador
def eliminar_jugador(id_jugador):
    conexion = conectar()
    if conexion:
            cursor = conexion.cursor()
            query = "DELETE FROM jugadores WHERE id_jugador = %s"
            cursor.execute(query, (id_jugador,))
            conexion.commit()
            print(f"Jugador con ID {id_jugador} eliminado exitosamente")


# Ejemplo de uso del CRUD
if __name__ == "__main__":
    # Crear jugadores
    crear_jugador("Juan", 5, 100, "EquipoA", '{"espada": "nivel 5", "escudo": "nivel 3"}')
    crear_jugador("María", 7, 200, "EquipoB", '{"pocion": "nivel 1", "arco": "nivel 4"}')

    # Leer jugadores
    leer_jugadores()

    # Actualizar un jugador
    actualizar_jugador(1, nivel=6, puntuacion=150)

    # Eliminar un jugador
    eliminar_jugador(2)

    # Leer jugadores después de modificaciones
    leer_jugadores()

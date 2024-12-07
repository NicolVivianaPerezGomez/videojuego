import mysql.connector
import json

# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

# CRUD
def RegistraJugador(jug_nombre, nivel, puntuacion, equipo, inventario):
    inventario_json = json.dumps(inventario)  # Convertir el diccionario a JSON
    cursor.callproc('RegistraJugador', (jug_nombre, nivel, puntuacion, equipo, inventario_json))

# Uso de la función guardar datos
try:
    RegistraJugador('Adela', 2, 60, 'Equipo2', {"Espada": 2, "Escudo": 1})
    db.commit()
    print("Jugador registrado exitosamente.")
finally:
    cursor.close()
    db.close()

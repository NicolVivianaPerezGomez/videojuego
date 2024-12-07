import mysql.connector
import json

# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

# CRUD
import json
def RegistraJugador(jug_nombre, nivel, puntuacion, equipo, inventario):
    inventario_json = json.dumps(inventario)  # Convertir el diccionario a JSON
    cursor.callproc('RegistraJugador', (jug_nombre, nivel, puntuacion, equipo, inventario_json))

# Uso de la función
    RegistraJugador('Sandra', 3, 150, 'Equipo1', {"Espada":1, "Arco": 4})
    db.commit()
    print("Jugador registrado exitosamente.")
    cursor.close()
    db.close()

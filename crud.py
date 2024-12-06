import mysql.connector

# CONECTAMOS LA BASE DE DATOS
db=mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="myql_native_password")
cursor = db.cursor()

# CRUD
# Regustar a un jugador
def RegistraJugador(jug_nombre, nivel, puntuacion, equipo, inventario):
    cursor = db.cursor()
    cursor.callproc('RegistraJugador',(jug_nombre,nivel,puntuacion,equipo,inventario))
    db.commit()
    cursor.close()
    db.close()
    print(f'Jugador Registrado{jug_nombre}{nivel}{puntuacion}{equipo}{nivel}.')
    
import mysql.connector
conexion = mysql.connector.connect(host="localhost", user="root" password="1234", database="videojuego")
cursor = conexion.cursor()
def conectar():
    print("Conectado a la base de datos")
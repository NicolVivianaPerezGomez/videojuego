import mysql.connector

#PARTE ARTE
def conectar():
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="videojuego"
        ):
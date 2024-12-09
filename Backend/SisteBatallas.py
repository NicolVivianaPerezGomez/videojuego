import mysql.connector
import json

#DICCIONARIO
# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

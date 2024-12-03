import mysql.connector

#PARTE ARTE
conexion = mysql.connector.connect(host="localhost", user="root" password="1234", database="videojuego")
cursor = conexion.cursor()

def conectar():

 #Hola Grupo 2  
 #Hola Juli y Saris

    print("Conectado a la base de datos")
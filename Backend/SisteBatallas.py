import mysql.connector
import json

#ARBOLBINANIRIO
# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()


class Node:
    def __init__(self, fecha, partida):
        self.fecha = fecha
        self.partida = partida
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, fecha, partida):
        if self.raiz is None:
            self.raiz = Node(fecha, partida)
        else:
            self._insertar_recursivo(self.raiz, fecha, partida)

    def _insertar_recursivo(self, nodo, fecha, partida):
        if fecha < nodo.fecha:
            if nodo.izquierda is None:
                nodo.izquierda = Node(fecha, partida)
            else:
                self._insertar_recursivo(nodo.izquierda, fecha, partida)
        else:
            if nodo.derecha is None:
                nodo.derecha = Node(fecha, partida)
            else:
                self._insertar_recursivo(nodo.derecha, fecha, partida)

    def buscar(self, fecha):
        return self._buscar_recursivo(self.raiz, fecha)

    def _buscar_recursivo(self, nodo, fecha):
        if nodo is None:
            return None
        if fecha == nodo.fecha:
            return nodo.partida
        elif fecha < nodo.fecha:
            return self._buscar_recursivo(nodo.izquierda, fecha)
        else:
            return self._buscar_recursivo(nodo.derecha, fecha)

    def mostrar_inorden(self):
        self._mostrar_inorden_recursivo(self.raiz)

    def _mostrar_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_inorden_recursivo(nodo.izquierda)
            print(f"Fecha: {nodo.fecha}, Partida: {nodo.partida}")
            self._mostrar_inorden_recursivo(nodo.derecha)

class Partida:
    def __init__(self, equipo1, equipo2, resultado):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.resultado = resultado

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    # Crear algunas partidas
    partida1 = Partida("Equipo A", "Equipo B", "2-1")
    partida2 = Partida("Equipo C", "Equipo D", "3-0")
    partida3 = Partida("Equipo E", "Equipo F", "1-1")

    # Insertar partidas en el árbol
    arbol.insertar("2023-10-01", partida1)
    arbol.insertar("2023-10-02", partida2)
    arbol.insertar("2023-10-03", partida3)

    # Mostrar todas las partidas en orden
    print("Historial de partidas:")
    arbol.mostrar_inorden()

    # Buscar una partida por fecha
    fecha_busqueda = "2023-10-02"
    partida_encontrada = arbol.buscar(fecha_busqueda)
    if partida_encontrada:
        print(f"Partida encontrada en {fecha_busqueda}: {partida_encontrada.equipo1} vs {partida_encontrada.equipo2}, Resultado: {partida_encontrada.resultado}")
    else:
        print(f"No se encontró partida en la fecha {fecha_busqueda}.")


def main():

    fechas_partidas = []

    while True:
        print("\n--- Consola de Almacenamiento de Fechas de Partidas ---")
        print("1. Agregar fecha de partida")
        print("2. Mostrar todas las fechas de partidas")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            fecha = input("Ingresa la fecha de la partida (formato YYYY-MM-DD): ")
            fechas_partidas.append(fecha)
            print(f"Fecha {fecha} agregada exitosamente.")
        elif opcion == '2':
            print("\nFechas de partidas almacenadas:")
            for fecha in fechas_partidas:
                print(fecha)
        elif opcion == '3':
            print("Saliendo de la consola.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()

#GRAFOS

class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista) NODO: UBICACION JUGADORE ARISTA: RUTA Y EL PESO ES LA DISTANCIA
    def add_edge(self, ubicacion, rutas, distancia=1):
        if ubicacion not in self.graph:
            self.graph[ubicacion] = [] 
        self.graph[ubicacion].append(rutas)  

CREATE DATABASE videojuego;
use videojuego;

CREATE TABLE jugadores (
    id_jugador INT  AUTO_INCREMENT PRIMARY KEY,
    jug_nombre VARCHAR(100) NOT NULL UNIQUE,
    nivel INT NOT NULL DEFAULT 1,
    puntuación INT NOT NULL DEFAULT 0,
    equipo VARCHAR(50) NULL,
    inventario JSON
);

CREATE TABLE partidas(
    id_partida INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    equipo_1 VARCHAR(50) NOT NULL,
    equipo_2 VARCHAR(50) NOT NULL,
    resultado VARCHAR(50)
);

CREATE TABLE mundos(
     id_mundos INT AUTO_INCREMENT PRIMARY KEY,
     grafo_serializado JSON
);

CREATE TABLE ranking(
	id_ranking INT AUTO_INCREMENT PRIMARY KEY,
	id_jugador INT NOT NULL,
	puntuacion INT NOT NULL,
	posicion INT NOT NULL,
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);
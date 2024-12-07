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

-- SELECCIONA EL TOP 10 DE MAYOR PUNTUACIÓN 
SELECT jug_nombre, puntuación 
FROM jugadores -- De donde provienen los datos
ORDER BY puntuación DESC -- Ordena los resultados de manera descendente
LIMIT 10; -- Permitia que solo los 10 primeros puntajes se muestren


-- PROCEDIMIENTOS DE ALMACENAMIENTO

-- Registro de un jugador 
DELIMITER //
CREATE PROCEDURE RegistraJugador( IN p_nombre VARCHAR(100), IN p_nivel INT, IN p_puntuacion INT, IN p_equipo VARCHAR(50), IN p_inventario JSON) -- IN: Indica los atributos de entrada 
BEGIN
INSERT INTO jugadores (jug_nombre, nivel, puntuación, equipo, inventario)  -- Datos de entrada 
VALUES (p_nombre, p_nivel, p_puntuacion, p_equipo, p_inventario); -- Datos asignados 
END //
DELIMITER ;

-- Registro
CALL RegistraJugador('Julian', 5,10, 'Equipo2', '{"Arco": 4, "Armadura": 3}');

-- Consultar todos los jugadores
DELIMITER //
CREATE PROCEDURE ConsultarJugadores()
BEGIN
SELECT * FROM jugadores;
END //
DELIMITER ;

-- Consulta
CALL ConsultarJugadores;

-- Modificar un jugador
DELIMITER //
CREATE PROCEDURE ModificarJugador(IN p_id INT, IN p_nombre VARCHAR(100), IN p_nivel INT, IN p_puntuacion INT, IN p_equipo VARCHAR(50), IN p_inventario JSON)
BEGIN
UPDATE jugadores -- Actualiza el jugador 
SET jug_nombre = p_nombre, nivel = p_nivel, puntuación = p_puntuacion, equipo = p_equipo, inventario = p_inventario -- Columnas que se actualizan 
WHERE id_jugador = p_id; -- Actaliza si id_jugador y p_id coinciden
END //
DELIMITER 

-- Modificaciòn
CALL ModificarJugador(20,'David',5,200,'Equipo1','{"Armadura": 3, "Arco": 4}');

-- Eliminar un jugador
DELIMITER //
CREATE PROCEDURE EliminarJugador(IN p_id INT)
BEGIN
DELETE FROM jugadores -- Inicio de comando para eliminaciòn
WHERE id_jugador = p_id; -- Identifica el jugador a eliminar
END //
DELIMITER ;

-- Eliminaciòn
CALL EliminarJugador(21);



	




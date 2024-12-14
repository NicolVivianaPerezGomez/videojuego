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


-- PROCEDIMIENTOS DE ALMACENAMIENTO JUGADOR

-- Registro de un jugador 
DELIMITER //
CREATE PROCEDURE RegistraJugador( IN p_nombre VARCHAR(100), IN p_nivel INT, IN p_puntuacion INT, IN p_equipo VARCHAR(50), IN p_inventario JSON) -- IN: Indica los atributos de entrada 
BEGIN
INSERT INTO jugadores (jug_nombre, nivel, puntuación, equipo, inventario)  -- Datos de entrada 
VALUES (p_nombre, p_nivel, p_puntuacion, p_equipo, p_inventario); -- Datos asignados 
END //
DELIMITER ;


-- Registro
CALL RegistraJugador('Sara', 5,10, 'Equipo2', '{"Arco": 4, "Armadura": 3}');

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
CALL ModificarJugador('David',5,200,'Equipo1','{"Armadura": 3, "Arco": 4}');

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

-- PROCEDIMIENTOS DE ALMACENAMIENTO MUNDOS

DELIMITER //
CREATE PROCEDURE InsertarMundo(IN p_grafo_serializado JSON)
BEGIN
    INSERT INTO mundos (grafo_serializado) VALUES (p_grafo_serializado);
END //
DELIMITER ;

 CALL InsertarMundo('{"nodos": ["A", "B"], "aristas": [["A", "B"]]}');
 
 
DELIMITER //
CREATE PROCEDURE ActualizarMundo(IN p_id_mundos INT, IN p_grafo_serializado JSON)
BEGIN
    UPDATE mundos
    SET grafo_serializado = p_grafo_serializado
    WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL ActualizarMundo(2, '{"nodos": ["A", "B", "C"], "aristas": [["A", "B"], ["B", "C"]]}');

DELIMITER //
CREATE PROCEDURE ConsultarMundo(IN p_id_mundos INT)
BEGIN
    SELECT * FROM mundos WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL ConsultarMundo(2);

DELIMITER //
CREATE PROCEDURE EliminarMundo(IN p_id_mundos INT)
BEGIN
    DELETE FROM mundos WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL EliminarMundo(1);

DELIMITER //
CREATE PROCEDURE consultar_ubicaciones()
BEGIN
    SELECT id_mundos, JSON_UNQUOTE(JSON_EXTRACT(grafo_serializado, '$.nodos')) AS ubicaciones
    FROM mundos;
END //
DELIMITER ;

CALL consultar_ubicaciones();

DELIMITER //
CREATE PROCEDURE eliminar_ubicacion(IN p_id_mundos INT, IN p_ubicacion VARCHAR(50))
BEGIN
    -- Eliminar el nodo
    UPDATE mundos
    SET grafo_serializado = JSON_REMOVE(grafo_serializado, CONCAT('$.nodos[', JSON_UNQUOTE(JSON_SEARCH(grafo_serializado, 'one', p_ubicacion)), ']'))
    WHERE id_mundos = p_id_mundos;

    -- Eliminar las rutas asociadas
    UPDATE mundos
    SET grafo_serializado = JSON_REMOVE(grafo_serializado, CONCAT('$.aristas[', JSON_UNQUOTE(JSON_SEARCH(grafo_serializado, 'one', p_ubicacion)), ']'))
    WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL eliminar_ubicacion(1, 'A');

DELIMITER //
CREATE PROCEDURE agregar_ruta(IN p_id_mundos INT, IN p_ruta JSON)
BEGIN
    UPDATE mundos
    SET grafo_serializado = JSON_ARRAY_APPEND(grafo_serializado, '$.aristas', p_ruta)
    WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL agregar_ruta(1, '{"origen": "A", "destino": "B", "distancia": 10}');

DELIMITER //
CREATE PROCEDURE consultar_rutas()
BEGIN
    SELECT id_mundos, JSON_UNQUOTE(JSON_EXTRACT(grafo_serializado, '$.aristas')) AS rutas
    FROM mundos;
END //
DELIMITER ;

CALL consultar_rutas();

DELIMITER //
CREATE PROCEDURE actualizar_distancia(IN p_id_mundos INT, IN p_ruta JSON, IN p_distancia INT)
BEGIN
    UPDATE mundos
    SET grafo_serializado = JSON_REPLACE(grafo_serializado, 
        CONCAT('$.aristas[', JSON_UNQUOTE(JSON_SEARCH(grafo_serializado, 'one', p_ruta)), '].distancia'), p_distancia)
    WHERE id_mundos = p_id_mundos;
END //
DELIMITER ;

CALL actualizar_distancia(1, '{"origen": "A", "destino": "B"}', 15);


-- PROCEDIMIENTOS DE ALMACENAMIENTO PARTIDAS

DELIMITER //
CREATE PROCEDURE insertar_partida(IN p_fecha DATE,IN p_equipo_1 VARCHAR(50),IN p_equipo_2 VARCHAR(50),IN p_resultado VARCHAR(50))
BEGIN
    INSERT INTO partidas(fecha, equipo_1, equipo_2, resultado)
    VALUES (p_fecha, p_equipo_1, p_equipo_2, p_resultado);
END //
DELIMITER ;

CALL insertar_partida('2024-12-13', 'Equipo A', 'Equipo B', '2-1');

DELIMITER //
CREATE PROCEDURE consultar_partidas()
BEGIN
    SELECT * FROM partidas;
END //
DELIMITER ;

CALL consultar_partidas();

DELIMITER //
CREATE PROCEDURE actualizar_partida(IN p_id_partida INT,IN p_fecha DATE,IN p_equipo_1 VARCHAR(50),IN p_equipo_2 VARCHAR(50),IN p_resultado VARCHAR(50))
BEGIN
    UPDATE partidas
    SET fecha = p_fecha,
        equipo_1 = p_equipo_1,
        equipo_2 = p_equipo_2,
        resultado = p_resultado
    WHERE id_partida = p_id_partida;
END //
DELIMITER ;

CALL actualizar_partida(1, '2024-12-14', 'Equipo C', 'Equipo D', '3-2');

DELIMITER //
CREATE PROCEDURE eliminar_partida(IN p_id_partida INT)
BEGIN
    DELETE FROM partidas
    WHERE id_partida = p_id_partida;
END //
DELIMITER ;

CALL eliminar_partida(1);

-- PROCEDIMIENTOS DE ALMACENAMIENTO RANKING

DELIMITER //
CREATE PROCEDURE actualizar_ranking(IN p_id_ranking INT,IN p_puntuacion INT,IN p_posicion INT
)
BEGIN
    UPDATE ranking
    SET puntuacion = p_puntuacion, posicion = p_posicion
    WHERE id_ranking = p_id_ranking;
END //
DELIMITER ;

CALL actualizar_ranking(1, 1500, 2);

DELIMITER //
CREATE PROCEDURE eliminar_ranking(IN p_id_ranking INT)
BEGIN
    DELETE FROM ranking
    WHERE id_ranking = p_id_ranking;
END //
DELIMITER ;

CALL actualizar_ranking(1, 1500, 2);






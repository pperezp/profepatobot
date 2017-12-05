CREATE DATABASE profe_pato_bot;

USE profe_pato_bot;

CREATE TABLE alumno(
  id INT,
  nombre VARCHAR(200),
  fecha DATETIME,
  PRIMARY KEY (id)
);

SELECT * FROM alumno;

DROP DATABASE profe_pato_bot;
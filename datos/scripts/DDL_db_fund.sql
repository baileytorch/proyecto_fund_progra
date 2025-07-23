USE 'db_proyecto_intro';
GO;

CREATE TABLE opciones_menu(
    id INTEGER NOT NULL AUTO_INCREMENT,
    numero_opcion INTEGER NOT NULL,
    nombre_opcion VARCHAR(25) NOT NULL,

    CONSTRAINT pk_opciones_menu PRIMARY KEY (id)
);

CREATE TABLE asignaturas(
    id INTEGER NOT NULL AUTO_INCREMENT,
    codigo_asignatura CHAR(5) NOT NULL,
    nombre_asignatura VARCHAR(255) NOT NULL,

    CONSTRAINT pk_asignaturas PRIMARY KEY (id)
);

CREATE TABLE docentes(
    id INTEGER NOT NULL AUTO_INCREMENT,
    rut INTEGER NOT NULL UNIQUE,
    digito_verificador CHAR(1) NOT NULL,
    nombre_docente VARCHAR(255) NOT NULL,
    correo_docente VARCHAR(255) NOT NULL,
    direccion_docente VARCHAR(255) NOT NULL,

    CONSTRAINT pk_docentes PRIMARY KEY (id)
);

CREATE TABLE asignaturas_docentes(
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_asignatura INTEGER NOT NULL,
    id_docente INTEGER NOT NULL,

    CONSTRAINT pk_asignaturas_docentes PRIMARY KEY (id),
    CONSTRAINT fk_asignaturas FOREIGN KEY (id_asignatura) REFERENCES asignaturas (id),
    CONSTRAINT fk_docentes FOREIGN KEY (id_docente) REFERENCES docentes (id)
);
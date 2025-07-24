INSERT INTO opciones_menu (numero_opcion,nombre_opcion,tipo_menu,habilitado)
VALUES
(1,'Gestión Asignaturas',1,1),
(2,'Gestión Docentes',1,1),
(0,'salir',1,1),
(1,'Listado Asignaturas',2,1),
(2,'Agregar Asignatura',2,1),
(3,'Modificar Asignatura',2,1),
(4,'Eliminar Asignatura',2,1),
(0,'Volver Menú Anterior',2,1),
(1,'Listado Docentes',3,1),
(2,'Agregar Docente',3,1),
(3,'Modificar Docente',3,1),
(4,'Eliminar Docente',3,1),
(0,'Volver Menú Anterior',3,1);

INSERT INTO asignaturas (codigo_asignatura,nombre_asignatura,habilitado)
VALUES
('BIO','Biología Celular',1),
('QUI','Química inorgánica',1),
('FIS','Cinemática',1);

INSERT INTO docentes (rut,digito_verificador,nombre_docente,correo_docente,direccion_docente,habilitado)
VALUES
(12345678,'5','Aquiles Baeza','aquiles.baeza@test,test','Los Confines 123, Temuco',1),
(12345679,'5','Wendy Sulca','wendy.sulca@test,test','Los Confines 123, Temuco',1),
(12345689,'5','Delfin Quispe','delfin.quispe@test,test','Los Confines 123, Temuco',1);
from datos.conexion_db import leer_datos


def menu_principal():
    consulta = '''
        SELECT numero_opcion,nombre_opcion
        FROM opciones_menu
        WHERE tipo_menu = 1
    '''
    resultado = leer_datos(consulta)
    print(resultado)


def menu_asignaturas():
    pass

from datos.asignaturas import asignaturas
from datos.datos_asignaturas import guardar_asignatura


def listado_asignaturas():
    # if asignaturas != None:
    #     print(f'Imprimiendo listado != None: {asignaturas}')
    print('Listado de Asignaturas')
    print('======================')
    if len(asignaturas) > 0:
        contador = 0
        for asignatura in asignaturas:
            contador += 1
            print(f'[{contador}] {asignatura}')
        print()
    else:
        print('No se han encontrado elementos')


def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input('Ingrese el nombre de su nueva asignatura: ')
    print()
    if nueva_asignatura != '':
        asignaturas.append(nueva_asignatura)
    datos_guardar = f'asignaturas = {asignaturas}'
    guardar_asignatura(datos_guardar)
    listado_asignaturas()

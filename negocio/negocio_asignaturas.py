from datos.datos_asignaturas import obtener_listado_asignaturas, guardar_asignatura


def listado_asignaturas():
    # if asignaturas != None:
    #     print(f'Imprimiendo listado != None: {asignaturas}')
    print('Listado de Asignaturas')
    print('======================')
    asignaturas = obtener_listado_asignaturas()
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
    asignaturas = obtener_listado_asignaturas()
    if len(asignaturas) > 0:
        if nueva_asignatura != '':
            asignaturas.append(nueva_asignatura.title())
        datos_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(datos_guardar)
    listado_asignaturas()


def modificar_asignatura():
    listado_asignaturas()
    indicar_asignatura = input('Indique el número de la asignatura: ')
    try:
        numero_asignatura = int(indicar_asignatura)
        asignaturas = obtener_listado_asignaturas()
        if len(asignaturas) > 0:
            asignatura_modificada = input(
                'Ingrese nuevo nombre de asignatura: ')
            if asignatura_modificada != '':
                asignaturas[numero_asignatura - 1] = asignatura_modificada
        datos_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(datos_guardar)
    except:
        print('Valor NO corresponde')


def eliminar_asignatura():
    listado_asignaturas()
    indicar_asignatura = input('Indique el número de la asignatura: ')
    try:
        numero_asignatura = int(indicar_asignatura)
        asignaturas = obtener_listado_asignaturas()
        if len(asignaturas) > 0:
            asignaturas.pop(numero_asignatura - 1)
        datos_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(datos_guardar)
    except:
        print('Valor NO corresponde')

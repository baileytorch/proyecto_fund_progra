from datos.asignaturas import asignaturas


def listado_asignaturas():
    # if asignaturas != None:
    #     print(f'Imprimiendo listado != None: {asignaturas}')
    if len(asignaturas) > 0:
        contador = 0
        for asignatura in asignaturas:
            contador += 1
            print(f'[{contador}] {asignatura}')
        print()
    else:
        print('No se han encontrado elementos')

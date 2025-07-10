from auxiliares.version import version_actual
from datos.asignaturas import asignaturas


def menu_principal():
    print()
    print(f'Aplicación Gestión de Notas v.{version_actual}')
    print('===========================')

    while True:
        print('[1] Gestión Asignaturas')
        print('[2] Gestión Docentes')
        print('[3] Gestión Estudiantes')
        print('[4] Gestión Notas')
        print('[0] Salir')
        print()

        opcion = input('Seleccione su opción: ')
        if opcion == '1':
            contador = 1
            print()
            print('Listado de Asignaturas')
            for asignatura in asignaturas:
                print(f'{contador} {asignatura}')
                contador += 1

        elif opcion == '2':
            print('Ud. ha seleccionado la opción 2')
        elif opcion == '3':
            print('Ud. ha seleccionado la opción 3')
        elif opcion == '4':
            print('Ud. ha seleccionado la opción 4')
        elif opcion == '0':
            print('Saliendo...')
            break
        else:
            print('Opción ingresada NO corresponde...')


menu_principal()

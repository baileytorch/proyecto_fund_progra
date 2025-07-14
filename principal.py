from auxiliares.version import version_actual
from datos.asignaturas import asignaturas
from negocio.negocio_menu import menu_principal


def programa_principal():
    print()
    print(f'Aplicación Gestión de Notas v.{version_actual}')
    print('===========================')

    while True:
        menu_principal()

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


programa_principal()

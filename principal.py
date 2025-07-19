from auxiliares.version import version_actual
from datos.asignaturas import asignaturas
from negocio.negocio_menu import menu_principal, menu_asignaturas
from negocio.negocio_asignaturas import listado_asignaturas, agregar_asignatura, modificar_asignatura


def programa_principal():
    print()
    print(f'Aplicación Gestión de Notas v.{version_actual}')
    print('===========================')

    while True:
        menu_principal()
        opcion = input('Seleccione su opción: ')
        print()
        if opcion == '1':
            while True:
                menu_asignaturas()
                opcion_asignaturas = input('Seleccione su opción: ')
                print()
                if opcion_asignaturas == '1':
                    listado_asignaturas()
                elif opcion_asignaturas == '2':
                    agregar_asignatura()
                elif opcion_asignaturas == '3':
                    modificar_asignatura()
                elif opcion_asignaturas == '4':
                    pass
                elif opcion_asignaturas == '0':
                    print('Volviendo al menú anterior...')
                    break
                else:
                    print('Opción ingresada NO corresponde...')
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

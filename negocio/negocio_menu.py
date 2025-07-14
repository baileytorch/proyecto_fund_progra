import auxiliares.opciones_menu as opciones


def menu_principal():
    for clave, valor in opciones.menu_principal.items():
        print(f'[{clave}] {valor}')
    print()

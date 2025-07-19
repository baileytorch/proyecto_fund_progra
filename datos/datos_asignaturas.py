import os
from datos.asignaturas import asignaturas


def obtener_listado_asignaturas():
    if len(asignaturas) > 0:
        return asignaturas
    else:
        return []


def guardar_asignatura(listado_asignaturas):
    archivo = 'asignaturas.py'
    ubicacion = os.path.join('datos', archivo)
    ubicacion = os.path.abspath(ubicacion)
    ubicacion = os.path.relpath(ubicacion)

    archivo = open(ubicacion, 'w+')
    archivo.write(listado_asignaturas)
    archivo.close()

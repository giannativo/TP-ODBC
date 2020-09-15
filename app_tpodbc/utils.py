import pyodbc

conn = pyodbc.connect(
    'DRIVER={MySQL ODBC 8.0 Unicode Driver};UID=root;Pwd=root;Server=localhost;Database=sakila;OPTION=3;')

cursor = conn.cursor()


def traer_ciudades():
    ciudades = []
    cursor.execute('SELECT * FROM city')
    for ciudad in cursor:
        ciudades.append({'id': ciudad[0], 'ciudad': ciudad[1]})
    return ciudades


def traer_clientes(cursor):
    clientes = []
    for cliente in cursor:
        clientes.append({'id_cliente': cliente[0], 'id_tienda': cliente[1], 'nombre': cliente[2],
                         'apellido': cliente[3], 'email': cliente[4], 'activo': cliente[5], 'direccion': cliente[6],
                         'distrito': cliente[7], 'codigo_postal': cliente[8], 'telefono': cliente[9],
                         'ciudad': cliente[10], 'pais': cliente[11], 'id_ciudad': cliente[12],
                         'id_direccion': cliente[13]})
    return clientes

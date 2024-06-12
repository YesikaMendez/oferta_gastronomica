import pymysql
import requests
import csv
import io

with open('claves.txt') as archivo:
    keys = [clave.strip() for clave in archivo]

connection = pymysql.connect(host=keys[0],
                             database=keys[1],
                             user=keys[2],
                             password=keys[3])
cursor = connection.cursor()


respuesta = requests.get('https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ente-de-turismo/oferta-establecimientos-gastronomicos/oferta_gastronomica.csv')

contenido_csv = respuesta.text

# Utilizar io.StringIO para tratar el contenido CSV como un archivo

f = io.StringIO(contenido_csv)
lector_dict = csv.DictReader(f)

# Recorrer las filas del CSV e imprimir cada fila
for fila in lector_dict:
    id_local = fila['id']
    nombre = fila['nombre']
    categoria = fila['categoria']
    direccion = fila['direccion_completa']
    barrio = fila['barrio']
    comuna = fila['comuna']
    print(f"Nombre: {nombre}, Categoría: {categoria},direccion: {direccion}")

    cursor.execute("INSERT INTO locaciones (id_local,nombre,categoria,direccion,barrio,comuna) VALUES(%s,%s,%s,%s,%s,%s)", (id_local, nombre, categoria, direccion, barrio, comuna))

    connection.commit()  # Para que impacten los queries

# se terminan de insertan los registros recorridos en el for y se procede a cerrar la conexion
connection.close()
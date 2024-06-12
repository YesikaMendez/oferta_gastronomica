import pymysql

with open('claves.txt') as archivo:
    keys = [clave.strip() for clave in archivo]

connection = pymysql.connect(host=keys[0],
                             database=keys[1],
                             user=keys[2],
                             password=keys[3])
cursor = connection.cursor()
cursor.execute("SELECT * FROM alumno ORDER BY idAlumno DESC;")
alumnos=cursor.fetchall()
for fila in alumnos:
   print(fila)
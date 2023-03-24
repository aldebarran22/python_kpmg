"""
Filtrar ficheros de una carpeta:
"""

import os

fichero = "libro1.xlsx"
t = fichero.partition('.')
# Expansión de tuplas, ignoramos el separador: '.'
nombreF, _, ext = t

# Listar solo los archivos de dos extensiones: csv y txt
extensiones = ('txt','csv')
for f  in os.listdir():
    ext = f.partition('.')[2]
    if ext in extensiones:
        print(f)

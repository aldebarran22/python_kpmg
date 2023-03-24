"""
Filtrar ficheros de una carpeta:
"""

import os

fichero = "libro1.xlsx"
t = fichero.partition('.')
# Expansión de tuplas, ignoramos el separador: '.'
nombreF, _, ext = t

# Listar solo los archivos de dos extensiones: csv y txt
for f  in os.listdir():
    print(f)

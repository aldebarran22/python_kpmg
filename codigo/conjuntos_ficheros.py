"""
Cargar los ficheros csv con python y comparar los dos ficheros línea a línea
"""

"""
Pasos:
1) Abrir el fichero
2) Leer el contenido del fichero
3) Cerrar el fichero
"""
# Cargar los dos ficheros:
fichero1 = open("Empleados.csv","r")
txt = fichero1.read()
fichero1.close()
print(txt)

fichero2 = open("Empleados2.csv","r")
txt2 = fichero2.read()
fichero2.close()
print(txt2)

# Partir cada bloque de texto en filas: las filas están separadas por \n
L1 = txt.split('\n')
#print(L1)

L2 = txt2.split('\n')
#print(L2)

# Pasamos las listas a conjuntos quitando previamente las cabeceras:
c1 = set(L1[1:])
c2 = set(L2[1:])
filasComunes = c1 & c2 # Intersección
print("Filas comunes: \n", filasComunes)

# Diferencias: 
# Lineas que tenemos en el primer texto (txt) y que no están en el segundo (txt2)
filastxt1QueNoCoinciden = c1 - c2 # Diferencia
print("\nfilastxt1QueNoCoinciden: \n", filastxt1QueNoCoinciden)

todasLasFilasSinRepes = c1 | c2 # La unión
print('\nFilas sin repes:\n', todasLasFilasSinRepes)


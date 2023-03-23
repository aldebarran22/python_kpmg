"""
Extraer de dos ficheros CSV una columna y comparar las dos listas de nombres.csv
Buscar coincidencias a nivel de los nombres.
"""

# Cargar los dos ficheros:
fichero1 = open("../ficheros/Empleados_1.csv","r")
txt = fichero1.read()
fichero1.close()
#print(txt)

fichero2 = open("../ficheros/Empleados_2.csv","r")
txt2 = fichero2.read()
fichero2.close()
#print(txt2)

# Partir cada fichero por líneas:
L1 = txt.split('\n')
L2 = txt2.split('\n')

nombres1 = []
for i in L1[1:]:    
    fila = i.split(';')
    nombres1.append(fila[1])
print(nombres1)


nombres2 = []
for i in L2[1:]:    
    fila = i.split(';')
    nombres2.append(fila[1]) # nombres2 += [fila[1]]
print(nombres2)
    


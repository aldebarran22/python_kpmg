"""
Extraer de dos ficheros CSV una columna y comparar las dos listas de nombres.csv
Buscar coincidencias a nivel de los nombres.
VERSION CON FUNCIONES
"""

def cargarFichero(path):
    """
    Carga el fichero que recibe por parámetro y lo devuelve como texto
    """
    fichero1 = open(path,"r")
    txt = fichero1.read()
    fichero1.close()
    return txt

def extraerNombres(texto):
    """
    Recibe un texto en formato CSV, lo parte en líneas y extrae la columna del nombre
    """
    L = texto.split('\n')
    nombres = []
    for i in L[1:]:    
        
        fila = i.split(';')

        if fila[1] == 'Queen':
            print()

        nombres.append(fila[1])    
        

    return nombres

#Cargar el fichero utilizando la función: "cargarFichero"
txt = cargarFichero('Empleados.csv')
txt2 = cargarFichero('Empleados2.csv')

# Extraer los nombres de cada texto con la función: "extraerNombres"
nombres1 = extraerNombres(txt)
nombres2 = extraerNombres(txt2)

print(nombres1)
print(nombres2)
    


"""
Funciones relacionadas con el fichero de pedidos
"""

from datetime import datetime

def cargarFichero(path):
    """
    Carga el fichero que recibe por parámetro y lo devuelve como texto
    """
    fichero1 = open(path,"r")
    txt = fichero1.read()
    fichero1.close()
    return txt

def extraerColumna(texto, col):
    """
    Recibe un texto en formato CSV, lo parte en líneas y extrae la columna que indicamos con el parámetro col
    idpedido;cliente;idempleado;idempresa;importe;pais
    """
    L = texto.split('\n')
    cabeceras = L[0].split(';')
    posCol = cabeceras.index(col)
    nombres = []
    for i in L[1:]:            
        fila = i.split(';')
        nombres.append(fila[posCol])          

    return nombres


def calcularImportePorPais(texto, pais):
    """
    Recibe el texto y un pais y calcula el importe de los pedidos de ese pais
    """
    L = texto.split('\n')
    suma = 0
    for i in L[1:]:            
        fila = i.split(';')
        if fila[5] == pais:
            cantidad = float(fila[4])
            suma += cantidad
    return suma

def calcularImportes(texto):
    """
    Calcular el importe acumulado de todos los países
    """
    L = texto.split('\n')   
    d = dict()
    for i in L[1:]:            
        fila = i.split(';')
        pais = fila[5]
        cantidad = float(fila[4])
        if pais in d:
            d[pais] += cantidad
        else:
            # Crear la clave con el primer pedido del país
            d[pais] = cantidad
    return d

t1 = datetime.now()
texto = cargarFichero('Pedidos.csv')
d = calcularImportes(texto)
t2 = datetime.now()
print('Algoritmo 1: ', t2-t1)


#total = calcularImportePorPais(texto, 'Alemania')
#print('total: ', total)

t1 = datetime.now()
texto = cargarFichero('Pedidos.csv')
# EXTRAER LOS PAISES, QUITAR REPETIDOS Y ORDENAR ASCENDENTEMENTE:
# Lo pasamos por un conjunto para quitar repetidos:
paises = set(extraerColumna(texto, 'pais'))
# La función sorted ordena una colección y devuelve una lista con los datos ordenados!
Lpaises = sorted(paises)

# 21 paises x 830 filas de pedidos = 17430 iteraciones
# Solución poco eficiente:
for pais in Lpaises:    
    calcularImportePorPais(texto, pais)
t2 = datetime.now()
print('Algoritmo 2: ', t2-t1)

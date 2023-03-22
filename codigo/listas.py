"""
Ejemplos con listas en python:
definición, acceso, modificación, copia, slicing ...
funciones sobre listas
"""

# definición:
L = [1,4,5,3,2,8]
print(L, type(L))
print('Longitud: ', len(L)) # funcion(colección)
L.sort() # objeto.método()
print(L)

s ="hola que tal"
L2 = list(s)
print(L2)

# Listas mixed:
L = ['hola', [1,2,3], 78.9, True, None]
print(L, type(L), len(L))

#  Añadir elementos:
L2 = []  # L = list()
L2 += [56]
L2 += [90,1,2,3]
print(L2)

# Comprobar si existe un valor en la lista:
print('hola' in L)
print(78 in L)

# Bucles: i representa cada elemento
for i in L:
    print(i)

for pos, i in enumerate(L):
    print(pos, i)

for pos in range(len(L)):
    print(pos, L[pos])

# 20 iteraciones del 0 al 19
for i in range(20):
    print(i, end=' ') 
print()  

# modificar los elementos de una lista:
L = list(range(10))
print(L)
L[0] = 1000 # Machaca la posición 0
print(L)

# Funciones:
print('suma: ', sum(L))
print('longitud:', len(L))
print('min: ', min(L))
print('max: ', max(L))
print('media: ', sum(L)/len(L))

# Prácticas con listas:
# Dada una lista de números multiplicar por 5 cada elemento
# El resultado se da en una nueva lista
L = [1,4,3,5,6,1] # L2 = [5,20,15,25,30,5]
L2 = []
for i in L:
    L2 += [i*5]
print(L)
print(L2)

# Dadas dos listas calcular la intersección de ambas listas:
L1 = [3,4,5,5,6,7,3]
L2 = [3,5,7,7]
# LI = [3,5,7]
LI = []
for i in L1:
    if i in L2 and i not in LI:
        LI += [i]
print(LI)

# índices negativos
L = list(range(1,11))
print(L)
print('El último elemento:', L[len(L)-1], L[-1])
# Ejemplo: extraer el nombre del fichero de un path:
path = "C:/mis documentos/libros/cuentas.xlsx"
L = path.split("/")
print('Nombre del fichero:',L[-1])
print('Nombre del fichero:',path.split("/")[-1])

# slicing lista[ini:fin-1:salto]
L = list(range(1,11))
print(L)
print('Los 3 primeros: ', L[0:3])
print('Los 3 primeros: ', L[:3])
print('los 3 últimos: ', L[-3:])
print('Quitar el primero y el último: ', L[1:-1])
print('Todos pero de 2 en 2: ', L[::2])
print('Invertida: ', L[::-1])

nombre = "Ana"
if nombre == nombre[::-1]:
    print(nombre,'es palíndromo')
else:
    print('no lo es')


# Copiar listas


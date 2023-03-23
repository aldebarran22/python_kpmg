"""
Pruebas con conjuntos de python
Quitar repetidos, definición, añadir elementos al conjunto etc.
"""

# Definición:
c1 = {34,6,3,2,1,1,1,3}
print(c1, type(c1))

# Quitar repetidos a una lista:
L = [1,2,3,4,5,6,7,8,8,9,1,2,3,6,7]
c2 = set(L)
print(c2, type(c2))
L = list(c2)
print(L, type(L))

# Programa para almacenar los nombres de amigos que se apuntan a una comida:
# Versión 1 con una lista
amigos = []
nombre=''
while nombre !='fin':
    nombre = input('nombre:>')
    if nombre != 'fin':
        amigos.append(nombre)
print(amigos)

# Versión 2 con un conjuntos:
amigos2 = set()
nombre=''
while nombre !='fin':
    nombre = input('nombre:>')
    if nombre != 'fin':
        amigos2.add(nombre)
print(amigos2)



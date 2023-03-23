"""
Pruebas con conjuntos. 
"""

# Versión 3 con un conjuntos y control de mayúsculas / minúsculas:
print('\nVERSION 3:')
amigos2 = set()
nombre=''
while nombre.lower() != 'fin':
    nombre = input('nombre:>')
    if nombre.lower() != 'fin':
        amigos2.add(nombre.capitalize()) # Añade el nombre al conjunto con la primera letra en mayúsculas.
print(amigos2)

print('\nVERSION 4:')
amigos2 = set()
nombre=''
while nombre != 'Fin':
    nombre = input('nombre:>')
    nombre = nombre.capitalize()
    if nombre != 'Fin':
        amigos2.add(nombre) # Añade el nombre al conjunto con la primera letra en mayúsculas.
print(amigos2)
"""
Tuplas en python
Listas de tuplas
En el SQL parametrizado: 
select * from clientes where pais=? (Las ? se alimentan con tuplas)
execute("select * from clientes where pais=?", ('Suiza',))
EL resultado de una consulta SQL es una lista de tuplas
Parámetros a las funciones
Expansión de tuplas
"""

def suma(a,b):
    return a+b

# Definición:
t = (1,2,3,4)
t2 = 5,6,7,8

print(t, type(t))
print(t2, type(t2))

# Crear una tupla de un solo valor:
t = 6,
print(t, type(t))

# Operadores en tuplas:
print(t * 10)
print(t + (1,2,3))
print(8 in (1,4,5,6,7,8))

for i in t+t2:
    print(i)

t = tuple(range(10))
print(t)
print(t.count(5))

# Inicialización múltiple:
a,b = 1,2
print('a',a,'b',b)

# Intercambiar variables: en otros lenguaje: aux = a; a=b; b=aux
a,b = b,a
print('a',a,'b',b)

# Formas de llamar a una función:
# 1) Parámetros posicionales
print(suma(3,4))

# 2) De forma nominal:
print(suma(b=4, a=3))

# 3) Con una tupla:
t = (3,4)
print(suma(t[0], t[1])) # Muy largo para python!
print(suma(*t)) # Expande la tupla a los parámetros de la función

# 4) Diccionario:
d = {"a":3, "b":4}
print(suma(**d)) # Expande el diccionario

# 5) Listas:
L = [3,4]
print(suma(*L))


def dictToCSV(nombre,edad,altura):
    return nombre+";"+str(edad)+";"+str(altura)

L = [{'nombre':'Juan','edad':45, 'altura':1.88},
    {'nombre':'Ana','edad':33, 'altura':1.78},
    {'nombre':'Pedro','edad':66, 'altura':1.68}
    ]

csv = ""
for d in L:
    csv += dictToCSV(**d)+"\n"
print(csv)


print("\nPrueba 1")
L = [('Ana',34,1.66), ('Jorge',12,1.44), ('Gema',55,1.77)]
for nom, edad, altura in L:
    print(nom, edad, altura)


print("\nPrueba 2")
L = [('Ana',34,1.66,91292929), ('Jorge',12,1.44, 600606050), ('Gema',55,1.77,'Calle Gran Via',34,'madrid',28022)]
for t in L:
    nombre, edad, *resto = t  # Lo que sobra de la tupla cargaló en una Lista
    print(nombre, edad, resto)

print("\nPrueba 3")
L = [('Ana',34,1.66,91292929), ('Jorge',12,1.44, 600606050), ('Gema',55,1.77,'Calle Gran Via',34,'madrid',28022)]
for t in L:
    nombre, edad, *_ = t # *_ Ignora todo lo que sobra de la tupla!
    print(nombre, edad)
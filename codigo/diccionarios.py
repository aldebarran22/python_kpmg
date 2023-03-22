"""
Diccionarios en Python: definición, funciones, acceso a los elementos ...
"""

# definición: {key1: value1, key2: value2, key3: value3}
d = {"uno":1, "dos":2, "tres":3}

# Acceso:
print(d['uno'])
print(d['tres'])

# Añadir clave:
d['cuatro']=4
print(d, type(d))

d['uno']=100
print(d)

# Existe o no un elemento (clave)
clave = 'cinco'
if clave in d:
    print(f'la clave {clave} tiene el valor {d[clave]}')
else:
    print(f'la clave {clave} no existe')

# Buscar un valor en vez de una clave:
sValor = input('Dame un valor')
if sValor.isnumeric():
    # Si es un número lo convierto a número
    valor = int(sValor)
else:
    valor = sValor

if valor in d.values():
    print(f'El valor {valor} SI está en el dict')
else:
    print(f'El valor {valor} NO está en el dict')

productos = ["Libro", "HP", "Ratón","Teclado"]
precios = [40.0, 450.0, 12.5, 30.0]
d2 = dict() # Crea un diccionario vacío
for i in range(min(len(productos), len(precios))):
    # imprimir los productos y los precios:
    k = productos[i]
    v = precios[i]
    print(k, v)
    d2[k] = v
print(d2)

# Otra forma de crearlo:
d3 = dict(zip(productos, precios))
print(d3)

# Incrementar en un 20% el precio del HP:
porc = 20
# miDicc[clave] = valor
d3['HP'] = d3['HP'] * (porc / 100 + 1)
print(d3)

# Escribir en la variable:
# var = valor
d3['HP'] = 1000

# Leer de las variables:
# print(var)
# var2 = var * 100
print(d3['HP'])

# Recorrer un diccionario con un for:
for producto, precio in d3.items():
    print('Producto', producto,'con un precio de', precio)

print('items: ', d3.items())
print('keys: ', d3.keys())
print('values: ', d3.values())

# Invertir el diccionario d3: la clave pasan a ser valores, y los valores a las claves:
d4 = dict(zip(d3.values(), d3.keys()))
print(d4)
print(d4[12.5])


precios2 = d3.values()
productos2 = d3.keys()
d4 = dict(zip(precios2, productos2)) 
print(d4)

L = [{"nombre":'Jose',"tno":60606050}, 
     {"nombre":'Ana', "tno":91382828},
     {"nombre":"Miguel","tno":91324002}
     ]

print(L)
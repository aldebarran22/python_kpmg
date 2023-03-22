"""
Pruebas con cadenas:
"""

s = "hola"
s2 = 'hola'

print(s, type(s))
print(s2, type(s2))

# Uso de metacaracteres:
print('hola\tadios')
print('hola\nadios')

# cadenas raw:
print(r'hola\tadios')
print(r'hola\nadios')

# f-string: para impresión formateada
print('EL valor de s es: ',s)
print(f'El valor de s es: {s}')

fichero = "libro1"
path = f"C:/mis documentos/{fichero}.xlsx"
print(path)

# Operadores: + y *
nombre = "Juan"
ape1 = "Sanz"
nombre_completo = nombre + " " + ape1 # Concatenación
print(nombre_completo * 4)


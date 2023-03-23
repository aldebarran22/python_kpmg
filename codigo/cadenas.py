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

# Conversiones de may, minus, etc.
print('\n\n\n')
nombre = "juan sanz gomez"
# OJO, que NO se cambia la variable nombre. 
print(nombre)
print(nombre.upper())
print(nombre.capitalize())
print(nombre.title())
print(nombre)

# Para cambiar la variable nombre:
nombre = nombre.title()
print('Nombre cambiado: ', nombre)
print('Prueba con Lower: ', "HOLA".lower())


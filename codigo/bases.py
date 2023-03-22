"""
Pruebas con cambios de base en python:
binario, octal y hexadecimal
"""

n = 123
print(n, hex(n), oct(n), bin(n))

# Otra forma de hacer lo mismo:
print(format(n,'x'), format(n, 'o'), format(n, 'b'))

# Convierte de texto a entero pero en este indicamos la base:
num = int("0xFF", 16)
print(num)
print(print('hola'))
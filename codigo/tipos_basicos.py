"""
Pruebas con los tipos básicos y cambios de tipos
"""

numero = 234
print(numero, type(numero))

numero2 = "456"
print(numero2, type(numero2))
# Convertimos la var. numero2 a int
print(numero + int(numero2))

# Convertimos a str:
print(str(numero)+numero2)

# No es una buena práctica cambiar el tipo de la variable
numero2 = 34
# Con la contrabarra se pueden partir las instrucciones en python
print(numero2, \
       type(numero2))
print(numero + numero2)

if numero != numero2:
    print('los numeros son distintos')



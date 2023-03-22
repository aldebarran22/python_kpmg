"""
Calcular las soluciones de una ecuación de 2 grado
"""

import math

numero = 25
print(f'La raíz de {numero} es {math.sqrt(numero)}')

# El cálculo de la raíz: x^2 +  5x + 4 = 0
# a,b,c = 1,5,4
a = 1
b = 5
c = 4

# Inicialización múltiple (tuplas)
a,b,c=1,2,3

raiz = b**2 - 4 * a * c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print("x1:",x1,"x2:",x2)
else:
    print('No hay solución')
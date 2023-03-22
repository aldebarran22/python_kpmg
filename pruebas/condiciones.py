"""
Prueba con operadores relaciones y logicos
"""

n = 14
if n >= 10 and n <= 20:
    print('cumple intervalo ...')
else:
    print('No lo cumple')

if 10 <= n <= 20:
    print('cumple intervalo ...')
else:
    print('No lo cumple')

if n < 10 or n > 20:
    print('No cumple el intervalo')
else:
    print('Si lo cumple')

if not (n >= 10 and n <= 20):
    print('No cumple el intervalo')
else:
    print('Si lo cumple')
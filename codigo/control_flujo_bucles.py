"""
Pruebas con los bucles: for, while
"""

# Ejecutar el bucle 10 veces: range(ini, fin-1, salto)
for i in range(10):    
    for j in range(10):
        print(i, j)


# Calculando sumar parciales (por filas) y la suma total
L = [[1,2,3],[4,5,6],[7,8,9]]
suma = 0
for i in L:
    print(i, sum(i))
    suma += sum(i) # suma = suma + sum(i)
    print('Suma acumulada: ', suma)
print('suma total: ', suma)

# Imprimir las filas que sumen más de un valor leído de teclado:
valor = int(input('Dame el valor minimo:'))
for i in L:
    sumaFila = sum(i)
    if sumaFila > valor:
        print(i, sumaFila)


# Bucle While:
"""
Bucle infinito
while True:
    print('hola')
"""

"""
for i in range(10):
    print(i)
"""

i = 0
while i < 5:
    print(i)
    i+=1






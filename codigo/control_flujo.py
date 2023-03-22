"""
Instrucciones de programación estructurada: if, while, for
"""

L = [3,5,6,7,1,2,4,5,67]

# Imprimir sólo los números impares:
for i in L:
    if i % 2 != 0:
        print(i, end=' ')

# Sumar solo los pares:
print('Suma total: ', sum(L))
suma = 0
for i in L:
    if i % 2 != 0:
       suma = suma + i 
print("suma de impares: ", suma)
print("suma de los pares: ",sum(L)-suma)

# Calcular el porcentaje de cada sumatorio:
print('Porcentaje de impares: ', suma / sum(L) * 100, '%')
print(f'Porcentaje de impares: {round(suma / sum(L) * 100, 2)}%')

# Separar los números pares e impares en dos listas distintas:
pares = []
impares = []
for i in L:
    if i % 2 != 0:
        impares += [i]
    else:
        pares += [i]

print('impares: ', impares)
print('pares:', pares)

# Calcular la media de los números pares e impares: sum, min, max, len
print('Media impares:', round(sum(impares)/len(impares),2))
print('Media pares: ', round(sum(pares)/len(pares),2))

 
# Cuanto suman los 4 primeros números de la lista: slicing[ini:fin-1:salto]
print(L)
print('La suma de los 4 primeros: ', sum(L[:4]))
for i in L[:4]:
    print(i)






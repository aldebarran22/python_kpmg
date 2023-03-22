"""
Condiciones en Python
"""

n1 = 23
n2 = 23

# Guardar en una variable el  número menor:
if n1 < n2:
    menor = n1
elif n2 < n1:
    menor = n2
else:
    print('Las var. son iguales')

menor2 = min(n1, n2)    
print('menor2: ', menor2)

# Calcular el menor de 3 números:
n3 = 45
menor3 = min(n1,n2,n3)   # min(n1, min(n2,n3))

# Imprimir un número es par o impar: n1
if n1 % 2 == 0:
    print('par')
else:
    print('impar')

print("par" if n1 % 2 == 0 else "impar")

# Ejemplo de continue: Sirve para saltar iteraciones:
# Imprimir valores entre -5 y 5 pero el 0 no nos interesa
for i in range(-5,6):    
    if i == 0:
        continue
    print(i, end=' ')


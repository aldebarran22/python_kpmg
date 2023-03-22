"""
Operadores lógicos y relacionales en Python
"""

# Comprobar si una variable cumple el rango:
numero = 24

if numero >= 1 and numero <= 50:
    print('Cumple el rango 1-50')
else:
    print('No cumple el intervalo')

if  1 <= numero <= 50:
    print('Cumple el rango 1-50')
else:
    print('No cumple el intervalo')    

if not (numero >= 1 and numero <= 50):
    print('No cumple el intervalo')
else:
    print('Cumple el rango 1-50')

if numero < 1 or numero > 50:
    print('No cumple el intervalo')
else:
    print('Cumple el rango 1-50')  


# Operadores a nivel de Bits:
a = 0x0F  # 0000 1111
b = 0xF0  # 1111 0000
print("a & b:", a & b)    
print("a | b:", a | b, hex(a | b))    

a = 0xAA # 1010 1010
print('a ^ b: ', a^b, bin(a^b)) # Si son iguales los bits da 1, si son distintos 0

# Desplazamientos: 
# numero << n-bits -->  a multiplicar numero por 2^n-bits
a = 0x0F # 0000 1111
a = a << 3 # 0111 0000 Equivale a mult. por 2^3
print(a, hex(a), bin(a))

# numero >> n-bits -->  a dividir numero por 2^n-bits
a = 0x0F # 0000 1111
a = a >> 3 # 0000 0001 Equivale a div. por 2^3
print(a, hex(a), bin(a))
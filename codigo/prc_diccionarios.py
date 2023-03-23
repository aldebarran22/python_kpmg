"""
Prácticas con diccionarios. 
"""

# Número de ocurrencias de una letra en un texto:
txt = "Diccionarios en Python: definición, funciones, acceso a los elementos"
recuento = dict()
for letra in txt:
    # Comprobar si está o no la letra en el diccionario
    if letra in recuento:
        # Si esta: incrementar en 1 esa letra
        recuento[letra] += 1
    
    else:
        # Si no esta: se añade al diccionario con el valor 1
        recuento[letra] = 1

print(recuento)

# Cuantas veces se  repite una letra en la cadena txt:
letra = 'n'
cuenta = txt.count(letra)
print(letra,'se repite',cuenta)

for i in "nia":
    print(i, 'se repite',txt.count(i))

# Versión refinada:
recuento2 = dict()
letrasSinRepe = set(txt) # Quitar letras repetidas
for i in letrasSinRepe:
    recuento2[i] = txt.count(i)
print(recuento2)   
print(set(txt)) 

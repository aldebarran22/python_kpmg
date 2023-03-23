"""
Partimos de dos bloques de texto que vienen de ficheros CSV y queremos buscar
duplicados y registros diferentes, etc.
"""

txt="""id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

txt2="""id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;Queen;Representante de ventas
8;Jonh;Coordinador ventas interno
9;Ana;Representante de ventas"""

#print(txt == txt2)

# Partir cada bloque de texto en filas: las filas están separadas por \n
L1 = txt.split('\n')
#print(L1)

L2 = txt2.split('\n')
#print(L2)

# Pasamos las listas a conjuntos quitando previamente las cabeceras:
c1 = set(L1[1:])
c2 = set(L2[1:])
filasComunes = c1 & c2 # Intersección
print("Filas comunes: \n", filasComunes)

# Diferencias: 
# Lineas que tenemos en el primer texto (txt) y que no están en el segundo (txt2)
filastxt1QueNoCoinciden = c1 - c2 # Diferencia
print("\nfilastxt1QueNoCoinciden: \n", filastxt1QueNoCoinciden)

todasLasFilasSinRepes = c1 | c2 # La unión
print('\nFilas sin repes:\n', todasLasFilasSinRepes)


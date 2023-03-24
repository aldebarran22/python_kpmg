"""
Funciones para grabar pedidos en ficheros
"""

def cargarFichero(path):
    """
    Carga el fichero que recibe por parámetro y lo devuelve como texto
    """
    fichero1 = open(path,"r")
    txt = fichero1.read()
    fichero1.close()
    return txt

def grabarPedidosPorPais(texto, pais):
    """
    Genera un archivo de pedidos de un determinado país
    """
    nombreFichero = f"Pedidos_{pais}.csv"
    #print(nombreFichero)
    LFilas = []
    
    L = texto.split('\n')
    LFilas.append(L[0]+"\n")

    for i in L[1:]:            
        fila = i.split(';')
        if fila[5] == pais:
            LFilas.append(i+"\n")

    # grabar el fichero:
    f = open(nombreFichero, "w")
    f.writelines(LFilas)
    f.close()

    return len(LFilas)

txt = cargarFichero('Pedidos.csv')
numFilas = grabarPedidosPorPais(txt, 'Austria')
print('numFilas: ', numFilas)


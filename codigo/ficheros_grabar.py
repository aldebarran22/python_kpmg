"""
Ejemplo para crear un fichero:
a --> append: añade líneas al final del fichero
w --> write: cada vez que se ejecuta crea de nuevo el fichero 
"""

f = open("demofile3.txt", "w")
f.writelines(["nombre;edad;telefono\n",
              "Laura;45;907077070\n",
              "Ricardo;34;900077060"])
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
f.close()
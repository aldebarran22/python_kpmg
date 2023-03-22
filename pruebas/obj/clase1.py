
class Clase1:
	
	def __init__(self, nombre="", edad=0):
		self.nombre = nombre
		self.edad = edad
		
	def __str__(self):
		return self.nombre + ", " + str(self.edad)
		
		
class Clase2(Clase1):
	
	def __init__(self, nombre="", edad=0):
		nombre *= 2
		edad *= 10
		
		Clase1.__init__(self, nombre, edad)
		

if __name__=="__main__":
	
	c2 = Clase2("Julia", 45)
	print(c2)
	

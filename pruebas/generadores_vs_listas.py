def generadorPrimos(ini, fin, salto):
	
	def esPrimo(num):
		for i in range(2,num):
			if num%i==0:
				return False
		return True	
		
	i = ini
	while i < fin:
		if esPrimo(i):
			yield i
		i+=salto
		
def listaPrimos(ini, fin, salto):
	
	def esPrimo(num):
		for i in range(2,num):
			if num%i==0:
				return False
		return True	
		
	L = []
	i = ini
	while i < fin:
		if esPrimo(i):
			L.append(i)
		i+=salto
	return L

print('Lista')		
for i in listaPrimos(19999900,20000000,1):
	print(i)
	
print('Generador')	
for i in generadorPrimos(19999900,20000000,1):
	print(i)

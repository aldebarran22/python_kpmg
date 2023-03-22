myGlobal = 5

def func1():
    #global myGlobal    
    myGlobal = 42

def func2():
    print (myGlobal)

func1()
func2()



# datos globales:
num = 234
L=[1,2,3]


def funcion():
	print("num:",num)
	print("L:",L)
	
def funcion2():
	global num,L
	num+=2
	L+=[45]
		
def funcion3():
	L.append(8)	
	
funcion()
funcion2()
funcion()
funcion3()
funcion()

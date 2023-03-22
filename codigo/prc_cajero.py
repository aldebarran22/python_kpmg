"""
Simular el comportamiento de un cajero:
Importe:> 44
incorrecto, teclear un múltiplo de 10
Importe:> 33
incorrecto, teclear un múltiplo de 10
Importe:> 200
ok

200
4 de 50 euros

230
4 de 50 euros
1 de 20 euros
1 de 10 euros

40
2 de 20 euros
"""
billetes = [10, 5, 20, 50]
# Ordenar los billetes desc.
billetes.sort(reverse=True)
billeteMin = min(billetes)  # billeteMin = billetes[-1]
while True:
    importe = int(input('Importe:>'))    
    while importe % billeteMin != 0:        
        print('incorrecto, teclear un múltiplo de',billeteMin)
        importe = int(input('Importe:>'))
    for b in billetes:
        if importe >= b:
            numBilletes = importe // b
            importe = importe % b # importe %= b
            print(numBilletes,'de',b,'euros')
            if importe == 0:
                break
        
  
"""
while True:        
    importe = int(input('Importe2:>'))
    if importe % 10 != 0:
        print('incorrecto, teclear un múltiplo de 10')
    else: 
        break # Rompe el bucle
"""    
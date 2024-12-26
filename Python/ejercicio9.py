
numeros = range(1, 6)
acumulador  = 0

for numero in numeros:
    print(f'{acumulador} + {numero}')
    acumulador += numero
    
print(f'La suma de los primeros 5 numeros es {acumulador}')
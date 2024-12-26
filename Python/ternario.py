# Sentencia if-else en Python
mi_numero = int(input('Proporciona un numero: '))
# Revisar si el numero es mayor que cero
if mi_numero > 0:
    print(f'Valor positivo: {mi_numero}')
else:
    print(f'Valor cero o negativo: {mi_numero}')
    
    
#Optimizacion del codigo a una sola linea    
print('Positivo') if mi_numero > 0 else print('Cero o negativo')
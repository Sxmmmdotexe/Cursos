import math

numero_str = input('ingrese un numero')
numero = int(numero_str)

if numero > 0 and numero < 10 :
    print('Son unidades')
elif numero >= 10 and numero < 100 :
    print('Son decenas')
elif numero >= 100 and numero < 1000 :
    print('son centenas')
else:
    print('no esta contemplado')
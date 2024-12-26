import random
import math

cadena = 'Hola'
#len es para obtener la longitud, proviene de length en ingles
print(f' largo cadena : {len(cadena)}')

print(cadena[0])


#recorrer elementos de una cadena
#enumerate, enumera los caracteres que se estan recorriendo en este caso
for caracter in enumerate(cadena):
    print(caracter)
    
for indice, caracter in enumerate(cadena):
    print(f'{indice} - {caracter}')    
    
#subcadenas, manejo de listas
cadena = 'Hola mundo'
subcadena = cadena[0:4]
print(f'subcadena : {subcadena}')

subcadena1 = cadena[5:10]
print(f'Subcadena 1 : {subcadena1}')


#concatenacion
cadenaconcatenacio =  'hola'
cadenaconcatenacio1 = 'mundo'

print(f'concatenacion : {cadenaconcatenacio} {cadenaconcatenacio1}')

#convertir cadena a numero 
a,b = 1,2
print(f'valor a : {a} valor b : {b} = {a}+{b} = {a+b}')

x,y = '10', '15'
print(f'valor x : {x} valor y : {y} = {x + y}')
suma = int(x) + int(y)
print(suma)

#convertir numero a cadena
a,b = 1, 2
print(a+b)

concat = str(a) + str(b)
print(concat)

#.__str__() es el metodo de representacion de la cadena metodo rep 
#el doble guion bajo significa dunder, es un metodo especial de python
concat = a.__str__() + b.__str__()
print(concat)

concat = a.__repr__() + b.__repr__()
print(concat)

#generar valores aleatorios, para eso necesitamos importar la libreria "random"
maximo = 1000
minimo = 500
#generar un valor aleatorio entre minimo y maximo
#hay que especificar correctamente los valores minimos y maximos, minimos del lado izquierdo y maximo del lado derecho
print(random.randint(minimo,maximo))


#vlores absolutos
numero = int(input('Ingrese un valor: '))
print(abs(numero))

#redondear valores al par mas cercano 
numero = 9.5 
print(round(numero))

#para truncado hay que importar la libreria math
truncado = math.trunc(numero)
print(truncado)

#la funcion agrega floor redondea hacia abajo
floor = math.floor(numero)
print(floor)

#ceil redondea hacia arriba
ceil = math.ceil(numero)
print(ceil)
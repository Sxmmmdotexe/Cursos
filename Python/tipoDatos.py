#Tipos de datos aceptados por python

#estas son consideradas variables globales

#Existe la funcion typeOf que muestra el tipo de dato de la variable

#Las variables en realidad apuntan a una instancia del objeto en memoria. Es decir ya existen las variables en memoria antes de que se creen en el programa.

mi_entero = 10
otro_entero = 20
print('Entero = ', mi_entero, type(mi_entero), id(mi_entero),hex(id(mi_entero))) #Imprime el valor de la variable entero
print(otro_entero, id(otro_entero))

mi_flotante = 2.3
print('Flotante = ', mi_flotante, type(mi_flotante)) #Imprime el valor de la variable flotante

mi_cadena = 'Hello world'
print('Cadena = ', mi_cadena, type(mi_cadena)) #Imprime el valor de la variable cadena 

#para los bool, los valores tienen que ser en mayusuculas T para True o F para False
mi_bool = False
print('Booleano = ', mi_bool, type(mi_bool)) #Imprime el valor de la variable bool

#ausencia de valor , es decir, None
mi_nulo = None
print('Nulo = ', mi_nulo, type(mi_nulo)) #Imprime el valor de la variable nulo


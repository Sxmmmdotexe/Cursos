#nombre = input('Proporciona tu nombre: ')
#curp = input('Proporcione su CURP: ' )
#print('Tu nombre es: ', nombre)

#este es mas funcional para cadeans mas complejas o mas largas
#print(f'Hola {nombre} {curp}')

#este sigue siendo valido pero es mas utilizado en cosas simples. (podria ser como pruebas unitarias)
#print('Hola', nombre, curp)


numero_str = input('Proporciona un numero entero: ')
print(f'El numero {numero_str} es de tipo {type(numero_str)}')

#lo convertimos a entero
numero = int(numero_str)

print(f'El numero {numero} es de tipo {type(numero)}')


#obtenemos directamente un valor entero
entero = int(input('Ingresa un entero'))
print(f'El entero {entero} es de tipo {type(entero)}')

#si queremos cambiar el tipo de dato solo basta con colocar el tipo de dato que queremos int, float, str, bool, etc
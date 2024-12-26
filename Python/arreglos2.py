cadena = 'adios' * 3

no_elementos = int(input('No. elementos del array'))

arreglo= [0] * no_elementos

for indice in range(no_elementos):
    valor = int(input(f'Arreglo [{indice}]: '))
    arreglo[indice] = valor

print('imprimimos de otra forma la lista')
for indice in range (len(arreglo)):
    print(f'arreglo[{indice}] = {arreglo[indice]}')
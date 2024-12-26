renglones = int(input('Ingrese la cantidad de renglones: '))
columnas = int(input('Ingrese la cantidad de columnas: '))

matriz = [0] * renglones
for ren in range(renglones):
    #por cada renglon asiganmos una lista de m columnas
    matriz[ren] = [0] * columnas

#print(matriz)
for ren in range(renglones):
    for col in range(columnas):
        matriz[ren][col] = int(input(f'Ingrese el valor para la posicion [{ren}][{col}] = '))
        
        print(matriz)
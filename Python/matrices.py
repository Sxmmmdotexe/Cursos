#matrices (listas de listas)

matriz = [[100,200,300],[400,500,600]]


renglones = len(matriz)
columnas = len(matriz[0])

for ren in range(len(matriz)):
    for col in range(len(matriz[ren])):
        print(f'matriz[{ren}][{col}] = {matriz[ren][col]} ')


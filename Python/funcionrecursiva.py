def funcion_recursiva(numero):
    if numero == 1:
        print(numero)
    else:
        funcion_recursiva(numero -1 )
        print(numero)
        
funcion_recursiva(3)
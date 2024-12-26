varglobal = 10
a = 40

def mi_funcion(varlocal):
    print(varlocal)
    
    #cualquier cambio posterior no afecta a la variable global
    #acceder a la variable global
    global a
    a = 30
    print(a)
    
print(varglobal)
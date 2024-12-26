def sumar (a,b):
    resultado_suma = a + b
    return resultado_suma

arg_a = int(input('Valor a: '))
arg_b = int(input('valor v: '))

resultado = sumar(arg_a, arg_b)
print(f'El resultado de la suma es: {resultado}')
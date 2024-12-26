import datetime

current_year = datetime.datetime.now().year

anio_nacimiento = int(input('Ingrese su anio de nacimiento'))
edad = current_year - anio_nacimiento

print('es mayor de edad') if current_year - anio_nacimiento >= 18 else print('es menor de edad')
print(edad)
telefono = input("Introduzca el número de teléfono con formato '+prefijo(2)-número(9)-extension(2)': ")
numero = telefono.split("-")
print(numero[1])

nombre = input("Introduzca el nombre de un producto: ")
precioStr = input("Introduzca el precio del producto: ")
unidades = int(input("Introduzca las unidades del producto: "))

if "," in precioStr:
    precioStr = precioStr.replace(",", ".")
if "'" in precioStr:
    precioStr = precioStr.replace("'", ".")

precio = float(precioStr)

coste = precio * unidades

print(f"Nombre:{nombre} \nPrecio:{precio:6.2f} \nUnidades: {unidades:3d} \nCosteTotal:{coste:8.2f}")
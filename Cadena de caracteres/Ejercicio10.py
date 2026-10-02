lista = input("Escriba los productos de la cesta separados por comas: ")
productos = lista.split(",")

for i in range(0, len(productos)):
    print(productos[i].strip())

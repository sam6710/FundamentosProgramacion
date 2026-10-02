precio = input("Introduzca el precio en euros del producto con dos decimales: ")
if "," in precio:
    precioArray = precio.split(",")
if "." in precio:
    precioArray = precio.split(".")
if "'" in precio:
    precioArray = precio.split("'")
print(f"{precioArray[0]}")
print(f"{precioArray[1]}")


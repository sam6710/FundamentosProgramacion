edad = int(input("Escriba su edad: "))
ingresos = input("Escriba sus ingresos: ")

if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")
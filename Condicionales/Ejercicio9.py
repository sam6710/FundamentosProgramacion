edad = input("Escriba su renta anual: ")

if edad < 4:
    print("Entra gratis.")
elif edad >= 4 < 18:
    print("Debe pagar 5€.")
else:
    print("Debe pagar 10€.")
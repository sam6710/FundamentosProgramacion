edad = input("Introduzca su edad: ")

if edad < 4:
    print("Entra gratis.")
elif edad >= 4 <= 18:
    print("Debe pagar 5€.")
elif edad >18:
    print("Debe pagar 10€.")
else:
    print("No puedes tener una edad negativa.")
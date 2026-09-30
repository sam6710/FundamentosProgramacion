nombre = input("Introduzca su nombre completo: ")
nombreCompleto = ""

print(nombre.upper())
print(nombre.lower())

palabras = nombre.split()
for palabra in palabras:
    palabra=palabra.capitalize()
    nombreCompleto+=palabra + " "

print(nombreCompleto)

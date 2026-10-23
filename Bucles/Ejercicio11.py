palabra = input("Introduzca una palabra: ")

lista = list(palabra[::-1])

for letra in lista:
    print(letra)
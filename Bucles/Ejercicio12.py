frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

cant = 0
lista = list(frase)

for i in range (0, len(frase)):
    if lista[i] == letra:
        cant = cant+1
print(cant)
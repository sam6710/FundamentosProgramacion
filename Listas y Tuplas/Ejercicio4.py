numeros = []

for i in range (0,6):
    n_ganador = int(input("Introoduzca un número ganador de la primitiva: "))
    numeros.append(n_ganador)

numeros.sort()

for num in numeros:
    print(str(num) + " ", end = "")
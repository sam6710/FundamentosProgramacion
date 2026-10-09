sexo = input("Escriba su sexo (M/F): ")
nombre = input("Escriba su nombre: ")

inicial = nombre[:1]

if (sexo == "F" and  inicial < "M") or sexo == "M" and inicial > "N":
    print("Grupo A")
else:
    print("Grupo B")
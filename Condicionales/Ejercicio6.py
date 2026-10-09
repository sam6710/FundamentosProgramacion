sexo = input("Escriba su sexo (M/F): ")
nombre = input("Escriba su nombre: ")

inicial = nombre[:1]

print(inicial)

if (sexo.upper() == "F" and  inicial.upper() < "M") or (sexo.upper() == "M" and inicial.upper() > "N"):
    print("Grupo A")
else:
    print("Grupo B")
pesoPayaso = int(112)
pesoMunheca = int(75)

payasos = int(input("Introduzca la cantidad de payasos vendidos: "))
munhecas = int(input("Introduzca la cantidad de muñecas vendidas: "))

pesoTotalPayasos = pesoPayaso * payasos
pesoTotalMunhecas = pesoMunheca * munhecas

pesoTotal = pesoTotalMunhecas + pesoTotalPayasos

print(f"El peso total del paquete es de {pesoTotal} gr.")
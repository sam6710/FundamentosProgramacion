cant = float(input("Introduzca cantidad a invertir: "))
interes = float(input("Introduzca el interés anual: "))
anhos = int(input("Introduzca cantidad de año: "))

sumaInteres = cant*(interes/100)

for i in range(0, anhos):
    cant = cant + sumaInteres
    print(f"Suma del año {i+1}: {cant}")
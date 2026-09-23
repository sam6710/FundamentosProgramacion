cantidad = float(input("Introduzca cantidad a invertir: "))
interes = float(input("Introduzca porcentaje interés: "))
anhos = float(input("Introduzca cantidad de años: "))

capital_final = cantidad * (1 + interes / 100) ** anhos

print(f"El capital obtenido al final de los {anhos} años es: {round(capital_final, 2)}")

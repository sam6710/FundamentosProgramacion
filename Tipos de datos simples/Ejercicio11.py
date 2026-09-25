interes = int(4)
anhos = int(3)
dinero = float(input("Introduzca la cantidad de dinero de la cuenta: "))


ahorrosAnho1 = dinero*(1+interes/100)*1
ahorrosAnho2 = dinero*(1+interes/100)**2
ahorrosAnho3 = dinero*(1+interes/100)**3

print(f"Los ahorros tras los primeros 3 años han sido; {round(ahorrosAnho1,2)} , {round(ahorrosAnho2,2)} y {round(ahorrosAnho3,2)}.")
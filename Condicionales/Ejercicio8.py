rendimiento = float(input("Indique el nivel de rendimiento:"))

if rendimiento == 0.0:
    print("Tu rendimiento es inaceptable.")
    print(f"Tu nivel de rendimiento es {rendimiento} y la cantidad de dinero que recibirás por él es {2400*rendimiento}€.")
elif rendimiento == 0.4:
    print("Tu rendimiento es aceptable.")
    print(f"Tu nivel de rendimiento es {rendimiento} y la cantidad de dinero que recibirás por él es {2400*rendimiento}€.")
elif rendimiento >= 0.6:
    print("Tu rendimiento es meritorio.")
    print(f"Tu nivel de rendimiento es {rendimiento} y la cantidad de dinero que recibirás por él es {2400*rendimiento}€.")
else:
    print("Ese rendimiento no se contempla en el programa.")
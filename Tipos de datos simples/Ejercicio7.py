peso = float(input("Peso(kg): "))
estatura = float(input("Estatura(m): "))
imc = peso/(estatura)**2
print(f"Tu índice de masa corporal es: {round(imc,2)}")
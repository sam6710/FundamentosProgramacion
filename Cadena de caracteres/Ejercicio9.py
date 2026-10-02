fecha = input("¿Cual es tu fecha de nacimiento(dd/mm/aaaa)?: ")
splitedFecha = fecha.split("/")
print(f"El día {splitedFecha[0]} del mes {splitedFecha[1]} del año {splitedFecha[2]}")
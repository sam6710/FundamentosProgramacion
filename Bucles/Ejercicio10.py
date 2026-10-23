num = int(input("Introduzca un número entero positivo: "))

primo = True
divisor = 2

while divisor < num:
    if num % divisor == 0:
        primo = False
        break
    divisor += 1

if primo:
    print("Es primo")
else:
    print("No es primo")
precio = float(3.49)
precioPanDdescuento = float(precio*0.4)

barrasMalasVendidas = int(input("¿Cuántas barras de pan que no son del día se han vendido?"))

costeFinal = (barrasMalasVendidas*precioPanDdescuento)

print(f"El precio habitual de la barra es: {precio}")
print(f"El descuento de la barra es: {round(precio*0.6,2)}")
print(f"El coste final es: {round(costeFinal,2)}")

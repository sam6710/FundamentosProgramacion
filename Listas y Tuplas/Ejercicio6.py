asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
asignaturas2 = asignaturas

for i in range (0,len(asignaturas)):
    nota = int(input(f"Introduzca la nota de: "))
    if nota < 5:
        asignaturas.pop(i)
        # asignaturas.remove(borrada)
    else:
        notas.append(nota)

# for i in range (0, len(notas)):
#     if i >= 5:
#         del asignaturas[i]

print(asignaturas)
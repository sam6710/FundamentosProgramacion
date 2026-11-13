asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"Introduzca la nota de {asignatura}: ")
    notas.append(nota)

for i in range (0, len(notas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}.")
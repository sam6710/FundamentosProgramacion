asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"Introduzca la nota de {asignatura}: ")
    print(f"En {asignatura} has sacado {nota}.")
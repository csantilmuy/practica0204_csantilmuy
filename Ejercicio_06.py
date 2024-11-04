# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al
# usuario la nota que ha sacado en cada asignatura y elimine de la lista las
# asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
# asignaturas que el usuario tiene que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []
for asignatura in asignaturas:
    nota = float(input(f"Nota sacada en {asignatura}: "))
    if nota < 5:
        repetir.append(asignatura)
if repetir:
    print("Asignaturas a repetir:" , ", ".join(repetir))
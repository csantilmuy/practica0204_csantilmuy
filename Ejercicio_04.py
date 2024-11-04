# Escribir un programa que pregunte al usuario los números ganadores de la
# lotería primitiva, los almacene en una lista y los muestre por pantalla
# ordenados de menor a mayor.
n_ganadores = []
for i in range(5):
    números = int(input(f"Ingrese el número ganador {i + 1}: "))
    n_ganadores.append(números)
n_ganadores.sort()
print("Los números ganadores ordenados son:", n_ganadores)
# Escribir un programa que pregunte por una muestra de números, separados por
# comas, los guarde en una lista y muestre por pantalla su media y desviación
# típica.
números = list(map(float, input("Escribe una muestra de números separados "
                                "por comas: ").split(",")))
media = sum(números) / len(números)
desviación = (sum((x - media) ** 2 for x in números) / len(números)) ** 0.5
print("Media:", media)
print("Desviación típica:", desviación)
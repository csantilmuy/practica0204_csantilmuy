# Escribir un programa que pida al usuario una palabra y muestre por pantalla
# si es un palíndromo.
palabra = input("Escribe una palabra: ")
if palabra.lower() == palabra.lower()[::-1]:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
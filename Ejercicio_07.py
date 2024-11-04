# Escribir un programa que almacene el abecedario en una lista, elimine de la
# lista las letras que ocupen posiciones múltiplos de 3, y muestre por
# pantalla la lista resultante.
abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
resultante = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
print("Lista resultante:", resultante)
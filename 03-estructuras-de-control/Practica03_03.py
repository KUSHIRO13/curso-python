# Librerias
import random

# Listas

par = []
impar = []
numero = (1, 2, 3, 4, 5, 6, 7, 8, 9)


"""
print(numero_random)

mul = numero * numero_random
"""

for multi in numero:
    numero_random = random.randint(1, 100)
    resultado = multi * numero_random
    if resultado % 2 == 0:
        print(f"{multi} x {numero_random} da : {resultado}")
        par.append(resultado)
    else:
        print(f"{multi} x {numero_random} da : {resultado}")
        impar.append(resultado)

print("La lista de pares es: ", par)
print("La lista de impares es: ", impar)

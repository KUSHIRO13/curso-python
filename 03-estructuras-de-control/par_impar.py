"""
if False:
    print("Se cumple la condicion")
else:
    print("No se cumple la condicion")
"""
n = int(input("Ingrese un numero entero: "))
# Saber si el numero es par o impar
if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f"El numero {n} es par positivo")
        else:
            print(f"El numero {n} es impar positivo")
    else:
        if n % 2 == 0:
            print(f"El numero {n} es par negativo")
        else:
            print(f"El numero {n} es impar negativo")
else:
    print(f"El es numero {n} es neutro")

def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs


suma_total,datos = sumar(10, 2, 3, 40, 50, 6, 70, 8, 90, nombre="Kushiro", edad=18)
print("La suma total es: ", suma_total)
print(datos)

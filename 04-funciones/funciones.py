

def saludar(nombre):
    # global nombre
    # nombre = "Andres"
    edad = 25
    return f"Hola,{nombre} desde la funcion saludar", nombre, edad
    print("Hola", nombre)


def suma(a, b):
    return a + b


def resta(a= None, b = None):
    if a == None or b == None:
        print("Error debes enviar dos numeros")
        return
    return a - b


"""
valor = saludar()
saludo, nombres, edades = saludar()
print(saludo)
print(nombres)
print(edades)
print(valor)
"""
# print("Hola desde fuera de la funcion", nombre)

sal = saludar(input("Cual es tu nombre? "))
print(sal)

sumas = suma(int(input("Da un numero ")), int(input("Da otro numero ")))
print(f"La suma es: {sumas}")

restar1 = resta(a=15, b=5)

print("La resta es. ", restar1)

resta()
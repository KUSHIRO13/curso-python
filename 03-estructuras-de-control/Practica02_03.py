# Pregunta
compra = float(input("Cuanto gastastastes en este restaurante? "))

impuesto = 1.19

if compra >= 0:
    if compra <= 100:
        descuento = compra * 0.10
        td = "10%"
        valor = compra - descuento
    elif compra >= 100 and compra <= 200:
        descuento = compra * 0.20
        td = "20%"
        valor = compra - descuento
    else:
        descuento = compra * 0.30
        td = "30%"
        valor = compra - descuento

    print("=" * 50)
    print(f"Descuento total de {td}")
    print("=" * 50)
    print(f"Se le descuenta: {descuento}")
    print("=" * 50)
    print(f"Se te suma un impuesto del 19% porciento que da: {impuesto}")
    print("=" * 50)
    print(
        f"Eso quiere decir que la cuenta queda en {valor * impuesto}")
else:
    print("Error al ingresar la compra")

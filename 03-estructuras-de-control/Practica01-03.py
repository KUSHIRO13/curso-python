# Declarar variables
descuento = 0
impuesto = 1.19

compra = float(input(
    "Vas a un restaurante y cuando revisas lo que comprastes te das cuenta que gastastes...: "))

if compra <= 100.00:
    descuento = compra * 0.10
    valor = compra - descuento
    print(
        f"Entonces te damos un descuento del 10% quedando la cuenta en {valor} soles pero por el impuesto que en {valor * impuesto}")
else:
    descuento = compra * 0.20
    valor = compra - descuento
    print(
        f"Entonces te damos un descuento del 20% quedando la cuenta en {valor} soles pero por el impuesto que en {valor * impuesto}")

# Practica 02
print("Quieres saber el igb y el precio de venta de un producto")
# Emprezar
venta = input("Ingrese el valor del producto: ")
# Convertir
venta = float(venta)

igv = venta * 0.18
precio_venta = venta + igv

print(
    f"El igv es: {igv} \ny el precio de venta recomendado es: {precio_venta}")

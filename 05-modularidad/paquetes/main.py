import mi_paquete.aritmeticas as a

def main():
    suma = a.suma(4,5,6,7,8,9,5)
    resta = a.resta(6,5)
    potencia = a.potencia(2,3)

    print(f"""
    La suma es : {suma}
    La resta es: {resta}
    La potecia es: {potencia}""")

if __name__ == "__main__":
    main()
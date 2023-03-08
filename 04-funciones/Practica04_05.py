#Conversor
def conversor(valor_dolar,pais):
    cantidad_monedad = float(input(f"Ingrese cantidad de {pais}: "))

    dolar = cantidad_monedad / valor_dolar
    dolar = round(dolar,2)
    print(f"Tienes ${dolar} dolares")


def main():
    while True:
        menu = """
        1-Pesos Colombianos a Dolares
        2-Soles Peruanos a Dolares
        3-Pesos Mexicano a Dolares
        4-Salir
        Ingrese una Opcion: """
        opcion = input(menu)
        if opcion == "1":
            conversor(4761.00,"Pesos Colombianos")
        elif opcion == "2":
            conversor(3.78,"Soles Peruanos")
        elif opcion == "3":
            conversor(18.11,"Pesos Mexicanos")
        elif opcion == "4":
            print("Cerrando conversor de monedas")
            break
        else:
            print("Opcion incorrecta vuelva a seleccionar")


if __name__ =="__main__":
    main()




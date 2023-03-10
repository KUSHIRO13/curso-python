from personas import Persona

def main():

    persona1 = Persona("Kushiro",18)
    

    persona2 = Persona("Andres",25)

    persona1.mostrar_Datos()
    print("="*30)
    persona2.mostrar_Datos()

    print(persona1)

if __name__ == "__main__":
    main()
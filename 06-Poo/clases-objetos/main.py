from personas import Persona

def main():

    persona1 = Persona()
    persona1.nombre = "Kushiro"
    persona1.edad = 18
    

    persona2 = Persona()
    persona2.nombre = "Andres"
    persona2.edad = 25

    persona1.mostrar_Datos()
    print("="*30)
    persona2.mostrar_Datos()

if __name__ == "__main__":
    main()
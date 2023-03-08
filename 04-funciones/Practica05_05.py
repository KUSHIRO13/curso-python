# Importar
import random
# Proceso


def adivina(vidas):
    numero_random = random.randint(1, 100)
    puntaje = 0
    numero_elegido = None

    while numero_random != numero_elegido:
        numero_elegido = int(input("Ingrese un numero entre 1 y 100: "))
        if numero_random < numero_elegido:
            print("Elige uno mas pequeño")
            vidas -= 1
        elif numero_random > numero_elegido:
            print("El numero es mas grande")
            vidas -= 1
        if vidas == 0:
            print("GAME OVER")
            break
        print(f"Te quedan {vidas} vidas")
    if numero_elegido == numero_random:
        print("Felicidades ganastes")



def main():
    dificultad = """
    ADIVINA EL NUMERO ALEATORIO
    Selecciona la dificultad:
    1-Facil
    2-Intermedio
    3-Dificil
    4-Cerrar
    Ingrese un numero: """
    while True:
        seleccionar = int(input(dificultad))
        if seleccionar == 1:
            adivina(10)
        elif seleccionar == 2:
            adivina(7)
        elif seleccionar == 3:
            adivina(5)
        elif seleccionar == 4:
            print("Cerrando el juego")
            break
        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()

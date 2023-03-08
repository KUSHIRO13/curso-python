import random


def generar(cantidad):
    minusculas = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mayusculas = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numeros = ["1", "2", "3", "4", "5","6", "7", "8", "9", "0"]
    simbolos = ["|", "°", "¬", "!", "\"", "#", "$", "%", "&", "/",
                "(", ")", "=", "?","\\", "¿", "¡", "*", "-", "+",";",":", "_", "{", "}", "^", "[", "]", "¨", "~", "<", ">"]

    conjunto = minusculas + mayusculas + numeros + simbolos

    contrasena = []

    for i in range(cantidad):
        conjunto_random = random.choice(conjunto)
        contrasena.append(conjunto_random)

    
    contrasena = "".join(contrasena)
    return contrasena


def main():
    contrasena = generar(
        int(input("De cuantos caracter necesitas en tu contraseña?: ")))

    print("Tu nueva contraseña es: ", contrasena)


if __name__ == "__main__":
    main()

# Palindromo
def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

# Funcion principal


def main():
    palabra = input("Ingrese una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


# Punto de entrada
if __name__ == "__main__":
    main()

import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]

    cantidad = int(sys.argv[2])
    c = 0
    while c < cantidad:
        print(texto)
        c+=1
else:
    print("Hay un error")
    print("Ejemplo: entrada_scrip.py 'Texto' 5")
c = 0

while c < 10:
    c += 1
    print(c)
    if c == 5:
        # print("Termina el bucle")
        print("Saltar de iteracion")
        continue
    print("Despues del continue")
    # break
else:
    print("Fin del While")

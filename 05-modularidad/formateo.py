from sys import argv

if len(argv) == 4:
    nombre= argv[1]
    edad= int(argv[2])
    altura = float(argv[3])
   
    #print(f"Tu nombre es: {nombre}\n Tu edad es: {edad}\n Y tu alrura es: {altura}")
    #print("Tu nombre es: {} \n Tu edad es: {} \n Y tu alrura es: {} ".format(nombre,edad,altura))
    #print("Tu nombre es: {n} \n Tu edad es: {e} \n Y tu alrura es: {a} ".format(n=nombre,e = edad,a= altura))
    print("Tu nombre es: %s \n Tu edad es: %i \n Y tu alrura es: %f "%(nombre,edad,altura))
else:
    print("Hay un error")
    print("Ejemplo: formateo.py 'Tienes que colocar un nombre' 'Edad' 'Altura'")
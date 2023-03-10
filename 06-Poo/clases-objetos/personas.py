class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_Datos(self):
        print(f"Su nombre es: ",self.nombre)
        print(f"Su edad es: ",self.edad)

    def __str__(self):
        return f"Nombre: {self.nombre} \n Edad: {self.edad}"
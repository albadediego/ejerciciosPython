#Aquí estás creando la plantilla de una mascota. Cada vez que crees una, tendrá nombre, especie y edad.
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

#Ahora puedes pedirle al objeto que se describa a sí mismo.
    def mostrar_info(self):
        print(f"Nombre : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Edad : {self.edad} años")
    
#Se añade un método para que haga un sonido
    def hacer_sonido(self):
        if self.especie == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido desconocido.")

#Crear objetos
mascota1 = Mascota("Toby", "perro", 4)
mascota2 = Mascota("Mimi", "gato", 2)

#Mostrar informacion
mascota1.mostrar_info()
mascota1.hacer_sonido()

print("---")

mascota2.mostrar_info()
mascota2.hacer_sonido()
'''
Clase perro
'''
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

#Crear un objeto
mi_perro = Perro("Fido", "Labrador")

#Usar el metodo
mi_perro.ladrar()

'''
Clase Persona
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

#Prueba
persona1 = Persona("Alba", 29)
persona1.saludar()

'''
Clase Producto
'''
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)

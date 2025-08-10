'''
Clase Perro que ladra:
Objetivo: Crear clase Perro con nombre y método ladrar.
Pseudocódigo:
    Crear clase Perro
        Atributos: nombre
        Método: ladrar() → mostrar "nombre ladra"
    Crear objeto Perro y llamar a ladrar()
'''
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} ladra")

perro1 = Perro("Ahsoka")

perro1.ladrar()
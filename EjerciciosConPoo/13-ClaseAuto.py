'''
Clase Auto que puede arrancar o detenerse:
Pseudocódigo:
    Crear clase Auto
        Atributos: marca, encendido (bool)
        Métodos: arrancar(), detener(), estado()
    Crear objeto, arrancarlo, mostrar estado
'''
class Auto:
    def __init__(self, marca:str, encendido:bool = False):
        self.marca = marca
        self.encendido = encendido

    def arrancar(self):
        self.encendido = True
        print(f"{self.marca} ha arrancado")

    def detener(self):
        self.encendido = False
        print(f"{self.marca} se ha detenido")

    def estado(self):
        if self.encendido == True:
            print(f"{self.marca} está encendido")
        else:
            print(f"{self.marca} está apagado")

coche1 = Auto("Audi")
coche1.arrancar()
coche1.estado()
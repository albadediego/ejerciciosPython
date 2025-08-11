'''
Clase Evento que se puede posponer:
Pseudocódigo:
    Clase Evento
        Atributos: nombre, fecha
        Método: posponer(días)
    Instanciar evento y posponer
'''
from datetime import date, timedelta

class Evento:
    def __init__(self, nombre:str, fecha:date):
        self.nombre = nombre
        self.fecha = fecha

    def posponer(self, dias:int):
        self.fecha += timedelta(days = dias)
        print(f"El evento {self.nombre} se ha pospuesto a {self.fecha}")

evento1 = Evento("Reunion", date(2025, 8, 11))

print(f"Fecha inicial: {evento1.fecha}")

evento1.posponer(5)
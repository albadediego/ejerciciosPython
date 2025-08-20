'''
Clase Estudiante con promedio:
Pseudocódigo:
    Clase Estudiante(nombre, lista_notas)
    Método: calcular_promedio()
    Instanciar estudiante y mostrar promedio
'''
class Estudiante():
    def __init__(self, nombre, listaNotas):
        self.nombre = nombre
        self.listaNotas = listaNotas

    def calcularPromedio(self):
        promedio = 0
        total = sum(self.listaNotas)
        promedio = total/len(self.listaNotas)
        return promedio
    
estudiante1 = Estudiante("Maria", [6,9,8,9,10])
promedioEstudiante = estudiante1.calcularPromedio()

print(f"El promedio de {estudiante1.nombre} es: {promedioEstudiante}")
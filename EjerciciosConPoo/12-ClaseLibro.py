'''
Clase Libro con título y autor:
Objetivo: Mostrar la información de un libro.
Pseudocódigo:
    Crear clase Libro
        Atributos: titulo, autor
        Método: mostrar_info()
    Crear varios libros y mostrar su info
'''
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Libro: {self.titulo} y autor: {self.autor}")

libro1 = Libro("El libro de Azrael", "Amber V. Nicole")
libro2 = Libro("La paciente silenciosa", "Alex Michaelides")

libro1.mostrar_info()
libro2.mostrar_info()
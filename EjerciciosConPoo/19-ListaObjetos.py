'''
Lista de objetos:
Objetivo: Crear una lista de mascotas y recorrerla.
Pseudocódigo:
    Clase Mascota(nombre, tipo)
    Crear lista con varios objetos Mascota
    Recorrer con for y mostrar información
'''
#Creamos la clase Mascota
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
#Creamos una lista de objetos Mascota
listaMascota = [Mascota("Ahsoka", "Perro"), Mascota("Lima", "Gato"), Mascota("Max", "Loro")]

#Recorremos la lista e imprimimos la informacion             
for mascota in listaMascota:
    print(f"Nombre: {mascota.nombre}, Tipo: {mascota.tipo}")

'''
Clase Producto con descuento:
Pseudocódigo:
    Crear clase Producto
        Atributos: nombre, precio
        Método: aplicar_descuento(porcentaje)
    Crear producto y aplicar descuento
'''
class Producto:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio
    
    def aplicar_descuento(self, porcentaje:float):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Se aplico un descuento del {porcentaje}%. Precio final: {self.precio}€")

producto1 = Producto("Lavavajillas", 280)
producto1.aplicar_descuento(15)

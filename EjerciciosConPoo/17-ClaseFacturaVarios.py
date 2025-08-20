'''
Clase Factura con varios productos:
Pseudocódigo:
    Clase Producto(nombre, precio)
    Clase Factura(lista_productos)
        Método: calcular_total()
    Crear 3 productos y calcular total

'''
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__ (self, listaProductos):
         self.listaProductos = listaProductos
        
    def calcularTotal(self):
        total = 0
        for producto in self.listaProductos:
            total += producto.precio
        return total
    
producto1 = Producto("Leche", 5.24)
producto2 = Producto("Pechuga de pollo", 6.32)
producto3 = Producto("Cafe", 10.11)

factura = Factura([producto1, producto2, producto3])

total = factura.calcularTotal()

print(f"El total de la factura es: {total:.2f}")


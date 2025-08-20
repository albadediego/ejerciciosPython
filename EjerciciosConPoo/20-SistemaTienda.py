'''
Sistema básico de tienda:
Pseudocódigo:
    Clase Producto(nombre, precio)
    Clase Tienda(lista_productos)
        Método: agregar_producto()
        Método: mostrar_productos()
    Crear tienda, agregar productos, mostrar lista
'''
#Creamos la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio:.2f}"
    
#Creamos la clase Tienda
class Tienda:
    def __init__(self):
        self.listaProductos = []

    def agregarProductos(self, producto):
        self.listaProductos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente")

    def mostrarProductos(self):
        for producto in self.listaProductos:
            print(producto)

#Creamos la tienda
tienda1 = Tienda()

#Creamos productos
producto1 = Producto("Abanico", 8.30)
producto2 = Producto("Pendientes", 10.40)
producto3 = Producto("Colgante", 15.99)

#Agregamos productos a la tienda
tienda1.agregarProductos(producto1)
tienda1.agregarProductos(producto2)
tienda1.agregarProductos(producto3)

#Mostramos los productos
tienda1.mostrarProductos()
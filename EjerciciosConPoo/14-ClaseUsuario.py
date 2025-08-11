'''
Clase Usuario con login:
Pseudocódigo:
    Crear clase Usuario
        Atributos: nombre, contraseña
        Método: login() → pedir datos y validar
    Instanciar usuario y probar login()
'''
class Usuario:
    def __init__(self, nombre:str, contrasenia:str):
        self.nombre = nombre
        self.contrasenia = contrasenia
    
    def login(self):
        #Pedimos los datos al usuario
        nombre_ingresado = input("Introduce tu nombre: ")
        contrasenia_ingresada = input("Introduce tu contraseña: ")

        #Validamos
        if nombre_ingresado == self.nombre and contrasenia_ingresada == self.contrasenia:
            print("Acceso concedido")
        else:
            print("Nombre de usuario o contaseña incorrectos")

usuario1 = Usuario("alba", "1234")
usuario1.login()



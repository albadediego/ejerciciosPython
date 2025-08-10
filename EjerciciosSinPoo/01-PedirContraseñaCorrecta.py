'''
Pedir contraseña correcta:
Objetivo: Repetir hasta que el usuario escriba la contraseña correcta.
Pseudocódigo:
    Definir contraseña_correcta como "python123"
    Repetir mientras la entrada del usuario no sea igual a contraseña_correcta:
        Pedir al usuario que escriba la contraseña
    Mostrar mensaje de acceso concedido
'''
contraseniaCorrecta = "python123"
contrasenia = input("Escriba la contraseña: ")

while contrasenia != contraseniaCorrecta:
    contrasenia = input("Escriba la contraseña: ")
print("Acceso concedido")

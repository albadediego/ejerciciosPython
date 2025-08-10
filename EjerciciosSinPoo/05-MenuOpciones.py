'''
Menú de opciones:
Objetivo: Mostrar un menú hasta que el usuario elija salir.
Pseudocódigo:
    Mientras opción != 3:
        Mostrar menú (1. Saludar, 2. Hora, 3. Salir)
        Pedir opción
        Si opción == 1: mostrar saludo
        Si opción == 2: mostrar hora (ficticia)
    Mostrar "Programa terminado"
'''
opcion = 0
while opcion != 3:
    print("Menu: \n1.Saludar \n2.Hora \n3.Salir")
    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        print("HOLAAA!")
    elif opcion == 2:
        print("Son las 14:30")
print("Programa terminado")
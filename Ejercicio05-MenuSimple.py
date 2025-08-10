'''
Muestra un menú y repite hasta que elija salir.
Pseudocódigo:
    opcion ← 0
    Mientras opcion ≠ 3
        Mostrar "1. Ver productos"
        Mostrar "2. Comprar"
        Mostrar "3. Salir"
        Leer opcion
        Si opcion = 1
            Mostrar "Mostrando productos..."
        Sino si opcion = 2
            Mostrar "Procesando compra..."
        Sino si opcion = 3
            Mostrar "Saliendo del programa"
        Sino
            Mostrar "Opción no válida"
'''

opcion = 0
while opcion != 3:
    print("1. Ver productos")
    print("2. Comprar")
    print("3. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        print("Mostrando productos...")
    elif opcion == 2:
        print("Procesando compra...")
    elif opcion == 3:
        print("Saliendo del programa")
    else:
        print("Opcion no válida")

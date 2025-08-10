'''
Sumar hasta que el usuario escriba 'fin':
Objetivo: Pedir números indefinidamente y sumar hasta que escriba "fin".
Pseudocódigo:
    Inicializar suma = 0
    Mientras entrada != "fin":
        Pedir entrada
        Si es número:
            sumar al total
    Mostrar suma total
'''

suma = 0
entrada = input("Dime un numero o fin: ")

while entrada != "fin":
    suma += int(entrada)
    entrada = input("Dime un numero o fin: ")
    
print(f"La suma total es: {suma}")
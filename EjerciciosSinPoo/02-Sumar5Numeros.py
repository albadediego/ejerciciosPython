'''
Sumar 5 números introducidos:
Objetivo: Pedir 5 números y sumar sus valores.
Pseudocódigo:
    Inicializar suma = 0
    Repetir 5 veces:
        Pedir número
        Sumar al total
    Mostrar la suma
'''
suma = 0
contador = 0
while contador < 5:
    num = int(input("Dime un numero: "))
    suma += num
    contador += 1
print(suma)
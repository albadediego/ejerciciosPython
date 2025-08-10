'''
Verificar si es un número primo:
Objetivo: Saber si un número es primo.
Pseudocódigo:
    Pedir número
    Inicializar contador de divisores = 0
    Para i desde 1 hasta número:
        Si número % i == 0:
            aumentar contador
    Si contador == 2:
        Mostrar "primo"
    Sino:
        Mostrar "no primo"
'''
num = int(input("Dime un numero: "))
contador = 0
for i in range(1, num + 1):
    if num % i == 0:
        contador += 1
if contador == 2:
    print("Primo")
else:
    print("No primo")
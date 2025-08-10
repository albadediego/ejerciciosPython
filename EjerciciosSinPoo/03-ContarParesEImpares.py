'''
Contar pares e impares:
Objetivo: Pedir 10 números y contar cuántos son pares y cuántos impares.
Pseudocódigo:
    Inicializar pares = 0, impares = 0
    Repetir 10 veces:
        Pedir número
        Si número % 2 == 0:
            aumentar pares
        sino:
            aumentar impares
    Mostrar pares e impares
'''
pares = 0
impares = 0
contador = 0

while contador < 10:
    num = int(input("Dime un numero: "))
    if num % 2 == 0:
        pares += 1
        contador +=1
    else:
        impares += 1
        contador += 1
print(f"Pares: {pares} e impares: {impares}")


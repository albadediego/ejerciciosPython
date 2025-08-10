'''
Pide un número y muestra si es par o impar.
Pseudocódigo:
    Mostrar "Introduce un número"
    Leer numero
    Si numero % 2 = 0
        Mostrar "Es un número par"
    Sino
        Mostrar "Es un número impar"
'''

num = int(input("Introduce un numero: "))

if num % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")
'''
Tabla de multiplicar:
Objetivo: Pedir un número y mostrar su tabla del 1 al 10.
Pseudocódigo:
    Pedir número
    Para i del 1 al 10:
        Mostrar número x i = resultado
'''
num = int(input("Dime un numero: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} * {i} = {resultado}")
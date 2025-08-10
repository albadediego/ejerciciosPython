'''
Usa un bucle para sumar los números del 1 al 10.
Pseudocódigo:
    suma ← 0
    numero ← 1
    Mientras numero ≤ 10
        suma ← suma + numero
        numero ← numero + 1
    Mostrar suma
'''

suma = 0
num = 1

while num <= 10:
    suma += num
    num += 1
print(suma)
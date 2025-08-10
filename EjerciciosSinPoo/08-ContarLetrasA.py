'''
Contar letras 'a' en una palabra:
Objetivo: Pedir una palabra y contar cuántas veces aparece la letra "a".
Pseudocódigo:
    Pedir palabra
    Inicializar contador = 0
    Para cada letra en palabra:
        Si letra == "a":
            aumentar contador
    Mostrar resultado
'''
palabra = input("Dime una palabra: ")
contador = 0
for letra in palabra:
    if letra == "a":
        contador += 1
print(f"Hay {contador} 'a' en {palabra}")
'''
Número secreto:
Objetivo: Adivinar un número secreto con while.
Pseudocódigo:
    Definir secreto = 7
    Mientras intento != secreto:
        Pedir intento
        Si intento < secreto: decir "muy bajo"
        Si intento > secreto: decir "muy alto"
    Mostrar "¡Correcto!"
'''

secreto = 7
intento = 0

while intento != secreto:
    intento = int(input("Dime un numero: "))
    if intento < secreto:
        print("Muy bajo")
    elif intento > secreto:
        print("Muy alto")
print("¡Correcto!")
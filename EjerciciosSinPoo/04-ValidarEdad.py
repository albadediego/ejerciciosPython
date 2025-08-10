'''
Validar edad entre 1 y 120:
Objetivo: Pedir una edad válida con while.
Pseudocódigo:
    Mientras edad no esté entre 1 y 120:
        Pedir edad
    Mostrar edad válida
'''
edad = int(input("Dime tu edad: ")) 

while edad < 1 or edad > 120:
    print("La edad debe estar comprendida entre 1 y 120")
    edad = int(input("Dime tu edad: "))

print(edad)
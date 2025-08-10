'''
Pide la edad al usuario y muestra si es mayor o menor de edad.
Pseudocódigo:
    Mostrar "Introduce tu edad"
    Leer edad
    Si edad ≥ 18
        Mostrar "Eres mayor de edad"
    Sino
        Mostrar "Eres menor de edad"
'''

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
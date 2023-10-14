"""Programa para el cálculo de las áreas y los perímetros de figuras planas y volumenes de los solidos regulares"""
import math
import os
from math import *

# Creamos el menú.

def menu():
    os.system('cls')
    print("\nPrograma para el cálculo de áreas, perímetros y volúmenes. ")
    print("\t1. Cuadrado.")
    print("\t2. Rectángulo.")
    print("\t3. Triángulo.")
    print("\t4. Rombo.")
    print("\t5. Paralelogramo.")
    print("\t6. Trapecio.")
    print("\t7. Polígono regular (Figura de 5 lados o más, de igual longitud).")
    print("\t8. Circunferencia.")
    print("\t9. Prisma rectángular.")
    print("\t10. Prisma cilíndrico.")
    print("\t11. Cubo.")
    print("\t12. Pirámide.")
    print("\t13. Cono.")
    print("\t14. Esfera.")
    print("\t15. Salir.")

# Mostramos el menú en pantalla.

while True:
    menu()

    #Le pedimos al usuario que seleccione una opción.
    opcion = int(input("Seleccione una opción: "))

    if opcion < 0 or opcion > 15:
        print("Ingrese un valor entre 1 y 14. ")
        menu()

    # Cuadrado
    elif opcion == 1:
        lado1 = float(input("lado = "))

        if lado1 <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = 4 * lado1
            area = pow(lado1, 2)

            print("El perímetro del Cuadrado es: ",perimetro)
            print("El área del Cuadrado es: ",area)

    # Rectángulo.
    elif opcion == 2:
        lado1 = float(input("lado1 = "))
        lado2 = float(input("lado2 = "))

        if lado1 <= 0 or lado2 <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = 2 * (lado1 + lado2)
            area = lado1 * lado2

            print("El perímetro del Rectángulo es: ", perimetro)
            print("El área del Rectángulo es: ", area)

    # Triángulo.
    elif opcion == 3:
        lado1 = float(input("cateto1 = "))
        lado2 = float(input("cateto2 (si es un triángulo rectángulo, ingrese el valor de la hipotenusa) = "))
        base = float(input("base = "))
        altura = float(input("altura = "))

        if lado1 <= 0 or lado2 <= 0 or base <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = lado1 + lado2 + base
            area = (base * altura) / float(2)

            print("El perímetro del Triángulo es: ", format(perimetro, ".3f"))
            print("El área del Triángulo es: ", format(area, ".3f"))

    # Rombo
    elif opcion == 4:
        lado1 = float(input("lado = "))
        diagonal1 = float(input("diagonal1 = "))
        diagonal2 = float(input("diagonal2 = "))

        if lado1 <= 0 or diagonal1 <= 0 or diagonal2 <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = 4 * lado1
            area = (diagonal1 * diagonal2) / float(2)

            print("El perímetro del Rombo es: ", format(perimetro, ".3f"))
            print("El área del Rombo es: ", format(area, ".3f"))

    # Paralelogramo.
    elif opcion == 5:
        lado1 = float(input("lado = "))
        lado2 = float(input("base = "))
        altura = float(input("altura = "))

        if lado1 <= 0 or lado2 <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = 2 * (lado1 + lado2)
            area = lado2 * altura

            print("El perímetro del Paralelogramo es: ", perimetro)
            print("El área del Paralelogramo es: ", format(area, ".3f"))

    # Trapecio
    elif opcion == 6:
        lado1 = float(input("lado1 = "))
        lado2 = float(input("lado2 = "))
        base1 = float(input("base1 = "))
        base2 = float(input("base2 = "))
        altura = float(input("altura = "))

        if lado1 <= 0 or lado2 <= 0 or base1 <= 0 or base2 <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = lado1 + lado2 + base1 + base2
            area = ((base1 + base2) / float (2)) * altura

            print("El perímetro del Trapecio es: ", perimetro)
            print("El área del Trapecio es: ", format(area, ".3f"))

    # Polígono regular
    elif opcion == 7:
        lado1 = float(input("lado = "))
        lados = int(input("Número de lados del polígono : "))
        apotema = float(input("apotema = "))

        if lado1 <= 0 or lados <= 0 or apotema <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = float(lados) * lado1
            area = perimetro * apotema

            print("El perímetro del Polígono regular es: ", format(perimetro, ".3f"))
            print("El área del Polígono regular es: ", format(area, ".3f"))

    # Circunferencia
    elif opcion == 8:
        radio = float(input("radio = "))

        if radio <= 0:
            print("Ingrese un valor positivo.")
        else:
            perimetro = 2 * pi * radio
            area = pi * pow(radio, 2)

            print("El perímetro de la Circunferencia es: ", format(perimetro, ".3f"))
            print("El área de la Circunferencia es: ", format(area, ".3f"))

    # Prisma rectángular.
    elif opcion == 9:
        lado1 = float(input("lado1 = "))
        lado2 = float(input("lado2 = "))
        altura = float(input("altura = "))

        if lado1 <= 0 or lado2 <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = lado1 * lado2 * altura

            print("El volumen del Prisma rectángular es: ",format(volumen, ".3f"))

    # Prisma cilíndrico
    elif opcion == 10:
        radio = float(input("radio = "))
        altura = float(input("altura = "))

        if radio <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = pi * pow(radio, 2) * altura

            print("El volumen del Prisma cilíndrico es: ", format(volumen, ".3f"))

    # Cubo
    elif opcion == 11:
        lado1 = float(input("lado = "))

        if lado1 <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = pow(lado1, 3)

            print("El volumen del Cubo es: ", format(volumen, ".3f"))

    # Pirámide
    elif opcion == 12:
        lado1 = float(input("lado = "))
        altura = float(input("altura = "))

        if lado1 <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = (pow(lado1, 2) * altura) / float(3)

            print("El volumen del Pirámide es: ", format(volumen, ".3f"))

    # Cono
    elif opcion == 13:
        radio = float(input("radio = "))
        altura = float(input("altura = "))

        if radio <= 0 or altura <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = (pi * pow(radio, 2) * altura) / float(3)

            print("El volumen del Cono es: ", format(volumen, ".3f"))

    # Esfera
    elif opcion == 14:
        radio = float(input("radio = "))

        if radio <= 0:
            print("Ingrese un valor positivo.")
        else:
            volumen = float(4/3) * (pi * pow(radio, 3))

            print("El volumen del Esfera es: ", format(volumen, ".3f"))

    elif opcion == 15:
        break









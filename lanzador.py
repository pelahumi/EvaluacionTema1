from Ejercicio1 import *
from Ejercicio2 import *
from Ejercicio3 import *
from Tabla import *

def lanzador():

    #Ejercicio 1
    print("Ejercicio 1:", "\n")
    suma_matriz(matriz)

    #Ejercicio 2
    print("Ejercicio 2:", "\n")
    print(longitud())

    #Ejercicio 3
    print("Ejercicio 3:", "\n")

    print("Números del 0 al 10")
    rango(0, 10, 1)

    print("Números del -10 al 0")
    rango(-10, 0, 1)

    print("Números pares del 0 al 20")
    rango(0, 20, 2)

    print("Números impares del -20 al 0")
    rango(-20, 0, 1)

    print("Números múltiplos de 5 del 0 al 50")
    rango(0, 50, 5)

    print("Ejercicio 3 de forma recursiva:", "\n")
    rango_recursivo()

    #Ejercicio 4
    tabla()
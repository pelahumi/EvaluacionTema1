def rango(a, b, c):
    for i in range(a, b, c):
        print(i ,end=" ")

#Forma recursiva

def rango_recursivo(a, b, c):
    n = b - a
    i = 0

    if n == 0:
        return print(a, end=" ")
    
    elif i == 0:
        print(b, end=" ")
        i = i + 1
        return rango_recursivo(a, b - c, c)

    else:
        n = b - c
        i = i + 1
        print(n, end=" ")
        return rango_recursivo(a, b - c, c)




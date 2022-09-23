matriz = [
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13],
    ]



def suma_matriz(matriz):
    for i in matriz:
        i = 1
        matriz[i][-1] = sum(matriz[1][:-1])
        i = i +1
    
    return matriz

print(suma_matriz(matriz))
    



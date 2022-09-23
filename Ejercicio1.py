matriz = [
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13],
    ]



def suma_matriz(matriz):

    matriz[1][-1] = sum(matriz[1][:-1])
    matriz[3][-1] = sum(matriz[3][:-1])
    
    return print(matriz)


    



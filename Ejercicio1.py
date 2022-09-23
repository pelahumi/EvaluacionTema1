matriz = [
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13],
    ]



def suma_matriz(matriz):
    i = 1
    matriz[i][-1] = sum(matriz[0][:-1])
    
    

suma_matriz(matriz)
    



def comprobacion(a):
    if 1 <= a <= 9:
        pass
    else:
        raise ValueError("Los números tienen que estar comprendidos entre 1 y 9")

def tabla(a, b):
    if a == "" or b == "":
        print("Hay que meter dos números entre el 1 y el 9") 
    
    comprobacion(a)
    comprobacion(b)

    for i in range(1, a):
        for j in range(b):
            print("* ", end="")
        print()



tabla(5, 5)
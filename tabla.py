def tabla(a, b):
    if a == "" or b == "":
        print("Hay que meter dos números entre el 1 y el 9") 
    if 1 <= a >= 9:
        pass
    else:
        raise ValueError("Los números tienen que estar comprendidos entre 1 y 9")
    if 1 <= b >= 9:
        pass
    else:
        raise ValueError("Los números tienen que estar comprendidos entre 1 y 9")

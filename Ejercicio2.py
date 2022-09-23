def longitud():
    string = input(str("Introduce la cadena de texto: "))

    if len(string) >= 3 and len(string) < 10:
        return True
    else:
        return False

print(longitud())
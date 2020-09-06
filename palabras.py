def palabras(palabra):
    primer_caracter = palabra[0]
    segundo_caracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primer_caracter}")
    print(f"El último caracter es {segundo_caracter}")
    return primer_caracter, segundo_caracter
def numero_par(numero):
    if (numero % 2) == 0:
        par = True
    else:
        par = False
    if par:
        print("Es par")
    else:
        print("Es impar")
    return par
def multiplos_rango(limite_inferior, limite_superior, numero):
    if limite_inferior > limite_superior:
        limite_inferior, limite_superior = limite_superior, limite_inferior
    limite_superior += 1
    multiplos = []
    for i in range(limite_inferior, limite_superior):
        if (i % numero) == 0:
            multiplos.append(i)
    return multiplos

print(multiplos_rango(2,21,3))

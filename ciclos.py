import datetime

print("Bienvenido, aquí están los métodos de los problemas de ciclos")

def superar_poblacion(poblacion_A, poblacion_B, tasa_A, tasa_B):
    year = datetime.date.today().year
    while poblacion_B < poblacion_A:
        poblacion_A = poblacion_A * (1+tasa_A)
        poblacion_B = poblacion_B * (1+tasa_B)
        year += 1
        print(year)
    return year

def multiplos_rango(limite_inferior, limite_superior, numero):
    multiplos = []
    if limite_inferior > 0 and limite_superior > 0:
        if limite_inferior > limite_superior:
            limite_inferior, limite_superior = limite_superior, limite_inferior
        limite_superior += 1
        for i in range(limite_inferior, limite_superior):
            if (i % numero) == 0:
                multiplos.append(i)
    return multiplos
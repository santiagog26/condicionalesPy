import datetime

def superar_poblacion(poblacion_A, poblacion_B, tasa_A, tasa_B):
    year = datetime.date.today().year
    while poblacion_B < poblacion_A:
        poblacion_A = poblacion_A * (1+tasa_A)
        poblacion_B = poblacion_B * (1+tasa_B)
        year += 1
        print(year)
    return year


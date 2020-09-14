print("Bienvenido, aquí están los métodos de los problemas de condicionales")

def calculo_edad(edad_actual, año_actual):
    if edad_actual > 0:
        if año_actual > 0:
            años = 2070 - año_actual 
            edad_futura = edad_actual + años
            print(f"La edad que tendrás en 2070 es de {edad_futura}")
            return edad_futura
        else:
            print("El año ingresado es negativo")
    else:
        print("La edad ingresada es negativa")

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

def palabras(palabra):
    primer_caracter = palabra[0]
    segundo_caracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primer_caracter}")
    print(f"El último caracter es {segundo_caracter}")
    return primer_caracter, segundo_caracter
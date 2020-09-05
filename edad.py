edad_actual = int(input("Ingresa tu edad actual:"))
año_actual = int(input("Ingresa el año actual:"))

if edad_actual > 0:
    if año_actual > 0:
        años = 2070 - año_actual 
        edad_futura = edad_actual + años
        
        print("En el año 2070 vas a tener ", edad_futura)
    else:
        print("El año ingresado es negativo")
else:
    print("La edad ingresada es negativa")
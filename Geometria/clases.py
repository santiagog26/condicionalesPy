import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hallar_distancia(self, punto):
        distancia = math.sqrt(math.pow(self.x - punto.x,2) + math.pow(self.y - punto.y,2))
        return distancia

    def verificar_dentro_circulo(self, circulo):
        if self.hallar_distancia(circulo.centro) <= circulo.radio:
            return True
        else:
            return False

class Triangulo:
    def __init__(self, punto1, punto2, punto3):
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3
        self.lado1 = punto1.hallar_distancia(punto2)
        self.lado2 = punto1.hallar_distancia(punto3)
        self.lado3 = punto2.hallar_distancia(punto3)

    def hallar_perimetro_triangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro

    def hallar_area_triangulo(self):
        s = self.hallar_perimetro_triangulo()/2
        altura = (2/self.lado1)*math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        area = (altura*self.lado1)/2
        return area

    def clasificar_triangulo_lados(self):
        if ((self.lado1 == self.lado2) and (self.lado2 == self.lado3) and (self.lado1 == self.lado3)):
            tipo = "Equilatero"
        elif (((self.lado1 == self.lado2) and (self.lado2 == self.lado3) and (self.lado1 != self.lado3)) or ((self.lado1 == self.lado2) and (self.lado2 != self.lado3) and (self.lado1 == self.lado3)) or ((self.lado1 != self.lado2) and (self.lado2 == self.lado3) and (self.lado1 == self.lado3))):
            tipo = "Isosceles"
        elif ((self.lado1 != self.lado2) and (self.lado2 != self.lado3) and (self.lado1 != self.lado3)):
            tipo = "Escaleno"
        return tipo

    def clasificar_triangulo_angulos(self):
        angulo1 = math.acos((math.pow(self.lado2, 2) + math.pow(self.lado3, 2) - math.pow(self.lado1, 2))/(2 * self.lado2 * self.lado3)) * (180/math.pi)
        angulo2 = math.acos((math.pow(self.lado1, 2) + math.pow(self.lado3, 2) - math.pow(self.lado2, 2))/(2 * self.lado1 * self.lado3)) * (180/math.pi)
        angulo3 = math.acos((math.pow(self.lado2, 2) + math.pow(self.lado1, 2) - math.pow(self.lado3, 2))/(2 * self.lado2 * self.lado1)) * (180/math.pi)

        if ((angulo1 == 90) or (angulo2 == 90) or (angulo3 == 90)):
            tipo = "Rectangulo"
        elif ((angulo1 < 90) and (angulo2 < 90) and (angulo3 < 90)): 
            tipo = "Acutangulo"
        elif ((angulo1 > 90) or (angulo2 > 90) or (angulo3 > 90)):
            tipo = "Obtusangulo"

        return tipo

class Circulo:
    def __init__(self, radio, centro):
        self.radio = radio
        self.centro = centro

    def hallar_area_circulo(self):
        area = math.pi * math.pow(self.radio, 2)
        return area

    def hallar_perimetro_circulo(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro 

class Rectangulo:
    def __init__(self, punto1, punto2, punto3, punto4):
        if punto1.hallar_distancia(punto2) == punto3.hallar_distancia(punto4):
            if punto1.hallar_distancia(punto3) == punto2.hallar_distancia(punto4):
                self.lado1 = punto1.hallar_distancia(punto2)
                self.lado2 = punto1.hallar_distancia(punto3)
            elif punto1.hallar_distancia(punto4) == punto2.hallar_distancia(punto3):
                self.lado1 = punto1.hallar_distancia(punto2)
                self.lado2 = punto1.hallar_distancia(punto4)
        elif punto1.hallar_distancia(punto3) == punto2.hallar_distancia(punto4):
            if punto1.hallar_distancia(punto4) == punto3.hallar_distancia(punto2):
                self.lado1 = punto1.hallar_distancia(punto3)
                self.lado2 = punto1.hallar_distancia(punto4)
    
    def hallar_area_rectangulo(self):
        area = self.lado1 * self.lado2
        return area

    def hallar_perimetro_rectangulo(self):
        perimetro = (self.lado1 * 2) + (self.lado2 * 2)
        return perimetro


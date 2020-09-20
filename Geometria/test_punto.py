import pytest
from clases import Punto, Circulo

def test_hallar_distancia():
    assert(Punto(0,0).hallar_distancia(Punto(5,0))) == 5

@pytest.mark.parametrize(
    "input_punto1, input_punto2, expected",
    [
        (Punto(1,1), Punto(1,-4), 5),
        (Punto(3,0), Punto(0,4), 5)
    ]
)
def test_hallar_distancia_multi(input_punto1, input_punto2, expected):
    assert input_punto1.hallar_distancia(input_punto2) == expected

def test_verificar_dentro_circulo():
    assert(Punto(0,0).verificar_dentro_circulo(Circulo(2, Punto(0,1)))) == True

@pytest.mark.parametrize(
    "input_punto, input_circulo, expected",
    [
        (Punto(2,4), Circulo(4, Punto(5, -2)), False),
        (Punto(6,-2), Circulo(4, Punto(7, -1)), True)
    ]
)
def test_verificar_dentro_circulo_multi(input_punto, input_circulo, expected):
    assert(input_punto.verificar_dentro_circulo(input_circulo)) == expected
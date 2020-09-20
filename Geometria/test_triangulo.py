import pytest
from clases import Triangulo, Punto

def test_hallar_perimetro_triangulo():
    assert(Triangulo(Punto(0,0), Punto(0,3), Punto(4,0)).hallar_perimetro_triangulo()) == 12

@pytest.mark.parametrize(
    "triangulo, expected",
    [
        (Triangulo(Punto(0,0),Punto(0,5),Punto(5,0)), 17.07),
        (Triangulo(Punto(0,0),Punto(0,-4),Punto(-2,0)), 10.47)
    ]
)
def test_hallar_perimetro_triangulo_multi(triangulo, expected):
    assert triangulo.hallar_perimetro_triangulo() == pytest.approx(expected, 0.1)

def test_hallar_area_triangulo():
    assert(Triangulo(Punto(0,0), Punto(0,3), Punto(4,0)).hallar_area_triangulo()) == 6

@pytest.mark.parametrize(
    "triangulo, expected",
    [
        (Triangulo(Punto(0,0),Punto(0,5),Punto(5,0)), 12.5),
        (Triangulo(Punto(0,0),Punto(0,-4),Punto(-2,0)), 4)
    ]
)
def test_hallar_area_triangulo_multi(triangulo, expected):
    assert triangulo.hallar_area_triangulo() == pytest.approx(expected, 0.1)

def test_clasificar_triangulo_lados():
    assert(Triangulo(Punto(0,0), Punto(3,0), Punto(0,4)).clasificar_triangulo_lados()) == 'Escaleno'

def test_clasificar_triangulo_angulos():
    assert(Triangulo(Punto(0,0), Punto(0,3), Punto(4,0)).clasificar_triangulo_angulos()) == 'Rectangulo'
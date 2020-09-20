import pytest
from clases import Rectangulo, Punto

def test_hallar_area_rectangulo():
    assert(Rectangulo(Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)).hallar_area_rectangulo()) == pytest.approx(2, 0.01)

@pytest.mark.parametrize(
    "rectangulo, expected",
    [
        (Rectangulo(Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)), 2),
        (Rectangulo(Punto(0,0), Punto(0,-2), Punto(5,0), Punto(5,-2)), 10)
    ]
)
def test_hallar_area_rectangulo_multi(rectangulo, expected):
    assert(rectangulo.hallar_area_rectangulo()) == pytest.approx(expected, 0.01)

def test_hallar_perimetro_rectangulo():
    assert(Rectangulo(Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)).hallar_perimetro_rectangulo()) == pytest.approx(6, 0.01)

@pytest.mark.parametrize(
    "rectangulo, expected",
    [
        (Rectangulo(Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)), 6),
        (Rectangulo(Punto(0,0), Punto(0,-2), Punto(5,0), Punto(5,-2)), 14)
    ]
)
def test_hallar_perimetro_rectangulo_multi(rectangulo, expected):
    assert(rectangulo.hallar_perimetro_rectangulo()) == pytest.approx(expected, 0.01)
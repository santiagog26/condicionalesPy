import pytest
from clases import Circulo, Punto

def test_hallar_area_circulo():
    assert(Circulo(2, Punto(0,0)).hallar_area_circulo()) == pytest.approx(12.56, 0.01)

@pytest.mark.parametrize(
    "input_circulo, expected",
    [
        (Circulo(4,(1,0)), 50.26),
        (Circulo(5,(0,-2)), 78.53)
    ]
)
def test_hallar_area_circulo_multi(input_circulo, expected):
    assert(input_circulo.hallar_area_circulo()) == pytest.approx(expected, 0.01)

def test_hallar_perimetro_circulo():
    assert(Circulo(3, Punto(0,0)).hallar_perimetro_circulo()) == pytest.approx(18.84, 0.01)

@pytest.mark.parametrize(
    "input_circulo, expected",
    [
        (Circulo(4,(1,0)), 25.13),
        (Circulo(5,(0,-2)), 31.41)
    ]
)
def test_hallar_perimetro_circulo_multi(input_circulo, expected):
    assert(input_circulo.hallar_perimetro_circulo()) == pytest.approx(expected, 0.01)

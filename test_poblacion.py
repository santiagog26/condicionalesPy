import pytest
from ciclos import superar_poblacion

def test_superar_poblacion():
    assert superar_poblacion(35000000, 19900000, 0.02, 0.03) == 2078

@pytest.mark.parametrize(
    "input_A, input_B, input_tA, input_tB, expected",
    [
        (35,19.9,0.02,0.03,2078),
        (10,9,0.2,0.3,2022),
        (50000000,45000000,0.04,0.06,2026)
    ]
)
def test_superar_poblacion_multi(input_A, input_B, input_tA, input_tB, expected):
    assert superar_poblacion(input_A, input_B, input_tA, input_tB) == expected
import pytest
from ciclos import multiplos_rango

def test_multiplos_rango():
    assert multiplos_rango(2,21,3) == [3,6,9,12,15,18,21]

@pytest.mark.parametrize(
    "input_a, input_b, input_c, expected",
    [
        (2,21,3,[3,6,9,12,15,18,21]),
        (2,4,3,[3]),
        (1,10,2,[2,4,6,8,10]),
        (-10,2,2,[]),
        (21,2,3,[3,6,9,12,15,18,21])
    ]
)
def test_multiplos_rango_multi(input_a, input_b, input_c, expected):
    assert multiplos_rango(input_a,input_b,input_c) == expected
import pytest
from numero_par import numero_par

def test_par():
    assert numero_par(10) == True  

@pytest.mark.parametrize(
    "input_a, expected",
    [
        (2, True),
        (9, False),
        (-1, False),
        (-6, True)
    ]
)
def test_par_multi(input_a, expected):
    assert numero_par(input_a) == expected

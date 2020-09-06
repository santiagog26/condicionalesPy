import pytest
from edad import calculo_edad

def test_calculo_edad():
    assert calculo_edad(10,2010) == 70  

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (10,2010,70),
        (20,2020,70),
        (calculo_edad(10,2010),2070,70)
    ]
)
def test_calculo_edad_multi(input_a, input_b, expected):
    assert calculo_edad(input_a, input_b) == expected

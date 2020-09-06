import pytest
from palabras import palabras

def test_palabras():
    assert palabras("Hola") == ("H", "a")

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("Hola", ("H","a")),
        ("Santiago", ("S","o")),
        ("a", ("a", "a")),
        ("-291", ("-", "1"))
    ]
)
def test_palabras_multi(input_a, expected):
    assert palabras(input_a) == expected

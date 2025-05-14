import pytest
from mypkg import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (2, -2, 0),
    (100, 1, 101),
])
def test_add_various(a, b, expected):
    assert add(a, b) == expected

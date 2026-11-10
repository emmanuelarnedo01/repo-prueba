from app.main import suma, resta, multiplicacion, division
import pytest

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-1, -1) == 0
    assert resta(0, 5) == -5
    
def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0
    
def test_division():
    assert division(6, 3) == 2
    assert division(-4, 2) == -2
    with pytest.raises(ValueError):
        division(1, 0)
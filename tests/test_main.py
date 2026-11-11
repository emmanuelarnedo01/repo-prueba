from app.main import suma, resta, multiplicacion, division
import pytest
import os

def test_secret_inyectado():
    # Compureba que la variable de entorno existe y tiene el valor esperado
    assert os.environ.get("MI_CLAVE_SECRETA") == "api_key_falsa_123"

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
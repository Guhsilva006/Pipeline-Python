from calculadora import somar

def test_soma_correta():
    assert somar(2, 3) == 5

def test_soma_errada():
    assert somar(2, 2) != 5

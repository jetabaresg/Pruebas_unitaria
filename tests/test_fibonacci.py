from src.fibonacci import fibonacci_iterativo, fibonacci_recursivo, fibonacci_serie, es_fibonacci, es_cuadrado_perfecto

def test_fibonacci_iterativo():
    posicion = 4

    resultado_esperado = 3

    resultado = fibonacci_iterativo(posicion)

    assert resultado == resultado_esperado

def test_fibonacci_recursivo():
    posicion = 4

    resultado_esperado = 3

    resultado = fibonacci_recursivo(posicion)

    assert resultado == resultado_esperado

def test_fibonacci_serie():
    posicion = 4

    resultado_esperado = [0,1,1,2,3]

    resultado = fibonacci_serie(posicion)

    assert resultado == resultado_esperado

def test_es_fibonacci():
    num = 34
    resultado_esperado = True

    resultado = es_fibonacci(num)

    assert resultado == resultado_esperado

def test_es_cuadrado_perfecto():
    num = 26
    resultado_esperado = False

    resultado = es_cuadrado_perfecto(num)

    assert resultado == resultado_esperado
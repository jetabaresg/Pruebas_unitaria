# test_calculadora.py
import pytest
from src.calculadora import restar, sumar ,dividir,multiplicar, potencia, promedio, maximo, raiz_cuadrada, minimo


def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(-5, -3) == -8
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(-5, -3) == -2
    assert restar(0, 0) == 0

def test_dividir():
    assert dividir(5, 3) == 5/3
    assert dividir(-5, -3) == 5/3
    assert dividir(0, 1) == 0
    assert dividir(5, 0) == "No se puede dividir por cero"

def test_multiplicar():
    assert multiplicar(5, 3) == 15

def test_potencia():
    assert potencia(5, 3) == 125
    assert potencia(2, -4) == 1/16

def test_promedio():
    lista = [1, 2, 3, 4, 5]
    assert promedio(lista) == 3

def test_maximo():
    lista = [1, 2, 3, 4, 5]
    assert maximo(lista) == 5

def test_minimo():
    lista = [1, 2, 3, 4, 5]
    assert minimo(lista) == 1

def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(-8) == "No se pueden calcular raíces cuadradas de números negativos"

def test_calcular_area_rectangulo():
    from src.calculadora import calcular_area_rectangulo
    assert calcular_area_rectangulo(5, 3) == 15

def test_calcular_perimetro_rectangulo():
    from src.calculadora import calcular_perimetro_rectangulo
    assert calcular_perimetro_rectangulo(5, 3) == 16
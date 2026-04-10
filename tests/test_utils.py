import pytest
from src.utils import celsius_a_fahrenheit,es_primo, fahrenheit_a_celsius, celsius_a_kelvin, kelvin_a_celsius, calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes, fahrenheit_a_celsius, celsius_a_kelvin, kelvin_a_celsius, calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes ,calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes,calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes, calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes,calcular_imc, categorizar_imc, calcular_edad, es_bisiesto, dias_en_mes, mcd, mcm

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212

def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0
    assert fahrenheit_a_celsius(212) == 100

def test_celsius_a_kelvin():
    assert celsius_a_kelvin(0) == 273.15
    assert celsius_a_kelvin(100) == 373.15

def test_kelvin_a_celsius():
    assert kelvin_a_celsius(273.15) == 0
    assert kelvin_a_celsius(373.15) == 100

def test_calcular_imc():
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, 0.01)
    assert calcular_imc(-70, 1.75) == "El peso debe ser mayor a 0"
    assert calcular_imc(70, -1.75) == "La altura debe ser mayor a 0"

def test_categorizar_imc():
    assert categorizar_imc(17) == "Bajo peso"
    assert categorizar_imc(22) == "Normal"
    assert categorizar_imc(27) == "Sobrepeso"
    assert categorizar_imc(32) == "Obesidad"

def test_calcular_edad():
    assert calcular_edad(1990, 2020) == 30
    assert calcular_edad(2025, 2020) == "El año de nacimiento no puede ser mayor al año actual"

def test_es_bisiesto():
    assert es_bisiesto(2020) == True
    assert es_bisiesto(1900) == False
    assert es_bisiesto(2000) == True
    assert es_bisiesto(2021) == False

def test_dias_en_mes():
    assert dias_en_mes(1, 2020) == 31
    assert dias_en_mes(2, 2020) == 29
    assert dias_en_mes(2, 2021) == 28
    assert dias_en_mes(4, 2020) == 30
    assert dias_en_mes(0, 2020) == "El mes debe estar entre 1 y 12"
    assert dias_en_mes(13, 2020) == "El mes debe estar entre 1 y 12"

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(17) == True
    assert es_primo(20) == False

def test_mcd():
    assert mcd(48, 18) == 6
    assert mcd(101, 10) == 1
    assert mcd(54, 24) == 6

def test_mcm():
    assert mcm(4, 6) == 12
    assert mcm(21, 6) == 42
    assert mcm(8, 9) == 72
    assert mcm(0, 5) == 0
    assert mcm(28,31) == 868
    assert mcm(12,0) == 0
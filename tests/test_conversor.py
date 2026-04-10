import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas
)

def test_celsius_a_fahrenheit():
    """Prueba conversión de Celsius a Fahrenheit."""
    # Arrange
    celsius = 0
    resultado_esperado = 32

    # Act
    resultado = celsius_a_fahrenheit(celsius)

    # Assert
    assert resultado == resultado_esperado


def test_fahrenheit_a_celsius():
    """Prueba conversión de Fahrenheit a Celsius."""
    # Arrange
    fahrenheit = 32
    resultado_esperado = 0

    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)

    # Assert
    assert resultado == resultado_esperado


def test_celsius_a_kelvin():
    """Prueba conversión de Celsius a Kelvin."""
    # Arrange
    celsius = 0
    resultado_esperado = 273.15

    # Act
    resultado = celsius_a_kelvin(celsius)

    # Assert
    assert resultado == resultado_esperado


def test_kelvin_a_celsius():
    """Prueba conversión de Kelvin a Celsius."""
    # Arrange
    kelvin = 273.15
    resultado_esperado = 0

    # Act
    resultado = kelvin_a_celsius(kelvin)

    # Assert
    assert resultado == resultado_esperado


def test_kelvin_negativo():
    """Prueba Kelvin negativo (BUG esperado)."""
    # Arrange
    kelvin = -10

    # Act & Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)



def test_metros_a_kilometros():
    """Prueba metros a kilómetros."""
    # Arrange
    metros = 1000
    resultado_esperado = 1

    # Act
    resultado = metros_a_kilometros(metros)

    # Assert
    assert resultado == resultado_esperado


def test_kilometros_a_metros():
    """Prueba kilómetros a metros."""
    # Arrange
    km = 1
    resultado_esperado = 1000

    # Act
    resultado = kilometros_a_metros(km)

    # Assert
    assert resultado == resultado_esperado


def test_kilometros_a_millas():
    """Prueba kilómetros a millas."""
    # Arrange
    km = 1
    resultado_esperado = 1 / 1.60934

    # Act
    resultado = kilometros_a_millas(km)

    # Assert
    assert resultado == resultado_esperado


def test_kilometros_a_millas_error():
    """Prueba conversión incorrecta (BUG esperado)."""
    # Arrange
    km = 1
    resultado_incorrecto = 1.60934

    # Act
    resultado = kilometros_a_millas(km)

    # Assert
    assert resultado != resultado_incorrecto


def test_millas_a_kilometros():
    """Prueba millas a kilómetros."""
    # Arrange
    millas = 1
    resultado_esperado = 1.60934

    # Act
    resultado = millas_a_kilometros(millas)

    # Assert
    assert resultado == resultado_esperado



def test_libras_a_kilogramos():
    """Prueba libras a kilogramos."""
    # Arrange
    libras = 1
    resultado_esperado = 0.453592

    # Act
    resultado = libras_a_kilogramos(libras)

    # Assert
    assert resultado == resultado_esperado


def test_kilogramos_a_libras():
    """Prueba kilogramos a libras."""
    # Arrange
    kg = 1
    resultado_esperado = 1 / 0.453592

    # Act
    resultado = kilogramos_a_libras(kg)

    # Assert
    assert resultado == resultado_esperado



def test_galones_a_litros():
    """Prueba galones a litros."""
    # Arrange
    galones = 1
    resultado_esperado = 3.78541

    # Act
    resultado = galones_a_litros(galones)

    # Assert
    assert resultado == resultado_esperado


def test_litros_a_galones():
    """Prueba litros a galones."""
    # Arrange
    litros = 3.78541
    resultado_esperado = 1

    # Act
    resultado = litros_a_galones(litros)

    # Assert
    assert resultado == resultado_esperado



def test_pies_a_metros():
    """Prueba pies a metros."""
    # Arrange
    pies = 1
    resultado_esperado = 0.3048

    # Act
    resultado = pies_a_metros(pies)

    # Assert
    assert resultado == resultado_esperado


def test_metros_a_pies():
    """Prueba metros a pies."""
    # Arrange
    metros = 0.3048
    resultado_esperado = 1

    # Act
    resultado = metros_a_pies(metros)

    # Assert
    assert resultado == resultado_esperado



def test_onzas_a_gramos():
    """Prueba onzas a gramos."""
    # Arrange
    onzas = 1
    resultado_esperado = 28.3495

    # Act
    resultado = onzas_a_gramos(onzas)

    # Assert
    assert resultado == resultado_esperado


def test_gramos_a_onzas():
    """Prueba gramos a onzas."""
    # Arrange
    gramos = 28.3495
    resultado_esperado = 1

    # Act
    resultado = gramos_a_onzas(gramos)

    # Assert
    assert resultado == resultado_esperado
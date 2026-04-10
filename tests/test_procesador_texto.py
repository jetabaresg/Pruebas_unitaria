import pytest
from src.procesador_texto import *

# ------------------ CONTAR PALABRAS ------------------
def test_contar_palabras():
    # Arrange
    texto = "Hola mundo"
    esperado = 2

    # Act
    resultado = contar_palabras(texto)

    # Assert
    assert resultado == esperado


# ------------------ VOCALES ------------------
def test_contar_vocales():
    # Arrange
    texto = "Hola"
    esperado = 2

    # Act
    resultado = contar_vocales(texto)

    # Assert
    assert resultado == esperado


# ------------------ INVERTIR ------------------
def test_invertir_texto():
    # Arrange
    texto = "hola"
    esperado = "aloh"

    # Act
    resultado = invertir_texto(texto)

    # Assert
    assert resultado == esperado


# ------------------ PALINDROMO ------------------
def test_palindromo_simple():
    # Arrange
    texto = "oso"

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is True


def test_palindromo_con_espacios():
    """Detecta el BUG."""
    # Arrange
    texto = "anita lava la tina"

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is True


def test_palindromo_mayusculas():
    """Detecta el BUG."""
    # Arrange
    texto = "Anita Lava La Tina"

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is True


def test_no_palindromo():
    # Arrange
    texto = "hola"

    # Act
    resultado = es_palindromo(texto)

    # Assert
    assert resultado is False


# ------------------ ESPACIOS ------------------
def test_eliminar_espacios():
    # Arrange
    texto = "hola   mundo"
    esperado = "hola mundo"

    # Act
    resultado = eliminar_espacios_extra(texto)

    # Assert
    assert resultado == esperado


# ------------------ MAYUSCULAS ------------------
def test_mayusculas():
    # Arrange
    texto = "hola"
    esperado = "HOLA"

    # Act
    resultado = convertir_mayusculas(texto)

    # Assert
    assert resultado == esperado


# ------------------ MINUSCULAS ------------------
def test_minusculas():
    # Arrange
    texto = "HOLA"
    esperado = "hola"

    # Act
    resultado = convertir_minusculas(texto)

    # Assert
    assert resultado == esperado


# ------------------ CAPITALIZAR ------------------
def test_capitalizar():
    # Arrange
    texto = "hola mundo"
    esperado = "Hola Mundo"

    # Act
    resultado = capitalizar_palabras(texto)

    # Assert
    assert resultado == esperado


# ------------------ REEMPLAZAR ------------------
def test_reemplazar():
    # Arrange
    texto = "hola mundo"
    esperado = "hola python"

    # Act
    resultado = reemplazar_palabra(texto, "mundo", "python")

    # Assert
    assert resultado == esperado


# ------------------ INICIALES ------------------
def test_iniciales():
    # Arrange
    nombre = "Juan Perez"
    esperado = "JP"

    # Act
    resultado = extraer_iniciales(nombre)

    # Assert
    assert resultado == esperado


# ------------------ LIMPIAR TEXTO ------------------
def test_limpiar_texto():
    # Arrange
    texto = "hola!!! mundo123"
    esperado = "hola mundo123"

    # Act
    resultado = limpiar_texto(texto)

    # Assert
    assert resultado == esperado
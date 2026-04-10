import pytest
from src.validador import *

# ------------------ EMAIL ------------------
def test_email_valido():
    # Arrange
    email = "test@email.com"

    # Act
    resultado = validar_email(email)

    # Assert
    assert resultado is True


def test_email_invalido():
    # Arrange
    email = "testemail.com"

    # Act
    resultado = validar_email(email)

    # Assert
    assert resultado is False


# ------------------ TELEFONO ------------------
def test_telefono_valido():
    # Arrange
    telefono = "1234567890"

    # Act
    resultado = validar_telefono(telefono)

    # Assert
    assert resultado is True


def test_telefono_con_letras():
    # Arrange
    telefono = "123ABC"

    # Act
    resultado = validar_telefono(telefono)

    # Assert
    assert resultado is False


# ------------------ EDAD ------------------
def test_edad_valida():
    # Arrange
    edad = 25

    # Act
    resultado = validar_edad(edad)

    # Assert
    assert resultado is True


def test_edad_negativa():
    # Arrange
    edad = -5

    # Act
    resultado = validar_edad(edad)

    # Assert
    assert resultado is False


# ------------------ PASSWORD ------------------
def test_password_valido():
    # Arrange
    password = "Abc12345"

    # Act
    resultado = validar_password(password)

    # Assert
    assert resultado is True


def test_password_sin_mayuscula():
    # Arrange
    password = "abc12345"

    # Act
    resultado = validar_password(password)

    # Assert
    assert resultado is False


# ------------------ URL ------------------
def test_url_valida():
    # Arrange
    url = "https://google.com"

    # Act
    resultado = validar_url(url)

    # Assert
    assert resultado is True


def test_url_invalida():
    # Arrange
    url = "google.com"

    # Act
    resultado = validar_url(url)

    # Assert
    assert resultado is False


# ------------------ FECHA ------------------
def test_fecha_valida():
    # Arrange
    dia, mes, año = 15, 5, 2020

    # Act
    resultado = validar_fecha(dia, mes, año)

    # Assert
    assert resultado is True


def test_fecha_invalida_dia_mes():
    """Detecta el BUG."""
    # Arrange
    dia, mes, año = 31, 4, 2020  # Abril tiene 30

    # Act
    resultado = validar_fecha(dia, mes, año)

    # Assert
    assert resultado is False


# ------------------ CEDULA ------------------
def test_cedula_valida():
    # Arrange
    cedula = "12345678"

    # Act
    resultado = validar_cedula(cedula)

    # Assert
    assert resultado is True


def test_cedula_invalida():
    # Arrange
    cedula = "abc123"

    # Act
    resultado = validar_cedula(cedula)

    # Assert
    assert resultado is False
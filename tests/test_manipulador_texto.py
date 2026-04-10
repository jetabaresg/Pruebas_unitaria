from src.manipulador_texto import invertir_cadena, contar_vocales, contar_consonantes, es_palindromo, eliminar_duplicados, capitalizar_palabras, convertir_a_titulo,reemplazar_subcadena, dividir_en_palabras, extraer_dominio, enmascarar_email,normalizar_espacios, truncar, es_anagrama



import pytest


def test_invertir_cadena():
    cadena = "hola"
    resultado_esperado = "aloh"

    resultado = invertir_cadena(cadena)

    assert resultado == resultado_esperado


def test_contar_vocales():
    cadena = "hola mundo"
    resultado_esperado = 4

    resultado = contar_vocales(cadena)

    assert resultado == resultado_esperado


def test_contar_consonantes():
    cadena = "hola"
    resultado_esperado = 2

    resultado = contar_consonantes(cadena)

    assert resultado == resultado_esperado


def test_es_palindromo():
    cadena = "Anita lava la tina"
    resultado_esperado = True

    resultado = es_palindromo(cadena)

    assert resultado == resultado_esperado


def test_eliminar_duplicados():
    cadena = "aabbcc"
    resultado_esperado = "abc"

    resultado = eliminar_duplicados(cadena)

    assert resultado == resultado_esperado


def test_capitalizar_palabras():
    cadena = "hola mundo"
    resultado_esperado = "Hola Mundo"

    resultado = capitalizar_palabras(cadena)

    assert resultado == resultado_esperado


def test_convertir_a_titulo():
    cadena = "hola mundo"
    resultado_esperado = "Hola Mundo"

    resultado = convertir_a_titulo(cadena)

    assert resultado == resultado_esperado


def test_reemplazar_subcadena():
    cadena = "hola mundo"
    resultado_esperado = "hola python"

    resultado = reemplazar_subcadena(cadena, "mundo", "python")

    assert resultado == resultado_esperado


def test_dividir_en_palabras():
    cadena = "hola   mundo"
    resultado_esperado = ["hola", "mundo"]

    resultado = dividir_en_palabras(cadena)

    assert resultado == resultado_esperado


def test_extraer_dominio():
    email = "test@gmail.com"
    resultado_esperado = "gmail.com"

    resultado = extraer_dominio(email)

    assert resultado == resultado_esperado


def test_enmascarar_email():
    email = "correo@gmail.com"
    resultado_esperado = "c****o@gmail.com"

    resultado = enmascarar_email(email)

    assert resultado == resultado_esperado


def test_normalizar_espacios():
    cadena = "hola    mundo"
    resultado_esperado = "hola mundo"

    resultado = normalizar_espacios(cadena)

    assert resultado == resultado_esperado


def test_truncar():
    cadena = "hola mundo"
    resultado_esperado = "hola..."

    resultado = truncar(cadena, 7)

    assert resultado == resultado_esperado


def test_es_anagrama():
    c1 = "roma"
    c2 = "amor"
    resultado_esperado = True

    resultado = es_anagrama(c1, c2)

    assert resultado == resultado_esperado
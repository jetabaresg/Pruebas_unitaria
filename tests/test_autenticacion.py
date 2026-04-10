import pytest
from src.autenticacion import hash_contraseña, verificar_contraseña, validar_usuario,generar_token, validar_token, generar_codigo_2fa, verificar_codigo_2fa

def test_hash_contraseña():
    contraseña = "MiContraseña123"
    contraseña2 = "   "
    assert len(hash_contraseña(contraseña)) == 64  # SHA-256 produce 64 hex chars
    assert hash_contraseña(contraseña2) == "La contraseña no puede estar vacía o ser None"

def test_verificar_contraseña():
    contraseña = "Segura1!"
    h = hash_contraseña(contraseña)
    assert verificar_contraseña(contraseña, h) == True
    assert verificar_contraseña("OtraContraseña", h) == False

def test_validar_usuario():
    assert validar_usuario("usuario_valido") == True
    assert validar_usuario ("us") == False  # Demasiado corto
    assert validar_usuario("usuario_invalido!") == False  # Caracteres no permitidos

def test_generar_token():
    token1 = generar_token("usuario", "timestamp")
    token2 = generar_token("usuario", "timestamp")
    assert token1 != token2  # El salt hace que el token cambie en cada ejecucion
    assert validar_token(token1) == True
    assert validar_token(token2) == True

def test_validar_token():
    token = generar_token("usuario", "timestamp")
    assert validar_token(token) == True
    assert validar_token("token_invalido") == False
    assert validar_token("") == False

def test_generar_codigo_2fa():
    codigo1 = generar_codigo_2fa()
    codigo2 = generar_codigo_2fa()
    assert len(codigo1) == 6  # Código de 6 dígitos
    assert codigo1.isdigit() == True  # Solo dígitos
    assert codigo1 != codigo2  # Deben ser diferentes cada vez

def test_verificar_codigo_2fa():
    codigo = generar_codigo_2fa()
    assert verificar_codigo_2fa(codigo, codigo) == True
    assert verificar_codigo_2fa("123456", codigo) == False

def test_sanear_entradas():
    assert hash_contraseña("") == "La contraseña no puede estar vacía o ser None"
    assert hash_contraseña(None) == "La contraseña no puede estar vacía o ser None"
    assert validar_usuario("") == False
    assert validar_usuario(None) == False
    assert validar_token("") == False
    assert validar_token(None) == False
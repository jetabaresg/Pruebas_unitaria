"""
Módulo de validación de datos.
ATENCIÓN: Hay 1 bug oculto en este archivo.
"""

import re

def validar_email(email):
    """Valida si un email tiene formato correcto."""
    if not email:
        return False

    if '@' not in email:
        return False

    partes = email.split('@')
    if len(partes) != 2:
        return False

    usuario, dominio = partes

    if not usuario or not dominio:
        return False

    if '.' not in dominio:
        return False

    return True

def validar_telefono(telefono):
    """Valida si un teléfono tiene formato correcto (solo números)."""
    if not telefono:
        return False

    # Eliminar espacios y guiones
    telefono_limpio = telefono.replace(' ', '').replace('-', '')

    # Verificar que sea solo números
    if not telefono_limpio.isdigit():
        return False

    # Verificar longitud (entre 7 y 15 dígitos)
    return 7 <= len(telefono_limpio) <= 15

def validar_edad(edad):
    """Valida si una edad es correcta."""
    if not isinstance(edad, int):
        return False

    if edad < 0:
        return False

    if edad > 120:
        return False

    return True

def validar_password(password):
    """Valida si una contraseña cumple requisitos mínimos."""
    if not password:
        return False

    if len(password) < 8:
        return False

    # Debe tener al menos una mayúscula
    if not any(c.isupper() for c in password):
        return False

    # Debe tener al menos una minúscula
    if not any(c.islower() for c in password):
        return False

    # Debe tener al menos un número
    if not any(c.isdigit() for c in password):
        return False

    return True

def validar_url(url):
    """Valida si una URL tiene formato básico correcto."""
    if not url:
        return False

    # Patrón básico de URL
    patron = r'^https?://[^\s/$.?#].[^\s]*$'
    return re.match(patron, url) is not None

def validar_fecha(dia, mes, año):
    """Valida si una fecha es correcta."""
    if not all(isinstance(x, int) for x in [dia, mes, año]):
        return False

    # BUG: No valida correctamente el mes y día
    if mes < 1 or mes > 12:
        return False

    if dia < 1 or dia > 31:
        return False

    if año < 1900 or año > 2100:
        return False

    return True

def validar_cedula(cedula):
    """Valida si una cédula colombiana tiene formato básico."""
    if not cedula:
        return False

    # Debe ser solo números
    if not str(cedula).isdigit():
        return False

    # Debe tener entre 6 y 10 dígitos
    longitud = len(str(cedula))
    return 6 <= longitud <= 10
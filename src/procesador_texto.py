"""
Módulo de procesamiento de texto.
ATENCIÓN: Hay 1 bug oculto en este archivo.
"""

def contar_palabras(texto):
    """Cuenta las palabras en un texto."""
    if not texto:
        return 0

    palabras = texto.split()
    return len(palabras)

def contar_vocales(texto):
    """Cuenta las vocales en un texto."""
    if not texto:
        return 0

    vocales = 'aeiouAEIOU'
    return sum(1 for c in texto if c in vocales)

def invertir_texto(texto):
    """Invierte un texto."""
    if not texto:
        return ""
    return texto[::-1]

def es_palindromo(texto):
    """Verifica si un texto es palíndromo."""
    if not texto:
        return False

    # BUG: No maneja espacios ni mayúsculas
    return texto == texto[::-1]

def eliminar_espacios_extra(texto):
    """Elimina espacios extra de un texto."""
    if not texto:
        return ""

    return ' '.join(texto.split())

def convertir_mayusculas(texto):
    """Convierte un texto a mayúsculas."""
    if not texto:
        return ""
    return texto.upper()

def convertir_minusculas(texto):
    """Convierte un texto a minúsculas."""
    if not texto:
        return ""
    return texto.lower()

def capitalizar_palabras(texto):
    """Capitaliza cada palabra de un texto."""
    if not texto:
        return ""
    return texto.title()

def reemplazar_palabra(texto, vieja, nueva):
    """Reemplaza una palabra por otra en un texto."""
    if not texto:
        return ""

    return texto.replace(vieja, nueva)

def extraer_iniciales(nombre_completo):
    """Extrae las iniciales de un nombre completo."""
    if not nombre_completo:
        return ""

    partes = nombre_completo.split()
    iniciales = ''.join([p[0].upper() for p in partes])
    return iniciales

def limpiar_texto(texto):
    """Limpia un texto eliminando caracteres especiales."""
    if not texto:
        return ""

    # Permitir solo letras, números y espacios
    texto_limpio = ''.join(c for c in texto if c.isalnum() or c.isspace())
    return texto_limpio
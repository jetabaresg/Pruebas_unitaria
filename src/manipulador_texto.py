"""
Módulo de manipulación de cadenas y texto.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

def invertir_cadena(cadena):
    """Invierte una cadena de texto."""
    if not cadena:
        return ""
    return cadena[::-1]

def contar_vocales(cadena):
    """Cuenta las vocales en una cadena."""
    if not cadena:
        return 0

    vocales = "aeiouAEIOU"
    contador = 0

    for caracter in cadena:
        if caracter in vocales:
            contador += 1

    return contador

def contar_consonantes(cadena):
    """Cuenta las consonantes en una cadena."""
    if not cadena:
        return 0

    vocales = "aeiouAEIOU"
    contador = 0

    for caracter in cadena:
        if caracter.isalpha() and caracter not in vocales:
            contador += 1

    return contador

def es_palindromo(cadena):
    """Verifica si una cadena es palíndromo."""
    if not cadena:
        return False

    # BUG 1: No maneja espacios ni mayúsculas/minúsculas
    cadena_limpia = cadena
    return cadena_limpia == cadena_limpia[::-1]

def eliminar_duplicados(cadena):
    """Elimina caracteres duplicados conservando el orden."""
    if not cadena:
        return ""

    vistos = []
    resultado = []

    for caracter in cadena:
        if caracter not in vistos:
            vistos.append(caracter)
            resultado.append(caracter)

    return "".join(resultado)

def capitalizar_palabras(cadena):
    """Capitaliza la primera letra de cada palabra."""
    if not cadena:
        return ""

    palabras = cadena.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]

    return " ".join(palabras_capitalizadas)

def convertir_a_titulo(cadena):
    """Convierte una cadena a formato título."""
    if not cadena:
        return ""

    return cadena.title()

def reemplazar_subcadena(cadena, vieja, nueva, max_reemplazos=-1):
    """Reemplaza una subcadena por otra."""
    if not cadena:
        return ""

    if max_reemplazos == -1:
        return cadena.replace(vieja, nueva)
    else:
        return cadena.replace(vieja, nueva, max_reemplazos)

def dividir_en_palabras(cadena):
    """Divide una cadena en palabras."""
    if not cadena:
        return []

    # BUG 2: No maneja múltiples espacios ni puntuación
    return cadena.split(' ')

def extraer_dominio(email):
    """Extrae el dominio de un email."""
    if not email or '@' not in email:
        return ""

    partes = email.split('@')
    if len(partes) != 2:
        return ""

    return partes[1]

def enmascarar_email(email):
    """Enmascara parte de un email para privacidad."""
    if not email or '@' not in email:
        return ""

    partes = email.split('@')
    if len(partes) != 2:
        return ""

    usuario = partes[0]
    dominio = partes[1]

    if len(usuario) <= 2:
        usuario_mascarado = usuario
    else:
        usuario_mascarado = usuario[0] + '*' * (len(usuario) - 2) + usuario[-1]

    return f"{usuario_mascarado}@{dominio}"

def normalizar_espacios(cadena):
    """Normaliza los espacios en una cadena."""
    if not cadena:
        return ""

    palabras = cadena.split()
    return " ".join(palabras)

def truncar(cadena, longitud, sufijo="..."):
    """Trunca una cadena a una longitud máxima."""
    if not cadena:
        return ""

    if len(cadena) <= longitud:
        return cadena

    return cadena[:longitud - len(sufijo)] + sufijo

def es_anagrama(cadena1, cadena2):
    """Verifica si dos cadenas son anagramas."""
    if not cadena1 or not cadena2:
        return False

    # Normalizar: minúsculas y sin espacios
    c1 = cadena1.lower().replace(" ", "")
    c2 = cadena2.lower().replace(" ", "")

    return sorted(c1) == sorted(c2)
"""
Módulo de conversión de unidades.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    """Convierte grados Celsius a Kelvin."""
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    """Convierte Kelvin a Celsius."""
    # BUG 1: No valida que Kelvin sea >= 0 (absoluto)
    return kelvin - 273.15

def metros_a_kilometros(metros):
    """Convierte metros a kilómetros."""
    if metros < 0:
        raise ValueError("La distancia no puede ser negativa")
    return metros / 1000

def kilometros_a_metros(kilometros):
    """Convierte kilómetros a metros."""
    if kilometros < 0:
        raise ValueError("La distancia no puede ser negativa")
    return kilometros * 1000

def libras_a_kilogramos(libras):
    """Convierte libras a kilogramos."""
    if libras < 0:
        raise ValueError("El peso no puede ser negativo")
    return libras * 0.453592

def kilogramos_a_libras(kilogramos):
    """Convierte kilogramos a libras."""
    if kilogramos < 0:
        raise ValueError("El peso no puede ser negativo")
    return kilogramos / 0.453592

def galones_a_litros(galones):
    """Convierte galones a litros (galón estadounidense)."""
    if galones < 0:
        raise ValueError("El volumen no puede ser negativo")
    return galones * 3.78541

def litros_a_galones(litros):
    """Convierte litros a galones (galón estadounidense)."""
    if litros < 0:
        raise ValueError("El volumen no puede ser negativo")
    return litros / 3.78541

def millas_a_kilometros(millas):
    """Convierte millas a kilómetros."""
    if millas < 0:
        raise ValueError("La distancia no puede ser negativa")
    return millas * 1.60934

def kilometros_a_millas(kilometros):
    """Convierte kilómetros a millas."""
    if kilometros < 0:
        raise ValueError("La distancia no puede ser negativa")
    # BUG 2: Fórmula incorrecta (multiplica en lugar de dividir)
    return kilometros * 1.60934

def pies_a_metros(pies):
    """Convierte pies a metros."""
    if pies < 0:
        raise ValueError("La distancia no puede ser negativa")
    return pies * 0.3048

def metros_a_pies(metros):
    """Convierte metros a pies."""
    if metros < 0:
        raise ValueError("La distancia no puede ser negativa")
    return metros / 0.3048

def onzas_a_gramos(onzas):
    """Convierte onzas a gramos."""
    if onzas < 0:
        raise ValueError("El peso no puede ser negativo")
    return onzas * 28.3495

def gramos_a_onzas(gramos):
    """Convierte gramos a onzas."""
    if gramos < 0:
        raise ValueError("El peso no puede ser negativo")
    return gramos / 28.3495
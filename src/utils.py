"""
Módulo con funciones utilitarias varias.
ATENCIÓN: Hay 1 bug oculto en este archivo.
"""

def celsius_a_fahrenheit(celsius):
    """Convierte de Celsius a Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    """Convierte de Celsius a Kelvin."""
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    """Convierte de Kelvin a Celsius."""
    return kelvin - 273.15

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal."""
    if peso <= 0:
        return "El peso debe ser mayor a 0"

    if altura <= 0:
        return "La altura debe ser mayor a 0"

    return peso / (altura ** 2)

def categorizar_imc(imc):
    """Categoriza el IMC."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calcular_edad(año_nacimiento, año_actual):
    """Calcula la edad basada en el año de nacimiento."""
    if año_nacimiento > año_actual:
        return "El año de nacimiento no puede ser mayor al año actual"

    return año_actual - año_nacimiento

def es_bisiesto(anio):
    """Verifica si un año es bisiesto."""
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    else:
        return anio % 400 == 0

def dias_en_mes(mes, año):
    """Devuelve la cantidad de días en un mes."""
    if mes < 1 or mes > 12:
        return "El mes debe estar entre 1 y 12"

    if mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        # Febrero depende del año bisiesto
        return 29 if es_bisiesto(año) else 28
    else:
        return 31

def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

def mcd(a, b):
    """Calcula el Máximo Común Divisor."""
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    """Calcula el Mínimo Común Múltiplo."""
    # BUG: Error en el cálculo
    if a == 0 or b == 0:
        return 0
    return a * b // mcd(a, b)
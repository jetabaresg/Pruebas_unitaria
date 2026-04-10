"""
Módulo de cálculo de descuentos.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

def aplicar_descuento(precio, porcentaje):
    """Aplica un descuento a un precio."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    descuento = precio * (porcentaje / 100)
    return precio - descuento

def calcular_descuento(precio, porcentaje):
    """Calcula el monto del descuento."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    return precio * (porcentaje / 100)

def calcular_precio_final(precio, impuesto, descuento):
    """Calcula el precio final con impuesto y descuento."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if impuesto < 0:
        raise ValueError("El impuesto no puede ser negativo")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    # Primero aplicar el descuento
    precio_con_descuento = aplicar_descuento(precio, descuento)

    # Luego aplicar el impuesto
    # BUG 1: El impuesto se aplica incorrectamente
    impuesto_monto = precio * (impuesto / 100)
    precio_final = precio_con_descuento + impuesto_monto

    return precio_final

def descuento_por_volumen(cantidad, precio_unitario):
    """Calcula el precio con descuento por volumen."""
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    if precio_unitario < 0:
        raise ValueError("El precio unitario no puede ser negativo")

    subtotal = cantidad * precio_unitario

    # Descuentos por volumen
    if cantidad >= 100:
        descuento = 0.20
    elif cantidad >= 50:
        descuento = 0.15
    elif cantidad >= 20:
        descuento = 0.10
    elif cantidad >= 10:
        descuento = 0.05
    else:
        descuento = 0

    return aplicar_descuento(subtotal, descuento * 100)

def descuento_cumulativo(precio, descuentos):
    """Aplica múltiples descuentos de forma acumulativa."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if not descuentos:
        return precio

    precio_actual = precio

    for desc in descuentos:
        if desc < 0 or desc > 100:
            raise ValueError("Cada descuento debe estar entre 0 y 100")
        precio_actual = aplicar_descuento(precio_actual, desc)

    return precio_actual

def descuento_apilado(precio, descuentos):
    """Aplica múltiples descuentos de forma apilada (sumando porcentajes)."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if not descuentos:
        return precio

    # Sumar todos los descuentos
    total_descuento = sum(descuentos)

    # BUG 2: El descuento total puede exceder el 100%
    return aplicar_descuento(precio, total_descuento)
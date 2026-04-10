from src.descuentos import aplicar_descuento, calcular_descuento, calcular_precio_final,descuento_por_volumen,descuento_cumulativo, descuento_apilado
import pytest

def test_aplicar_descuento():
    precio = 1000
    porcentaje = 50

    resultado_esperado = 500

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == resultado_esperado

def test_aplicar_descuento_negativo():
    precio = -1000
    porcentaje = -10

    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_calcular_descuento():
    precio = 1000
    porcentaje = 40

    resultado_esperado = 400

    resultado = calcular_descuento(precio, porcentaje)

    assert resultado == resultado_esperado

def test_calcular_descuento_negativo():
    precio = -1000
    porcentaje = -40

    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)

def test_calcular_precio_final():
    precio = 1000
    impuesto = 19
    descuento = 40

    resultado_esperado = 714

    resultado = calcular_precio_final(precio, impuesto, descuento)

    assert resultado == resultado_esperado

def test_calcular_precio_final_negativo():
    precio = -1000
    impuesto = -19
    descuento = -40

    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)

def test_descuento_por_volumen():
    cantidad = 100
    precio_unitario = 10

    resultado_esperado = 800

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == resultado_esperado

def test_descuento_por_volumen_negativo():
    cantidad = -100
    precio_unitario = -10

    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)

def test_descuento_cumulativo():
    precio = 1000
    descuentos = [10, 20]

    resultado_esperado = 720

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == resultado_esperado

def test_descuento_cumulativo_negativo():
    precio = -1000
    descuentos = [-10, 200]

    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)

def test_descuento_apilado():
    precio = 1000
    descuentos = [10,20]

    resultado_esperado = 700

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == resultado_esperado

def test_descuento_apilado_neagtivo_mayor100():
    precio = -1000
    descuentos = [900]

    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)
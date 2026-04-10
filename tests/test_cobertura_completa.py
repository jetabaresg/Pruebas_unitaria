import pytest

from src.autenticacion import sanear_entrada, validar_token, verificar_codigo_2fa
from src.calculadora import (
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
    maximo,
    minimo,
    promedio,
)
from src.conversor import (
    galones_a_litros,
    gramos_a_onzas,
    kilogramos_a_libras,
    kilometros_a_metros,
    kilometros_a_millas,
    libras_a_kilogramos,
    litros_a_galones,
    metros_a_kilometros,
    metros_a_pies,
    millas_a_kilometros,
    onzas_a_gramos,
    pies_a_metros,
)
from src.csv_parser import (
    contar_columnas,
    contar_filas,
    csv_a_diccionarios,
    extraer_columna,
    filtrar_por_columna,
    leer_csv_como_lista,
    parse_csv_line,
    validar_csv,
)
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_apilado,
    descuento_cumulativo,
    descuento_por_volumen,
)
from src.fibonacci import (
    es_cuadrado_perfecto,
    es_fibonacci,
    fibonacci_iterativo,
    fibonacci_recursivo,
    fibonacci_serie,
)
from src.manipulador_texto import (
    capitalizar_palabras,
    convertir_a_titulo,
    contar_consonantes,
    contar_vocales,
    dividir_en_palabras,
    eliminar_duplicados,
    enmascarar_email,
    es_anagrama,
    es_palindromo,
    extraer_dominio,
    invertir_cadena,
    normalizar_espacios,
    reemplazar_subcadena,
    truncar,
)
from src.procesador_texto import (
    capitalizar_palabras as p_capitalizar_palabras,
    contar_palabras,
    contar_vocales as p_contar_vocales,
    convertir_mayusculas,
    convertir_minusculas,
    eliminar_espacios_extra,
    es_palindromo as p_es_palindromo,
    extraer_iniciales,
    invertir_texto,
    limpiar_texto,
    reemplazar_palabra,
)
from src.utils import es_primo
from src.validador import (
    validar_cedula,
    validar_edad,
    validar_email,
    validar_fecha,
    validar_password,
    validar_telefono,
    validar_url,
)


def test_autenticacion_ramas_faltantes():
    assert validar_token("g" * 64) is False
    assert verificar_codigo_2fa("", "123456") is False
    assert verificar_codigo_2fa("123456", "") is False
    assert sanear_entrada(None) == ""
    assert sanear_entrada(" <script>alert('x');</script> -- ") == "scriptalert(x)/script"


@pytest.mark.parametrize(
    "funcion,valor",
    [
        (promedio, []),
        (maximo, []),
        (minimo, []),
    ],
)
def test_calculadora_listas_vacias(funcion, valor):
    with pytest.raises(ValueError):
        funcion(valor)


def test_calculadora_dimensiones_negativas():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-1, 2)
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(2, -1)


@pytest.mark.parametrize(
    "funcion",
    [
        metros_a_kilometros,
        kilometros_a_metros,
        libras_a_kilogramos,
        kilogramos_a_libras,
        galones_a_litros,
        litros_a_galones,
        millas_a_kilometros,
        kilometros_a_millas,
        pies_a_metros,
        metros_a_pies,
        onzas_a_gramos,
        gramos_a_onzas,
    ],
)
def test_conversor_valores_negativos(funcion):
    with pytest.raises(ValueError):
        funcion(-1)


def test_csv_ramas_faltantes_generales():
    assert parse_csv_line(None) == []
    assert leer_csv_como_lista("") == []
    assert csv_a_diccionarios("", tiene_cabecera=True) == []
    assert csv_a_diccionarios("col1,col2", tiene_cabecera=True) == []
    assert csv_a_diccionarios("a,b\n1,2", tiene_cabecera=False) == []
    assert validar_csv("") is False
    assert extraer_columna("", 0) == []

    contenido = "a,b\n1,2\n3"
    assert extraer_columna(contenido, 1) == ["b", "2", ""]
    assert filtrar_por_columna(contenido, 0, "1") == [["1", "2"]]
    assert filtrar_por_columna("", 0, "x") == []

    assert contar_filas("") == 0
    assert contar_filas("a,b\n1,2") == 2
    assert contar_columnas("") == 0
    assert contar_columnas("a,b") == 2


class _SplitToEmpty:
    def split(self, _):
        return []


class _CsvLike:
    def __bool__(self):
        return True

    def strip(self):
        return _SplitToEmpty()


def test_csv_ramas_improbables_len_lineas_cero():
    assert validar_csv(_CsvLike()) is False
    assert contar_columnas(_CsvLike()) == 0


def test_descuentos_ramas_faltantes():
    with pytest.raises(ValueError):
        aplicar_descuento(100, 101)
    with pytest.raises(ValueError):
        calcular_descuento(100, -1)
    with pytest.raises(ValueError):
        calcular_precio_final(100, -1, 10)
    with pytest.raises(ValueError):
        calcular_precio_final(100, 19, 101)
    with pytest.raises(ValueError):
        descuento_por_volumen(10, -1)

    assert descuento_por_volumen(60, 10) == 510
    assert descuento_por_volumen(20, 10) == 180
    assert descuento_por_volumen(10, 10) == 95
    assert descuento_por_volumen(5, 10) == 50

    assert descuento_cumulativo(100, []) == 100
    with pytest.raises(ValueError):
        descuento_cumulativo(100, [10, 200])

    assert descuento_apilado(100, []) == 100
    with pytest.raises(ValueError):
        descuento_apilado(100, [80, 30])


def test_fibonacci_ramas_faltantes():
    assert fibonacci_iterativo(-1) == "El índice no puede ser negativo"
    assert fibonacci_iterativo(0) == 0
    assert fibonacci_iterativo(1) == 1

    assert fibonacci_recursivo(-1) == "El índice no puede ser negativo"
    assert fibonacci_recursivo(0) == 0
    assert fibonacci_recursivo(1) == 1

    assert fibonacci_serie(-1) == "El índice no puede ser negativo"
    assert fibonacci_serie(0) == [0]
    assert fibonacci_serie(1) == [0, 1]

    assert es_fibonacci(-8) is False
    assert es_fibonacci(0) is True
    assert es_fibonacci(1) is True
    assert es_cuadrado_perfecto(-4) is False
    assert es_cuadrado_perfecto(25) is True


@pytest.mark.parametrize(
    "funcion,entrada,salida",
    [
        (invertir_cadena, "", ""),
        (contar_vocales, "", 0),
        (contar_consonantes, "", 0),
        (es_palindromo, "", False),
        (eliminar_duplicados, "", ""),
        (capitalizar_palabras, "", ""),
        (convertir_a_titulo, "", ""),
        (dividir_en_palabras, "", []),
        (normalizar_espacios, "", ""),
    ],
)
def test_manipulador_entradas_vacias(funcion, entrada, salida):
    assert funcion(entrada) == salida


def test_manipulador_ramas_faltantes():
    assert reemplazar_subcadena("a-a-a", "a", "b", 2) == "b-b-a"
    assert reemplazar_subcadena("", "a", "b") == ""

    assert extraer_dominio("sin-arroba") == ""
    assert extraer_dominio("a@b@c") == ""

    assert enmascarar_email("aa@correo.com") == "aa@correo.com"
    assert enmascarar_email("invalido") == ""
    assert enmascarar_email("a@b@c") == ""

    assert truncar("", 3) == ""
    assert truncar("hola", 10) == "hola"

    assert es_anagrama("", "amor") is False
    assert es_anagrama("roma", "") is False


@pytest.mark.parametrize(
    "funcion",
    [
        contar_palabras,
        p_contar_vocales,
        invertir_texto,
        p_es_palindromo,
        eliminar_espacios_extra,
        convertir_mayusculas,
        convertir_minusculas,
        p_capitalizar_palabras,
        reemplazar_palabra,
        extraer_iniciales,
        limpiar_texto,
    ],
)
def test_procesador_texto_vacio(funcion):
    if funcion is reemplazar_palabra:
        assert funcion("", "a", "b") == ""
    else:
        assert funcion("") in (0, "", False)


def test_utils_rama_faltante():
    assert es_primo(1) is False


def test_validador_ramas_faltantes():
    assert validar_email("") is False
    assert validar_email("user@") is False
    assert validar_email("@dominio.com") is False
    assert validar_email("user@dominio") is False
    assert validar_email("a@b@c.com") is False

    assert validar_telefono("") is False

    assert validar_edad("20") is False
    assert validar_edad(121) is False

    assert validar_password("") is False
    assert validar_password("Ab1") is False
    assert validar_password("abcdefg1") is False
    assert validar_password("ABCDEFG1") is False
    assert validar_password("Abcdefgh") is False

    assert validar_url("") is False

    assert validar_fecha("1", 1, 2020) is False
    assert validar_fecha(1, 13, 2020) is False
    assert validar_fecha(1, 1, 1800) is False

    assert validar_cedula("") is False
    assert validar_cedula("12345") is False
    assert validar_cedula("12345678901") is False

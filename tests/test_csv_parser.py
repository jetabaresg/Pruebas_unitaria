import pytest
from src.csv_parser import csv_a_diccionarios,leer_csv_como_lista, validar_csv, extraer_columna, filtrar_por_columna, contar_filas, contar_columnas  

def test_parse_csv():

    csv_valido = "nombre,edad,ciudad\nJuan,30,Madrid\nAna,25,Barcelona"
    csv_invalido = "nombre,edad,ciudad\nJuan,30\nAna,25,Barcelona"
    csv_valido2 = "nombre edad ciudad\nJuan 30 Madrid\nAna 25 Barcelona\nPedro 40 Valencia"

    assert validar_csv(csv_valido) == True
    assert validar_csv(csv_invalido) == False
    assert validar_csv(csv_valido2) == True

def test_leer_csv_como_lista():
    csv_con_comas = "nombre,edad,ciudad\nJuan,30,Madrid\nAna,25,Barcelona"
    csv_sin_comas = "nombre edad ciudad\nJuan 30 Madrid\nAna 25 Barcelona\nPedro 40 Valencia"

    assert leer_csv_como_lista(csv_con_comas) == [["nombre", "edad", "ciudad"], ["Juan", "30", "Madrid"], ["Ana", "25", "Barcelona"]]
    assert leer_csv_como_lista(csv_sin_comas) == [["nombre edad ciudad"], ["Juan 30 Madrid"], ["Ana 25 Barcelona"], ["Pedro 40 Valencia"]]

def test_csv_a_diccionarios():
    csv_con_comas = "nombre,edad,ciudad\nJuan,30,Madrid\nAna,25,Barcelona"
    csv_sin_comas = "nombre edad ciudad\nJuan 30 Madrid\nAna 25 Barcelona\nPedro 40 Valencia"

    assert csv_a_diccionarios(csv_con_comas) == [{"nombre": "Juan", "edad": "30", "ciudad": "Madrid"}, {"nombre": "Ana", "edad": "25", "ciudad": "Barcelona"}]
    assert csv_a_diccionarios(csv_sin_comas) == [{"nombre": "Juan", "edad": "30", "ciudad": "Madrid"}, {"nombre": "Ana", "edad": "25", "ciudad": "Barcelona"}, {"nombre": "Pedro", "edad": "40", "ciudad": "Valencia"}]


"""
Módulo de parsing de archivos CSV.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

import csv
from io import StringIO

def parse_csv_line(linea):
    """Parsea una línea de CSV separada por comas."""
    if not linea:
        return []

    # Usa el parser estándar para manejar comillas escapadas y comas dentro de campos.
    return next(csv.reader(StringIO(linea)))

def leer_csv_como_lista(contenido_csv):
    """Lee el contenido de un CSV y retorna una lista de listas."""
    if not contenido_csv:
        return []

    lineas = contenido_csv.strip().split('\n')
    resultado = []

    for linea in lineas:
        resultado.append(parse_csv_line(linea))

    return resultado

def csv_a_diccionarios(contenido_csv, tiene_cabecera=True):
    """Convierte contenido CSV a una lista de diccionarios."""
    lineas = leer_csv_como_lista(contenido_csv)

    if not lineas:
        return []

    if tiene_cabecera and len(lineas) > 1:
        cabeceras = lineas[0]
        datos = lineas[1:]

        if len(cabeceras) == 1 and ',' not in cabeceras[0] and ' ' in cabeceras[0]:
            cabeceras = cabeceras[0].split()

        resultado = []
        for fila in datos:
            if len(fila) == 1 and ',' not in fila[0] and ' ' in fila[0]:
                fila = fila[0].split()

            fila_dict = {}
            for i, cabecera in enumerate(cabeceras):
                fila_dict[cabecera] = fila[i] if i < len(fila) else ""
            resultado.append(fila_dict)

        return resultado

    return []

def validar_csv(contenido_csv):
    """Valida si el contenido CSV tiene formato básico correcto."""
    if not contenido_csv:
        return False

    lineas = contenido_csv.strip().split('\n')

    if len(lineas) == 0:
        return False

    # Verificar que todas las líneas tengan el mismo número de comas
    num_comas = lineas[0].count(',')

    for linea in lineas:
        if linea.count(',') != num_comas:
            return False

    return True

def extraer_columna(contenido_csv, indice_columna):
    """Extrae una columna específica de un CSV."""
    lineas = leer_csv_como_lista(contenido_csv)

    if not lineas:
        return []

    columna = []
    for fila in lineas:
        if indice_columna < len(fila):
            columna.append(fila[indice_columna])
        else:
            columna.append("")

    return columna

def filtrar_por_columna(contenido_csv, indice_columna, valor):
    """Filtra las filas donde una columna tenga un valor específico."""
    lineas = leer_csv_como_lista(contenido_csv)

    if not lineas:
        return []

    resultado = []
    for fila in lineas:
        if indice_columna < len(fila):
            if fila[indice_columna] == valor:
                resultado.append(fila)

    return resultado

def contar_filas(contenido_csv):
    """Cuenta el número de filas en un CSV."""
    if not contenido_csv:
        return 0

    lineas = contenido_csv.strip().split('\n')
    return len(lineas)

def contar_columnas(contenido_csv):
    """Cuenta el número de columnas en un CSV (basado en la primera fila)."""
    if not contenido_csv:
        return 0

    lineas = contenido_csv.strip().split('\n')

    if len(lineas) == 0:
        return 0

    primera_linea = lineas[0]
    return len(parse_csv_line(primera_linea))
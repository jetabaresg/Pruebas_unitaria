# 🎯 PROYECTO: PRUEBAS UNITARIAS - CÓDIGO

---

## 📁 ESTRUCTURA DEL PROYECTO

```
proyecto-pruebas-unitarias/
├── src/
│   ├── __init__.py
│   ├── calculadora.py              # Operaciones matemáticas básicas
│   ├── validador.py                # Validación de datos
│   ├── procesador_texto.py         # Procesamiento de texto
│   ├── fibonacci.py                # Algoritmo de Fibonacci
│   ├── descuentos.py               # Cálculo de descuentos
│   ├── utils.py                    # Funciones utilitarias
│   ├── autenticacion.py            # Autenticación y seguridad
│   ├── conversor.py                # Conversión de unidades
│   ├── csv_parser.py               # Parsing de archivos CSV
│   └── manipulador_texto.py        # Manipulación de cadenas
├── tests/
│   ├── __init__.py
│   ├── test_calculadora.py
│   ├── test_validador.py
│   ├── test_procesador_texto.py
│   ├── test_fibonacci.py
│   ├── test_descuentos.py
│   ├── test_utils.py
│   ├── test_autenticacion.py
│   ├── test_conversor.py
│   ├── test_csv_parser.py
│   └── test_manipulador_texto.py
├── README.md
└── requirements.txt
```

---

## 📋 INSTRUCCIONES 

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/cesarpalacios/pruebas_unitarias_devops.git
cd pruebas_unitarias_devops
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar pruebas
```bash
pytest
```

### Paso 5: Ver reporte de cobertura
```bash
pytest --cov=src --cov-report=html
```

---

## 🎮 DESAFÍOS

### Desafío 1: El Detective de Bugs
Hay **14 bugs ocultos** en los archivos de `src/`. Escriban pruebas para encontrarlos y corregirlos.

- `calculadora.py`: 2 bugs
- `validador.py`: 1 bug
- `procesador_texto.py`: 1 bug
- `fibonacci.py`: 1 bug
- `descuentos.py`: 2 bugs
- `utils.py`: 1 bug
- `autenticacion.py`: 2 bugs
- `conversor.py`: 2 bugs
- `csv_parser.py`: 2 bugs
- `manipulador_texto.py`: 2 bugs

### Desafío 2: El Arquitecto de Pruebas
Cada prueba debe seguir la estructura AAA (Arrange, Act, Assert).

### Desafío 3: Casos Límite
Encuentren TODOS los casos límite posibles para cada función.

### Desafío 4: Cobertura Completa
Logren una cobertura del 100% en todos los archivos.

---

## 🏆 OBJETIVO FINAL

El ejercicio termina cuando:

1. **Todas las pruebas estén en estado PASSED**
2. **Todos los 14 bugs hayan sido encontrados y corregidos**
3. **Se haya alcanzado el 100% de cobertura en los archivos principales**

---

## 📝 EJEMPLO DE PRUEBA

```python
# test_calculadora.py
import pytest
from src.calculadora import sumar

def test_sumar_positivos():
    """Prueba suma de números positivos."""
    # Arrange
    a = 5
    b = 3
    resultado_esperado = 8

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == resultado_esperado
```

---

## 💡 CONSEJOS

1. Una prueba, un propósito
2. Nombres descriptivos
3. Casos normales, límites y errores
4. Organización clara
5. Comentarios cuando sea necesario
6. Revise el informe de errores y corrija los bugs encontrados
7. Empiecen con módulos más simples y avancen a los más complejos

---

## 🚀 LISTO PARA EMPEZAR

¡Comiencen a escribir pruebas, encuentren los 14 bugs ocultos y corrijan el código hasta que todas las pruebas pasen!

---

**Buena suerte!** 🎯

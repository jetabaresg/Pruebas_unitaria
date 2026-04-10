#!/bin/bash

# Script para subir el proyecto a Git
# Autor: César Palacios
# Fecha: 8 de abril de 2026

echo "🚀 CONFIGURANDO REPOSITORIO GIT PARA PROYECTO DE PRUEBAS UNITARIAS"
echo "======================================================================"

# Inicializar git si no existe
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositorio Git..."
    git init
    echo "✅ Repositorio inicializado"
else
    echo "✅ Repositorio ya existe"
fi

# Agregar todos los archivos
echo ""
echo "📦 Agregando archivos..."
git add .
echo "✅ Archivos agregados"

# Primer commit
echo ""
echo "💾 Creando primer commit..."
git commit -m "Proyecto inicial: Código para pruebas unitarias

- Módulos: calculadora, validador, procesador_texto, fibonacci, descuentos, utils
- 5 bugs ocultos para encontrar
- Listo para que los estudiantes escriban pruebas"
echo "✅ Commit creado"

# Preguntar por la URL del repositorio
echo ""
echo "======================================================================"
echo "📋 INSTRUCCIONES PARA SUBIR A GITHUB:"
echo "======================================================================"
echo ""
echo "1. Crear un nuevo repositorio en GitHub (si no existe)"
echo "2. Copiar la URL del repositorio (ej: https://github.com/usuario/repo.git)"
echo "3. Ejecutar:"
echo "   git remote add origin <URL_DEL_REPOSITORIO>"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "======================================================================"
echo "🎯 PROYECTO LISTO PARA USO DE ESTUDIANTES"
echo "======================================================================"
echo ""
echo "📋 Pasos para los estudiantes:"
echo "1. Clonar: git clone <URL_DEL_REPOSITORIO>"
echo "2. Entrar: cd proyecto-pruebas-unitarias"
echo "3. Crear entorno: python -m venv venv"
echo "4. Activar: source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)"
echo "5. Instalar: pip install -r requirements.txt"
echo "6. Crear pruebas en tests/"
echo "7. Ejecutar: pytest"
echo "8. Ver cobertura: pytest --cov=src --cov-report=html"
echo ""
echo "🎮 DESAFÍOS:"
echo "- 5 bugs ocultos en el código"
echo "- Escribir pruebas con estructura AAA"
echo "- Encontrar todos los casos límite"
echo "- Lograr 100% de cobertura"
echo ""
echo "🏆 PUNTUACIÓN:"
echo "- 1 punto por cada prueba válida"
echo "- 2 puntos por cada caso límite encontrado"
echo "- 3 puntos por cada bug encontrado"
echo "- 5 puntos por archivo con 100% de cobertura"
echo ""
echo "======================================================================"
echo "✅ ¡LISTO!"
echo "======================================================================"
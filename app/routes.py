from flask import Blueprint, render_template, jsonify, request
import subprocess
import tempfile
import os
import shutil
import uuid
import json
import re

main = Blueprint('main', __name__)

# ---------------------------------------------------------------------------
# Datos hardcodeados
# ---------------------------------------------------------------------------

CURSOS = [
    {
        "id": "iic2233-2026-1",
        "nombre": "Programación Avanzada",
        "codigo": "IIC2233",
        "periodo": "2026-1"
    }
]

SECCIONES = [
    {
        "id": "materias",
        "nombre": "Materias",
        "tipo": "materia",
        "items": [
            {"id": "semana-01", "nombre": "Semana 1: Introducción",              "descripcion": "Repaso de Python y entorno de trabajo"},
            {"id": "semana-03", "nombre": "Semana 3: Estructuras de Datos",      "descripcion": "Listas, Diccionarios, Sets, Stacks, Queues"},
            {"id": "semana-04", "nombre": "Semana 4: OOP Avanzado",              "descripcion": "Herencia, Clases Abstractas, Mixins"},
            {"id": "semana-06", "nombre": "Semana 6: Excepciones e Iteradores",  "descripcion": "Try/Except, Iterables, Generators"},
            {"id": "semana-07", "nombre": "Semana 7: Programación Funcional",    "descripcion": "Map, Filter, Reduce, Lambdas"},
            {"id": "semana-09", "nombre": "Semana 9: Interfaces Gráficas I",     "descripcion": "PyQt6, Signals, Slots"},
            {"id": "semana-10", "nombre": "Semana 10: Serialización y Networking I",  "descripcion": "JSON, Pickle, Sockets TCP"},
            {"id": "semana-11", "nombre": "Semana 11: Serialización y Networking II", "descripcion": "Threads, Servidores concurrentes"},
            {"id": "semana-14", "nombre": "Semana 14: Interfaces Gráficas II",   "descripcion": "PyQt6 avanzado, Modelos/Vistas"},
            {"id": "semana-15", "nombre": "Semana 15: Tópicos Avanzados",        "descripcion": "Decoradores, Metaclases, Type Hints"}
        ]
    },
    {
        "id": "actividades",
        "nombre": "Actividades",
        "tipo": "actividad",
        "items": [
            {"id": "AC1",     "nombre": "AC1: Tabla de Medallistas",      "descripcion": "OOP básico con clases Medallista, País y TablaPuntajes"},
            {"id": "AC2",     "nombre": "AC2: Estadísticas de Premios",   "descripcion": "Estructuras de datos con namedtuples y diccionarios"},
            {"id": "AC3",     "nombre": "AC3: Genética",                  "descripcion": "Herencia, clases abstractas y mixins"},
            {"id": "AC4",     "nombre": "AC4: Laberinto",                 "descripcion": "Algoritmos de búsqueda en grafos"},
            {"id": "AC5",     "nombre": "AC5: Simulación de Eventos",     "descripcion": "Programación funcional y eventos"},
            {"id": "AC6",     "nombre": "AC6: Cliente-Servidor",          "descripcion": "Networking y sockets TCP/IP"},
            {"id": "AC7",     "nombre": "AC7: Laberinto Avanzado",        "descripcion": "Búsqueda heurística y estadísticas"},
            {"id": "ACBonus", "nombre": "AC Bonus: Wikipedia Queries",    "descripcion": "Consultas a Wikipedia y serialización"}
        ]
    },
    {
        "id": "evaluaciones",
        "nombre": "Interrogaciones",
        "tipo": "evaluacion",
        "items": [
            {"id": "I1",     "nombre": "Interrogación 1",  "descripcion": "OOP, Estructuras de Datos, Iteradores"},
            {"id": "I2",     "nombre": "Interrogación 2",  "descripcion": "Funcional, Networking, GUI"},
            {"id": "Examen", "nombre": "Examen Final",     "descripcion": "Todos los contenidos del semestre"}
        ]
    }
]

# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api/cursos')
def get_cursos():
    return jsonify(CURSOS)


@main.route('/api/cursos/<curso_id>/secciones')
def get_secciones(curso_id):
    return jsonify(SECCIONES)


@main.route('/api/ejercicio/<ejercicio_id>')
def get_ejercicio(ejercicio_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(base_dir, 'ejercicios', f'{ejercicio_id}.json')
    if not os.path.exists(ruta):
        return jsonify({"error": "Ejercicio no encontrado"}), 404
    with open(ruta, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)


# ---------------------------------------------------------------------------
# Helpers de sandbox
# ---------------------------------------------------------------------------

def _crear_sandbox(ejercicio_id: str, codigo: str, archivos: dict) -> str:
    """Crea un directorio temporal de sandbox y devuelve su ruta."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sandbox_root = os.path.join(base_dir, 'sandbox')
    os.makedirs(sandbox_root, exist_ok=True)

    sandbox_path = os.path.join(sandbox_root, str(uuid.uuid4()))
    os.makedirs(sandbox_path)

    # Escribir el código principal
    with open(os.path.join(sandbox_path, 'main.py'), 'w', encoding='utf-8') as f:
        f.write(codigo)

    # Copiar archivos auxiliares del ejercicio si existen
    ejercicio_dir = os.path.join(base_dir, 'ejercicios', ejercicio_id)
    if os.path.isdir(ejercicio_dir):
        shutil.copytree(ejercicio_dir, sandbox_path, dirs_exist_ok=True)

    # Escribir archivos adicionales enviados por el cliente
    if archivos:
        for nombre, contenido in archivos.items():
            ruta_archivo = os.path.join(sandbox_path, nombre)
            os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)

    return sandbox_path


def _limpiar_sandbox(sandbox_path: str):
    """Elimina el directorio de sandbox."""
    try:
        shutil.rmtree(sandbox_path, ignore_errors=True)
    except Exception:
        pass


def _parse_pytest_summary(output: str):
    """Extrae conteos de passed/failed de la salida de pytest."""
    passed = 0
    failed = 0
    match = re.search(r'(\d+) passed', output)
    if match:
        passed = int(match.group(1))
    match = re.search(r'(\d+) failed', output)
    if match:
        failed = int(match.group(1))
    return passed, failed


# ---------------------------------------------------------------------------
# Ruta /api/ejecutar
# ---------------------------------------------------------------------------

@main.route('/api/ejecutar', methods=['POST'])
def ejecutar():
    data = request.get_json(force=True, silent=True) or {}
    codigo = data.get('codigo', '')
    ejercicio_id = data.get('ejercicio_id', '')
    archivos = data.get('archivos', {})

    sandbox_path = _crear_sandbox(ejercicio_id, codigo, archivos)
    try:
        resultado = subprocess.run(
            ['python', 'main.py'],
            cwd=sandbox_path,
            capture_output=True,
            text=True,
            timeout=10
        )
        return jsonify({
            "stdout":   resultado.stdout,
            "stderr":   resultado.stderr,
            "exitcode": resultado.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            "stdout":   "",
            "stderr":   "Error: tiempo de ejecución excedido (10 s)",
            "exitcode": 1
        })
    finally:
        _limpiar_sandbox(sandbox_path)


# ---------------------------------------------------------------------------
# Ruta /api/test
# ---------------------------------------------------------------------------

@main.route('/api/test', methods=['POST'])
def test():
    data = request.get_json(force=True, silent=True) or {}
    codigo = data.get('codigo', '')
    ejercicio_id = data.get('ejercicio_id', '')
    archivos = data.get('archivos', {})

    sandbox_path = _crear_sandbox(ejercicio_id, codigo, archivos)
    try:
        resultado = subprocess.run(
            ['python', '-m', 'pytest', 'tests_publicos/', '-v', '--tb=short'],
            cwd=sandbox_path,
            capture_output=True,
            text=True,
            timeout=30
        )
        salida_completa = resultado.stdout + resultado.stderr
        passed, failed = _parse_pytest_summary(salida_completa)
        return jsonify({
            "stdout":   resultado.stdout,
            "stderr":   resultado.stderr,
            "exitcode": resultado.returncode,
            "passed":   passed,
            "failed":   failed
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            "stdout":   "",
            "stderr":   "Error: tiempo de ejecución de tests excedido (30 s)",
            "exitcode": 1,
            "passed":   0,
            "failed":   0
        })
    finally:
        _limpiar_sandbox(sandbox_path)

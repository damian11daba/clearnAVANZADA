from flask import Blueprint, render_template, jsonify, request, send_from_directory
import subprocess
import os
import shutil
import uuid
import json

main = Blueprint('main', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'curso.json')

def cargar_curso():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"semanas": [], "actividades": [], "evaluaciones": []}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/curso')
def get_curso():
    return jsonify(cargar_curso())

@main.route('/data/<path:filename>')
def serve_data(filename):
    data_dir = os.path.join(BASE_DIR, 'data')
    return send_from_directory(data_dir, filename)

@main.route('/static/<path:filename>')
def serve_static(filename):
    static_dir = os.path.join(BASE_DIR, 'static')
    return send_from_directory(static_dir, filename)

@main.route('/api/ejecutar', methods=['POST'])
def ejecutar():
    data = request.get_json(silent=True) or {}
    codigo = data.get('codigo', '')
    archivos = data.get('archivos', {})

    sandbox_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sandbox')
    os.makedirs(sandbox_root, exist_ok=True)
    sandbox_path = os.path.join(sandbox_root, str(uuid.uuid4()))
    os.makedirs(sandbox_path, exist_ok=True)

    try:
        # Escribir código principal
        with open(os.path.join(sandbox_path, 'main.py'), 'w', encoding='utf-8') as f:
            f.write(codigo)

        # Escribir archivos adicionales
        for nombre, contenido in archivos.items():
            fpath = os.path.join(sandbox_path, nombre)
            os.makedirs(os.path.dirname(fpath), exist_ok=True)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(contenido)

        resultado = subprocess.run(
            ['python', 'main.py'],
            cwd=sandbox_path,
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8',
            errors='replace'
        )
        return jsonify({
            'stdout': resultado.stdout,
            'stderr': resultado.stderr,
            'exitcode': resultado.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            'stdout': '',
            'stderr': '⏱️ Tiempo límite excedido (10 segundos).',
            'exitcode': -1
        })
    except Exception as e:
        return jsonify({
            'stdout': '',
            'stderr': str(e),
            'exitcode': -1
        })
    finally:
        shutil.rmtree(sandbox_path, ignore_errors=True)

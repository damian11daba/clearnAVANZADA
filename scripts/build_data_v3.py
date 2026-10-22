import os
import glob
import json
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR1 = r"C:\Users\ThinkPad\OneDrive\Desktop\repositorio 3.0"
BASE_DIR2 = r"C:\Users\ThinkPad\OneDrive\Desktop\P.A"

def find_folder(folder_name):
    candidates = [
        os.path.join(BASE_DIR1, "contenidos", folder_name),
        os.path.join(BASE_DIR2, "contenidos", folder_name),
        os.path.join(BASE_DIR1, "contenidos", "semana-09-interfaces_graficas_1", folder_name)
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def parse_notebook(folder_path, nb_filename):
    full_path = os.path.join(folder_path, nb_filename)
    if not os.path.exists(full_path):
        return []
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception:
        return []

    bloques = []
    cells = nb.get("cells", [])
    start = 1 if cells and cells[0].get("cell_type") == "markdown" and "IIC2233" in "".join(cells[0].get("source", [])) else 0

    for c in cells[start:]:
        ctype = c.get("cell_type")
        source = "".join(c.get("source", []))
        if not source.strip():
            continue
        if ctype == "markdown":
            bloques.append({
                "tipo": "teoria",
                "contenido": source
            })
        elif ctype == "code":
            out_texts = []
            for out in c.get("outputs", []):
                if "text" in out:
                    out_texts.append("".join(out["text"]))
                elif "data" in out and "text/plain" in out["data"]:
                    out_texts.append("".join(out["data"]["text/plain"]))
            bloques.append({
                "tipo": "codigo",
                "contenido": source,
                "output": "\n".join(out_texts).strip()
            })
    return bloques

# Importar configuraciones de ejercicios
from ejercicios_data import SEMANAS_DETALLADAS, ACTIVIDADES_SINGLE_FILE, EVALUACIONES_DATA

def build():
    print("Compilando plataforma ClearnP.A con 7 ejercicios por sección y Actividades Single-File...")
    semanas_compiladas = []

    for cfg in SEMANAS_DETALLADAS:
        folder_path = find_folder(cfg["folder"])
        lecciones = []

        if folder_path and os.path.isdir(folder_path):
            nb_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".ipynb") and not ".ipynb_checkpoints" in f])
            for nb_file in nb_files:
                bloques = parse_notebook(folder_path, nb_file)
                clean_title = nb_file.replace(".ipynb", "").replace("-", " ").replace("_", " ").capitalize()
                clean_title = re.sub(r'^\d+\s*', '', clean_title)

                lecciones.append({
                    "id": nb_file.replace(".ipynb", "").replace(".", "_"),
                    "filename": nb_file,
                    "titulo": clean_title,
                    "bloques": bloques or []
                })

        semanas_compiladas.append({
            "id": cfg["id"],
            "nombre": cfg["nombre"],
            "dificultad": cfg["dificultad"],
            "descripcion": cfg["descripcion"],
            "actividad_id": cfg["actividad_id"],
            "lecciones": lecciones,
            "ejercicios_guiados": cfg["ejercicios"]
        })
        print(f"  ✓ {cfg['nombre']}: {len(lecciones)} lecciones, {len(cfg['ejercicios'])} ejercicios guiados")

    print(f"  ✓ {len(ACTIVIDADES_SINGLE_FILE)} Actividades (en formato UN SOLO ARCHIVO)")
    print(f"  ✓ {len(EVALUACIONES_DATA)} Evaluaciones escritas/prácticas")

    curso_data = {
        "curso": {
            "id": "iic2233-2026-1",
            "codigo": "IIC2233",
            "nombre": "Programación Avanzada",
            "periodo": "2026-1",
            "universidad": "Pontificia Universidad Católica de Chile",
            "total_semanas": len(semanas_compiladas),
            "total_actividades": len(ACTIVIDADES_SINGLE_FILE),
            "total_evaluaciones": len(EVALUACIONES_DATA),
            "total_ejercicios_practica": sum(len(s["ejercicios_guiados"]) for s in semanas_compiladas)
        },
        "semanas": semanas_compiladas,
        "actividades": ACTIVIDADES_SINGLE_FILE,
        "evaluaciones": EVALUACIONES_DATA
    }

    # Guardar en local clearnP.A/data/curso.json
    output_dir = r"C:\Users\ThinkPad\OneDrive\Desktop\clearnP.A\data"
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "curso.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(curso_data, f, ensure_ascii=False, indent=2)
    print(f"\nGuardado exitoso en {json_path} ({os.path.getsize(json_path) / 1024:.1f} KB)")

    # Guardar en static/data/curso.json
    static_data_dir = r"C:\Users\ThinkPad\OneDrive\Desktop\clearnP.A\static\data"
    os.makedirs(static_data_dir, exist_ok=True)
    static_json_path = os.path.join(static_data_dir, "curso.json")
    with open(static_json_path, "w", encoding="utf-8") as f:
        json.dump(curso_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado exitoso en {static_json_path}")

    # Guardar en app/static/data/curso.json para Flask
    app_static_dir = r"C:\Users\ThinkPad\OneDrive\Desktop\clearnP.A\app\static\data"
    os.makedirs(app_static_dir, exist_ok=True)
    app_json_path = os.path.join(app_static_dir, "curso.json")
    with open(app_json_path, "w", encoding="utf-8") as f:
        json.dump(curso_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado exitoso en {app_json_path}")

if __name__ == "__main__":
    build()

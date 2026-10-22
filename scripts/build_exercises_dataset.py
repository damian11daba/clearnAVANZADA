import os
import json
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Cargar SEMANAS_DETALLADAS y ACTIVIDADES_SINGLE_FILE actuales
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ejercicios_data import SEMANAS_DETALLADAS, ACTIVIDADES_SINGLE_FILE, EVALUACIONES_DATA

# Generar soluciones completas para los 17 que tenían pass,
# y generar codigo_inicial (skeleton) y pistas para todos.

SOLUCIONES_OVERRIDE = {
    "s01-e1": """class Mascota:
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie

    def presentarse(self) -> str:
        return f"Hola, soy {self.nombre} y soy un {self.especie}."
""",
    "s01-e2": """class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)
""",
    "s01-e3": """class Punto2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Punto2D(x={self.x}, y={self.y})"
""",
    "s01-e4": """class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self._saldo = 0
        self.saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            raise ValueError("Saldo no puede ser negativo")
        self._saldo = valor
""",
    "s01-e5": """class Usuario:
    total_usuarios = 0

    def __init__(self, username: str):
        self.username = username
        Usuario.total_usuarios += 1
        self.id = Usuario.total_usuarios
""",
    "s01-e6": """def procesar_alumnos(texto_csv: str) -> dict[str, float]:
    resultado = {}
    for linea in texto_csv.strip().split("\\n"):
        linea = linea.strip()
        if linea:
            nombre, nota = linea.split(",")
            resultado[nombre.strip()] = float(nota.strip())
    return resultado
""",
    "s01-e7": """class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota: float):
        if not (1.0 <= nota <= 7.0):
            raise ValueError("Nota fuera de rango")
        self.notas.append(nota)

    def promedio(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def mejor_estudiante(self) -> str:
        if not self.estudiantes:
            return ""
        mejor = max(self.estudiantes, key=lambda e: e.promedio())
        return mejor.nombre
""",
    "s02-e1": """def limpiar_nombre(archivo: str) -> str:
    return archivo.strip().replace(" ", "_").lower()
""",
    "s02-e2": """import os

def obtener_extension(ruta: str) -> str:
    nombre, ext = os.path.splitext(ruta)
    if ext.startswith("."):
        return ext[1:].lower()
    return ""
""",
    "s02-e5": """def filtrar_archivos_python(lista_archivos: list[str]) -> list[str]:
    return [f for f in lista_archivos if f.lower().endswith(".py")]
""",
    "s02-e7": """def clasificar_archivos(rutas: list[str]) -> dict[str, list[str]]:
    categorias = {'codigo': [], 'datos': [], 'documentos': []}
    for r in rutas:
        ext = r.lower().split('.')[-1]
        if ext in ['py']:
            categorias['codigo'].append(r)
        elif ext in ['csv', 'json', 'dcc']:
            categorias['datos'].append(r)
        elif ext in ['pdf', 'md', 'txt']:
            categorias['documentos'].append(r)
    return categorias
""",
    "s03-e5": """from collections import deque

class FilaAtencion:
    def __init__(self):
        self.cola = deque()

    def llegar(self, nombre: str):
        self.cola.append(nombre)

    def atender(self) -> str | None:
        if self.cola:
            return self.cola.popleft()
        return None
""",
    "s03-e6": """from collections import defaultdict

def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    agrupados = defaultdict(list)
    for p in palabras:
        agrupados[len(p)].append(p)
    return dict(agrupados)
""",
    "s03-e7": """from collections import defaultdict

class RedSocial:
    def __init__(self):
        self.grafo = defaultdict(set)

    def agregar_amigo(self, u1: str, u2: str):
        self.grafo[u1].add(u2)
        self.grafo[u2].add(u1)

    def amigos_en_comun(self, u1: str, u2: str) -> set[str]:
        return self.grafo[u1] & self.grafo[u2]

    def sugerir_amigos(self, u: str) -> set[str]:
        sugerencias = set()
        for amigo in self.grafo[u]:
            sugerencias |= self.grafo[amigo]
        return sugerencias - self.grafo[u] - {u}
""",
    "s04-e1": """class Persona:
    def __init__(self, nombre: str, rut: str):
        self.nombre = nombre
        self.rut = rut

class Estudiante(Persona):
    def __init__(self, nombre: str, rut: str, carrera: str):
        super().__init__(nombre, rut)
        self.carrera = carrera
""",
    "s04-e2": """class Notificacion:
    def enviar(self, msg: str) -> str:
        return f'Enviando: {msg}'

class Email(Notificacion):
    def enviar(self, msg: str) -> str:
        return f'Email: {msg}'

class SMS(Notificacion):
    def enviar(self, msg: str) -> str:
        return f'SMS: {msg}'
""",
    "s10-e4": """import json

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def reconstruir_punto(d: dict):
    if 'x' in d and 'y' in d:
        return Punto(d['x'], d['y'])
    return d
"""
}

def generar_skeleton_y_pista(ej_id, solucion):
    """
    Toma la solución y genera un esqueleto (codigo_inicial) y una pista con código parcial.
    """
    lineas = solucion.strip().split("\n")
    skeleton_lineas = []
    pista_lineas = []

    # Detectar imports iniciales
    imports = []
    resto = []
    for l in lineas:
        if l.startswith("import ") or l.startswith("from "):
            imports.append(l)
        else:
            resto.append(l)

    skeleton_lineas.extend(imports)
    if imports:
        skeleton_lineas.append("")

    # Parsear funciones y clases
    i = 0
    while i < len(resto):
        line = resto[i]
        # Función o método
        if re.match(r'^\s*def\s+', line):
            indent = len(line) - len(line.lstrip())
            sig = line
            docstring = []
            i += 1
            if i < len(resto) and ('"""' in resto[i] or "'''" in resto[i]):
                docstring.append(resto[i])
                if resto[i].count('"""') < 2 and resto[i].count("'''") < 2:
                    i += 1
                    while i < len(resto) and ('"""' not in resto[i] and "'''" not in resto[i]):
                        docstring.append(resto[i])
                        i += 1
                    if i < len(resto):
                        docstring.append(resto[i])
                        i += 1
                else:
                    i += 1

            # Extraer 1-2 líneas de cuerpo para la pista
            body_sample = []
            while i < len(resto):
                curr = resto[i]
                curr_indent = len(curr) - len(curr.lstrip()) if curr.strip() else indent + 4
                if curr.strip() and curr_indent <= indent and not curr.strip().startswith("#"):
                    break
                if curr.strip() and not curr.strip().startswith('"""'):
                    body_sample.append(curr)
                i += 1

            skeleton_lineas.append(sig)
            for d in docstring:
                skeleton_lineas.append(d)
            skeleton_lineas.append(" " * (indent + 4) + "# TODO: Implementa tu solución aquí")
            skeleton_lineas.append(" " * (indent + 4) + "pass")
            skeleton_lineas.append("")

            # Guardar pista
            if body_sample:
                pista_lineas.append(f"# Pista para {sig.strip()}:")
                for bs in body_sample[:2]:
                    pista_lineas.append("  " + bs.strip())
            continue

        # Declaración de clase
        elif re.match(r'^\s*class\s+', line):
            skeleton_lineas.append(line)
            i += 1
            continue
        elif line.strip().startswith("@"):
            skeleton_lineas.append(line)
            i += 1
            continue
        elif not line.strip():
            skeleton_lineas.append("")
            i += 1
            continue
        else:
            # Variable de clase o asignación simple
            indent = len(line) - len(line.lstrip())
            if indent == 4 and "=" in line and not line.strip().startswith("self."):
                skeleton_lineas.append(line)
            i += 1

    clean_skeleton = "\n".join(skeleton_lineas).strip() + "\n"
    clean_pista = "\n".join(pista_lineas).strip()
    if not clean_pista:
        clean_pista = "# Pista: Analiza los tipos de datos de entrada y qué debe retornar la función."

    return clean_skeleton, clean_pista

def procesar_todo():
    print("Procesando los 84 ejercicios para quitar respuestas y agregar pistas + solución...")
    ejercicios_actualizados = 0

    for s in SEMANAS_DETALLADAS:
        for ej in s["ejercicios"]:
            eid = ej["id"]
            # 1. Obtener solución completa
            if eid in SOLUCIONES_OVERRIDE:
                sol = SOLUCIONES_OVERRIDE[eid].strip()
            else:
                sol = ej.get("codigo_inicial", "").strip()

            if eid == "s03-e7":
                ej["tests_code"] = """rs = RedSocial()
rs.agregar_amigo('Ana', 'Beto')
rs.agregar_amigo('Ana', 'Carlos')
rs.agregar_amigo('Beto', 'Daniel')
assert rs.amigos_en_comun('Ana', 'Daniel') == {'Beto'}
assert rs.sugerir_amigos('Ana') == {'Daniel'}
print('✅ Reto 7 superado exitosamente!')
"""

            # 2. Generar esqueleto (sin respuesta) y pista
            skel, pista = generar_skeleton_y_pista(eid, sol)

            # 3. Asignar campos
            ej["solucion"] = sol
            ej["codigo_inicial"] = skel
            ej["pista"] = f"💡 **Pista y estructura recomendada:**\n```python\n{pista}\n```"

            ejercicios_actualizados += 1

    print(f"✓ {ejercicios_actualizados} ejercicios actualizados con éxito")

    # Procesar ACTIVIDADES_SINGLE_FILE
    print("Procesando Actividades para asegurar formato esqueleto + pista + solución...")
    for ac in ACTIVIDADES_SINGLE_FILE:
        full_sol = ac["codigo_inicial"]
        ac["solucion"] = full_sol
        ac["pista"] = f"💡 **Pista para {ac['id']}:**\nRevisa la estructura de clases del enunciado. Implementa primero los constructores `__init__`, luego los métodos de cálculo y finalmente el flujo principal."
        
        # En AC1 por ejemplo, dejamos el esqueleto con pass en los métodos clave:
        if ac["id"] == "AC1":
            ac["codigo_inicial"] = re.sub(
                r'def agregar_medallista\(self, medallista: Medallista\):.*?(?=def ordenar_paises)',
                'def agregar_medallista(self, medallista: Medallista):\n        # TODO: Implementar puntaje por medalla (Oro: 5, Plata: 3, Bronce: 1)\n        pass\n\n    ',
                full_sol,
                flags=re.DOTALL
            )
            ac["codigo_inicial"] = re.sub(
                r'def cargar_medallistas\(texto_datos: str\) -> list\[Medallista\]:.*?(?=def crear_tabla)',
                'def cargar_medallistas(texto_datos: str) -> list[Medallista]:\n    # TODO: Parsear lineas CSV y retornar lista de Medallista\n    pass\n\n',
                ac["codigo_inicial"],
                flags=re.DOTALL
            )
        elif ac["id"] == "AC2":
            ac["codigo_inicial"] = re.sub(
                r'def get_top_winner\(self\).*?(?=def get_top_winner_in_award)',
                'def get_top_winner(self) -> tuple[str, int]:\n        # TODO: Retornar (nombre, total_premios) de la persona con mas premios\n        pass\n\n    ',
                full_sol,
                flags=re.DOTALL
            )
            ac["codigo_inicial"] = re.sub(
                r'def get_egot_winners\(self\).*?(?=if __name__)',
                'def get_egot_winners(self) -> set[str]:\n        # TODO: Retornar set con los nombres de quienes ganaron EGOT\n        pass\n\n\n',
                ac["codigo_inicial"],
                flags=re.DOTALL
            )
        elif ac["id"] == "AC4":
            ac["codigo_inicial"] = re.sub(
                r'def resolver_bfs\(self\) -> list\[tuple\[int, int\]\]:.*?(?=if __name__)',
                'def resolver_bfs(self) -> list[tuple[int, int]]:\n        # TODO: Implementar busqueda en amplitud (BFS) para encontrar camino mas corto\n        pass\n\n\n',
                full_sol,
                flags=re.DOTALL
            )

    # Validar que todas las soluciones pasen sus tests
    print("\nValidando que todas las SOLUCIONES pasen sus tests:")
    passed = 0
    failed = 0
    for s in SEMANAS_DETALLADAS:
        for ej in s["ejercicios"]:
            code = ej["solucion"] + "\n" + ej.get("tests_code", "")
            try:
                exec(code, {})
                passed += 1
            except Exception as e:
                failed += 1
                print(f"  ✕ Falló {ej['id']}: {e}")
    print(f"Resultado de validación de soluciones: {passed} de {passed+failed} pasaron exitosamente!")

    # Guardar en ejercicios_data_v4.py
    target_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ejercicios_data.py")
    with open(target_py, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Datos actualizados con codigo_inicial (esqueleto sin respuesta), pista y solucion."""\n\n')
        f.write(f"SEMANAS_DETALLADAS = {repr(SEMANAS_DETALLADAS)}\n\n")
        f.write(f"ACTIVIDADES_SINGLE_FILE = {repr(ACTIVIDADES_SINGLE_FILE)}\n\n")
        f.write(f"EVALUACIONES_DATA = {repr(EVALUACIONES_DATA)}\n")
    print(f"\nArchivo {target_py} actualizado con éxito")

if __name__ == "__main__":
    procesar_todo()

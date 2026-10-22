import os
import json
import re
import sys
import copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ejercicios_data

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

def crear_skeleton(solucion_code: str) -> str:
    """Convierte el código completo en una plantilla limpia para el alumno."""
    lines = solucion_code.strip().split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Mantener imports, decoradores y declaraciones de clase
        if (stripped.startswith("import ") or stripped.startswith("from ") or
            stripped.startswith("@") or stripped.startswith("class ")):
            out.append(line)
            i += 1
            continue

        # Si es una función o método
        if re.match(r'^\s*def\s+', line):
            indent = len(line) - len(line.lstrip())
            out.append(line)
            i += 1
            # Si hay docstring, conservarlo
            if i < len(lines) and ('"""' in lines[i] or "'''" in lines[i]):
                out.append(lines[i])
                if lines[i].count('"""') < 2 and lines[i].count("'''") < 2:
                    i += 1
                    while i < len(lines) and ('"""' not in lines[i] and "'''" not in lines[i]):
                        out.append(lines[i])
                        i += 1
                    if i < len(lines):
                        out.append(lines[i])
                        i += 1
                else:
                    i += 1
            # Agregar el placeholder
            out.append(" " * (indent + 4) + "# TODO: Escribe tu solución aquí")
            out.append(" " * (indent + 4) + "pass")
            out.append("")
            # Saltar el cuerpo de la función
            while i < len(lines):
                cur = lines[i]
                cur_indent = len(cur) - len(cur.lstrip()) if cur.strip() else indent + 4
                if cur.strip() and cur_indent <= indent and not cur.strip().startswith("#"):
                    break
                i += 1
            continue

        # Variables de clase (ej: total_usuarios = 0)
        if len(line) - len(line.lstrip()) == 4 and "=" in line and not stripped.startswith("self."):
            out.append(line)
            i += 1
            continue

        if not stripped:
            out.append("")
            i += 1
            continue

        i += 1

    return "\n".join(out).strip() + "\n"

def crear_pista(solucion_code: str, objetivo: str) -> str:
    """Extrae líneas clave de la solución para ofrecer una pista útil."""
    lines = [l.strip() for l in solucion_code.strip().split("\n") if l.strip()]
    hints = []
    for l in lines:
        if (l.startswith("return ") or "yield " in l or ".append(" in l or
            ".pop" in l or "with " in l or "super()" in l or "re." in l or
            "json." in l or "pickle." in l or "threading." in l):
            hints.append(l)

    partial = "\n".join(hints[:3]) if hints else "# Analiza las firmas de función y qué tipos de datos debes retornar."
    return f"💡 **Pista para guiarte:**\n{objetivo}\n\nLíneas clave recomendadas:\n```python\n{partial}\n```"

def main():
    print("1. Extrayendo y verificando soluciones de los 84 ejercicios...")
    semanas = copy.deepcopy(ejercicios_data.SEMANAS_DETALLADAS)

    # Corregir test de s03-e7
    for s in semanas:
        for ej in s["ejercicios"]:
            if ej["id"] == "s03-e7":
                ej["tests_code"] = """rs = RedSocial()
rs.agregar_amigo('Ana', 'Beto')
rs.agregar_amigo('Ana', 'Carlos')
rs.agregar_amigo('Beto', 'Daniel')
assert rs.amigos_en_comun('Ana', 'Daniel') == {'Beto'}
assert rs.sugerir_amigos('Ana') == {'Daniel'}
print('✅ Reto 7 superado exitosamente!')
"""

    # Asignar soluciones completas
    for s in semanas:
        for ej in s["ejercicios"]:
            eid = ej["id"]
            if eid in SOLUCIONES_OVERRIDE:
                ej["solucion"] = SOLUCIONES_OVERRIDE[eid].strip()
            else:
                ej["solucion"] = ej["codigo_inicial"].strip()

    # Validar que el 100% de las soluciones pasen los tests
    print("2. Verificando que las soluciones pasen el 100% de los tests:")
    passed = 0
    failed = 0
    for s in semanas:
        for ej in s["ejercicios"]:
            code = ej["solucion"] + "\n" + ej.get("tests_code", "")
            try:
                exec(code, {})
                passed += 1
            except Exception as e:
                failed += 1
                print(f"  ✕ ERROR en {ej['id']}: {e}")

    print(f"   Resultado: {passed} de {passed+failed} pasaron exitosamente!")
    assert failed == 0, f"Fallaron {failed} ejercicios"

    # Ahora generar codigo_inicial (esqueleto sin solución) y pista
    print("3. Generando esqueletos sin solución y pistas para cada ejercicio...")
    for s in semanas:
        for ej in s["ejercicios"]:
            ej["codigo_inicial"] = crear_skeleton(ej["solucion"])
            ej["pista"] = crear_pista(ej["solucion"], ej.get("objetivo", ""))

    # Procesar Actividades Single-File
    print("4. Adaptando Actividades (AC) a formato esqueleto + pista + solución...")
    actividades = copy.deepcopy(ejercicios_data.ACTIVIDADES_SINGLE_FILE)
    for ac in actividades:
        full = ac["codigo_inicial"]
        ac["solucion"] = full
        ac["pista"] = f"💡 **Pista para {ac['id']}:**\n{ac['descripcion']}\n\nComienza implementando los métodos base en las clases y luego el flujo principal con las llamadas a funciones auxiliares."

        # Reemplazar métodos clave por esqueletos
        if ac["id"] == "AC1":
            ac["codigo_inicial"] = re.sub(
                r'def agregar_medallista\(self, medallista: Medallista\):.*?(?=def ordenar_paises)',
                'def agregar_medallista(self, medallista: Medallista):\n        # TODO: Implementar puntaje por medalla (Oro: 5, Plata: 3, Bronce: 1)\n        pass\n\n    ',
                full,
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
                full,
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
                full,
                flags=re.DOTALL
            )

    evaluaciones = copy.deepcopy(ejercicios_data.EVALUACIONES_DATA)

    # Compilar dataset final en disco
    print("5. Escribiendo dataset limpio en ejercicios_data.py...")
    target_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ejercicios_data.py")
    with open(target_py, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Dataset oficial ClearnP.A con codigo_inicial (esqueleto sin respuesta), pista y solucion."""\n\n')
        f.write(f"SEMANAS_DETALLADAS = {repr(semanas)}\n\n")
        f.write(f"ACTIVIDADES_SINGLE_FILE = {repr(actividades)}\n\n")
        f.write(f"EVALUACIONES_DATA = {repr(evaluaciones)}\n")

    print("✓ Dataset completado y validado al 100%!")

if __name__ == "__main__":
    main()

import os
import glob
import json
import re
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = r"C:\Users\ThinkPad\OneDrive\Desktop\repositorio 3.0"
CONTENIDOS_DIR = os.path.join(BASE_DIR, "contenidos")
SYLLABUS_DIR = os.path.join(BASE_DIR, "Syllabus")
ACTIVIDADES_DIR = os.path.join(SYLLABUS_DIR, "Actividades")
STUDENT_ACT_DIR = os.path.join(BASE_DIR, "damian11daba-iic2233-2026-1", "Actividades")

SEMANAS_CONFIG = [
    {
        "id": "semana-01",
        "nombre": "Semana 1: Introducción & OOP Básico",
        "folder": "semana-01-introduccion",
        "dificultad": 1,
        "descripcion": "Repaso de programación orientada a objetos en Python, encapsulamiento, atributos y manejo de archivos I/O.",
        "actividad_id": None,
        "ejercicios_guiados": [
            {
                "id": "s01-e1",
                "titulo": "1. Creando tu primera Clase: Mascota",
                "nivel": "Fácil",
                "dificultad_num": 1,
                "objetivo": "Aprender a definir una clase con constructor `__init__` y atributos de instancia.",
                "descripcion": "Crea una clase `Mascota` que reciba `nombre` (str) y `especie` (str). Debe tener un método `presentarse()` que retorne: `'Hola, soy {nombre} y soy un {especie}.'`",
                "codigo_inicial": "class Mascota:\n    def __init__(self, nombre: str, especie: str):\n        # Completa los atributos\n        pass\n\n    def presentarse(self) -> str:\n        # Retorna el saludo esperado\n        pass\n\n# Prueba rápida\nm = Mascota('Firulais', 'Perro')\nprint(m.presentarse())\n",
                "tests_code": "m = Mascota('Pelusa', 'Gato')\nassert m.presentarse() == 'Hola, soy Pelusa y soy un Gato.', f'Esperado: Hola, soy Pelusa y soy un Gato., Obtenido: {m.presentarse()}'\nm2 = Mascota('Bobby', 'Perro')\nassert m2.presentarse() == 'Hola, soy Bobby y soy un Perro.'\nprint('✅ Todos los tests pasaron!')\n"
            },
            {
                "id": "s01-e2",
                "titulo": "2. Encapsulamiento y Properties",
                "nivel": "Fácil-Medio",
                "dificultad_num": 2,
                "objetivo": "Usar `@property` y `@setter` para validar atributos privados.",
                "descripcion": "Implementa una clase `CuentaBancaria` con saldo inicial. El saldo nunca puede ser negativo. Si se intenta asignar un valor menor a 0, debe lanzar un `ValueError('El saldo no puede ser negativo')`.",
                "codigo_inicial": "class CuentaBancaria:\n    def __init__(self, titular: str, saldo_inicial: float = 0):\n        self.titular = titular\n        self._saldo = 0\n        self.saldo = saldo_inicial\n\n    @property\n    def saldo(self):\n        return self._saldo\n\n    @saldo.setter\n    def saldo(self, valor):\n        # Valida que valor >= 0, sino lanza ValueError\n        pass\n",
                "tests_code": "c = CuentaBancaria('Ana', 100)\nassert c.saldo == 100\nc.saldo = 50\nassert c.saldo == 50\ntry:\n    c.saldo = -10\n    assert False, 'Debió lanzar ValueError'\nexcept ValueError:\n    pass\nprint('✅ Tests de property pasaron con éxito!')\n"
            }
        ]
    },
    {
        "id": "semana-02",
        "nombre": "Semana 2: Modularización & Entorno",
        "folder": "semana-02-entorno_de_trabajo",
        "dificultad": 1,
        "descripcion": "Buenas prácticas de código (PEP 8), modularización, imports y manejo de paths con os y pathlib.",
        "actividad_id": None,
        "ejercicios_guiados": [
            {
                "id": "s02-e1",
                "titulo": "1. Normalización de Nombres de Archivo",
                "nivel": "Fácil",
                "dificultad_num": 1,
                "objetivo": "Manipular strings y rutas para garantizar nombres válidos.",
                "descripcion": "Escribe una función `limpiar_nombre_archivo(nombre: str) -> str` que elimine espacios iniciales y finales, reemplace espacios internos por guiones bajos `_` y lo convierta a minúsculas, manteniendo la extensión intacta.",
                "codigo_inicial": "def limpiar_nombre_archivo(nombre: str) -> str:\n    # Completa la función\n    pass\n",
                "tests_code": "assert limpiar_nombre_archivo('  Mi Documento Final.PDF  ') == 'mi_documento_final.pdf'\nassert limpiar_nombre_archivo('Foto 2026.png') == 'foto_2026.png'\nprint('✅ Nombres normalizados correctamente!')\n"
            }
        ]
    },
    {
        "id": "semana-03",
        "nombre": "Semana 3: Estructuras de Datos",
        "folder": "semana-03-estructuras_de_datos",
        "dificultad": 2,
        "descripcion": "Tuplas, namedtuples, Stacks (LIFO), Colas (FIFO), Diccionarios, Sets y empaquetamiento (*args, **kwargs).",
        "actividad_id": "AC2",
        "ejercicios_guiados": [
            {
                "id": "s03-e1",
                "titulo": "1. Desempaquetado y NamedTuples",
                "nivel": "Fácil",
                "dificultad_num": 1,
                "objetivo": "Crear y usar `namedtuple` para almacenar registros inmutables y legibles.",
                "descripcion": "Crea una `namedtuple` llamada `Punto` con campos `x` e `y`. Luego crea una función `distancia_origen(p: Punto) -> float` que retorne la distancia euclidiana al origen: sqrt(x² + y²).",
                "codigo_inicial": "from collections import namedtuple\nimport math\n\n# Define Punto aquí\nPunto = None\n\ndef distancia_origen(p) -> float:\n    # Calcula y retorna la distancia\n    pass\n",
                "tests_code": "P = namedtuple('Punto', ['x', 'y'])\np = P(3, 4)\nassert distancia_origen(p) == 5.0, f'Esperado 5.0, obtenido {distancia_origen(p)}'\nprint('✅ Ejercicio de namedtuple completado!')\n"
            },
            {
                "id": "s03-e2",
                "titulo": "2. Verificador de Paréntesis con Stack (Pila)",
                "nivel": "Medio",
                "dificultad_num": 2,
                "objetivo": "Implementar un algoritmo clásico usando la estructura de datos Stack (LIFO).",
                "descripcion": "Escribe una función `es_valido_parentesis(cadena: str) -> bool` que determine si una cadena de paréntesis `()[]{}` está correctamente balanceada y cerrada.",
                "codigo_inicial": "def es_valido_parentesis(cadena: str) -> bool:\n    stack = []\n    pares = {')': '(', ']': '[', '}': '{'}\n    for char in cadena:\n        # Completa la lógica usando el stack\n        pass\n    return len(stack) == 0\n",
                "tests_code": "assert es_valido_parentesis('()[]{}') == True\nassert es_valido_parentesis('([{}])') == True\nassert es_valido_parentesis('(]') == False\nassert es_valido_parentesis('([)]') == False\nprint('✅ Verificador de paréntesis correcto!')\n"
            },
            {
                "id": "s03-e3",
                "titulo": "3. Conteo de Frecuencias con Diccionarios",
                "nivel": "Fácil-Medio",
                "dificultad_num": 2,
                "objetivo": "Agrupar y contar elementos eficientemente.",
                "descripcion": "Escribe una función `palabras_mas_frecuentes(texto: str, n: int = 3) -> list[tuple[str, int]]` que cuente las palabras de un texto (ignorando mayúsculas/minúsculas) y retorne las `n` más frecuentes ordenadas de mayor a menor frecuencia.",
                "codigo_inicial": "def palabras_mas_frecuentes(texto: str, n: int = 3) -> list[tuple[str, int]]:\n    # Usa un diccionario o Counter\n    pass\n",
                "tests_code": "res = palabras_mas_frecuentes('gato perro gato pajaro gato perro pez', 2)\nassert res == [('gato', 3), ('perro', 2)], f'Obtenido: {res}'\nprint('✅ Conteo de frecuencias completado!')\n"
            }
        ]
    },
    {
        "id": "semana-04",
        "nombre": "Semana 4: OOP Avanzado & Patrones",
        "folder": "semana-04-oop_avanzado",
        "dificultad": 3,
        "descripcion": "Herencia simple y múltiple, Method Resolution Order (MRO), polimorfismo, clases abstractas (ABC) y decoradores.",
        "actividad_id": "AC1",
        "ejercicios_guiados": [
            {
                "id": "s04-e1",
                "titulo": "1. Jerarquía de Figuras y Clases Abstractas",
                "nivel": "Fácil-Medio",
                "dificultad_num": 2,
                "objetivo": "Implementar una clase abstracta con métodos obligatorios para subclases.",
                "descripcion": "Crea una clase abstracta `Figura(ABC)` con el método abstracto `area() -> float`. Luego implementa `Circulo(radio)` y `Rectangulo(ancho, alto)` que hereden de ella.",
                "codigo_inicial": "from abc import ABC, abstractmethod\nimport math\n\nclass Figura(ABC):\n    @abstractmethod\n    def area(self) -> float:\n        pass\n\nclass Circulo(Figura):\n    def __init__(self, radio: float):\n        self.radio = radio\n    def area(self) -> float:\n        return math.pi * (self.radio ** 2)\n\nclass Rectangulo(Figura):\n    # Implementa Rectangulo\n    pass\n",
                "tests_code": "c = Circulo(2)\nr = Rectangulo(4, 5)\nassert round(c.area(), 2) == 12.57\nassert r.area() == 20.0\nprint('✅ Clases abstractas y polimorfismo implementados!')\n"
            },
            {
                "id": "s04-e2",
                "titulo": "2. Decorador de Tiempo de Ejecución",
                "nivel": "Medio",
                "dificultad_num": 3,
                "objetivo": "Crear un decorador en Python que envuelva una función y agregue funcionalidad.",
                "descripcion": "Escribe un decorador `@contador_llamadas` que cuente cuántas veces ha sido invocada una función. La función decorada debe tener un atributo `llamadas` accesible que comience en 0 y aumente en cada llamada.",
                "codigo_inicial": "import functools\n\ndef contador_llamadas(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        wrapper.llamadas += 1\n        return func(*args, **kwargs)\n    wrapper.llamadas = 0\n    return wrapper\n\n@contador_llamadas\ndef saludar(nombre):\n    return f'Hola {nombre}'\n",
                "tests_code": "assert saludar.llamadas == 0\nsaludar('Juan')\nsaludar('Pedro')\nassert saludar.llamadas == 2\nprint('✅ Decorador de llamadas exitoso!')\n"
            }
        ]
    },
    {
        "id": "semana-06",
        "nombre": "Semana 6: Excepciones e Iteradores",
        "folder": "semana-06-excepciones_iterables_e_iteradores",
        "dificultad": 3,
        "descripcion": "Manejo robusto de errores, excepciones personalizadas, protocolo de iteración (__iter__, __next__), funciones generadoras (yield) y listas ligadas.",
        "actividad_id": "AC3",
        "ejercicios_guiados": [
            {
                "id": "s06-e1",
                "titulo": "1. Excepción Personalizada para Validación",
                "nivel": "Fácil",
                "dificultad_num": 2,
                "objetivo": "Definir excepciones que hereden de `Exception` con mensajes informativos.",
                "descripcion": "Crea una excepción `EdadInvalidaError` que herede de `ValueError`. Escribe una función `registrar_usuario(nombre: str, edad: int)` que lance `EdadInvalidaError` si `edad < 18`.",
                "codigo_inicial": "class EdadInvalidaError(ValueError):\n    pass\n\ndef registrar_usuario(nombre: str, edad: int):\n    # Valida y lanza excepción si edad < 18\n    pass\n",
                "tests_code": "try:\n    registrar_usuario('Nico', 15)\n    assert False, 'Debio lanzar excepcion'\nexcept EdadInvalidaError:\n    pass\nprint('✅ Excepción personalizada verificada!')\n"
            },
            {
                "id": "s06-e2",
                "titulo": "2. Generador Infinito de Fibonacci",
                "nivel": "Medio",
                "dificultad_num": 3,
                "objetivo": "Usar `yield` para producir una secuencia perezosa (lazy evaluation) que consume memoria constante O(1).",
                "descripcion": "Crea una función generadora `generar_fibonacci()` que produzca la secuencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8...",
                "codigo_inicial": "def generar_fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n",
                "tests_code": "gen = generar_fibonacci()\nvalores = [next(gen) for _ in range(7)]\nassert valores == [0, 1, 1, 2, 3, 5, 8], f'Obtenido: {valores}'\nprint('✅ Generador de Fibonacci verificado!')\n"
            }
        ]
    },
    {
        "id": "semana-07",
        "nombre": "Semana 7: Programación Funcional",
        "folder": "semana-07-programacion_funcional",
        "dificultad": 4,
        "descripcion": "Funciones puras, inmutabilidad, lambdas, map, filter, functools.reduce, y combinadores funcionales.",
        "actividad_id": "AC4",
        "ejercicios_guiados": [
            {
                "id": "s07-e1",
                "titulo": "1. Pipeline de Datos con Map y Filter",
                "nivel": "Fácil-Medio",
                "dificultad_num": 2,
                "objetivo": "Encadenar transformaciones sobre iterables sin bucles for explícitos.",
                "descripcion": "Dada una lista de números enteros, escribe `filtrar_y_cuadrar(numeros: list[int]) -> list[int]` que filtre los números pares y luego retorne sus cuadrados.",
                "codigo_inicial": "def filtrar_y_cuadrar(numeros: list[int]) -> list[int]:\n    # Usa filter y map, o comprensiones de listas\n    pass\n",
                "tests_code": "assert filtrar_y_cuadrar([1, 2, 3, 4, 5, 6]) == [4, 16, 36]\nprint('✅ Pipeline funcional completado!')\n"
            },
            {
                "id": "s07-e2",
                "titulo": "2. Acumulaciones con Reduce",
                "nivel": "Medio",
                "dificultad_num": 3,
                "objetivo": "Utilizar `functools.reduce` para agregar elementos en una sola estructura.",
                "descripcion": "Usa `reduce` para encontrar el producto total de una lista de números, retornando 1 si la lista está vacía.",
                "codigo_inicial": "from functools import reduce\n\ndef producto_total(numeros: list[int]) -> int:\n    if not numeros:\n        return 1\n    return reduce(lambda x, y: x * y, numeros)\n",
                "tests_code": "assert producto_total([2, 3, 4]) == 24\nassert producto_total([]) == 1\nprint('✅ Reduce verificado!')\n"
            }
        ]
    },
    {
        "id": "semana-09",
        "nombre": "Semana 9: Interfaces Gráficas & Threading",
        "folder": "semana-09-interfaces_graficas_1",
        "dificultad": 4,
        "descripcion": "PyQt6 (ventanas, widgets, layouts, signals y slots) y programación concurrente con threading (Locks, eventos, sincronización).",
        "actividad_id": "AC5",
        "ejercicios_guiados": [
            {
                "id": "s09-e1",
                "titulo": "1. Sincronización Segura con Lock",
                "nivel": "Medio-Avanzado",
                "dificultad_num": 4,
                "objetivo": "Evitar Race Conditions en variables compartidas entre múltiples threads.",
                "descripcion": "Implementa una clase `ContadorSeguro` que tenga un método `incrementar()` protegido por un `threading.Lock()`.",
                "codigo_inicial": "import threading\n\nclass ContadorSeguro:\n    def __init__(self):\n        self.valor = 0\n        self.lock = threading.Lock()\n\n    def incrementar(self):\n        with self.lock:\n            self.valor += 1\n",
                "tests_code": "c = ContadorSeguro()\nthreads = [threading.Thread(target=lambda: [c.incrementar() for _ in range(100)]) for _ in range(10)]\nfor t in threads: t.start()\nfor t in threads: t.join()\nassert c.valor == 1000, f'Esperado 1000, obtenido {c.valor}'\nprint('✅ Concurrencia con Lock protegida con éxito!')\n"
            }
        ]
    },
    {
        "id": "semana-10",
        "nombre": "Semana 10: Serialización & Networking I",
        "folder": "semana-10-serializacion_y_networkin_1",
        "dificultad": 5,
        "descripcion": "Serialización JSON con encoders personalizados, arquitectura cliente-servidor y Web Services REST.",
        "actividad_id": "AC6",
        "ejercicios_guiados": [
            {
                "id": "s10-e1",
                "titulo": "1. JSON Encoder para Clases Personalizadas",
                "nivel": "Medio",
                "dificultad_num": 3,
                "objetivo": "Serializar objetos propios a JSON usando `json.JSONEncoder`.",
                "descripcion": "Crea una clase `Libro` con `titulo` y `autor`. Implementa un encoder `LibroEncoder` para que `json.dumps(libro, cls=LibroEncoder)` retorne un JSON válido con campos `titulo` y `autor`.",
                "codigo_inicial": "import json\n\nclass Libro:\n    def __init__(self, titulo: str, autor: str):\n        self.titulo = titulo\n        self.autor = autor\n\nclass LibroEncoder(json.JSONEncoder):\n    def default(self, obj):\n        if isinstance(obj, Libro):\n            return {'titulo': obj.titulo, 'autor': obj.autor}\n        return super().default(obj)\n",
                "tests_code": "l = Libro('Cien Años de Soledad', 'G. García Márquez')\ns = json.dumps(l, cls=LibroEncoder)\nassert 'Cien Años de Soledad' in s\nprint('✅ JSON Encoder implementado con éxito!')\n"
            }
        ]
    },
    {
        "id": "semana-11",
        "nombre": "Semana 11: Serialización & Networking II",
        "folder": "semana-11-serializacion_y_networking_2",
        "dificultad": 5,
        "descripcion": "Pickle, empaquetamiento y desempaquetamiento de bytes (bytearrays, big/little endian), sockets TCP/IP con Python.",
        "actividad_id": "AC6",
        "ejercicios_guiados": [
            {
                "id": "s11-e1",
                "titulo": "1. Protocolo de Mensajes con Longitud en Bytes",
                "nivel": "Medio-Avanzado",
                "dificultad_num": 4,
                "objetivo": "Diseñar paquetes de red con cabecera de longitud fija y cuerpo variable.",
                "descripcion": "Escribe `empaquetar_mensaje(texto: str) -> bytearray` que cree un paquete con: 4 bytes iniciales (big-endian) que indican el largo del texto, seguidos por el texto codificado en UTF-8.",
                "codigo_inicial": "def empaquetar_mensaje(texto: str) -> bytearray:\n    payload = texto.encode('utf-8')\n    largo = len(payload).to_bytes(4, byteorder='big')\n    return bytearray(largo + payload)\n\ndef desempaquetar_mensaje(datos: bytearray) -> str:\n    largo = int.from_bytes(datos[:4], byteorder='big')\n    return datos[4:4+largo].decode('utf-8')\n",
                "tests_code": "msg = 'Hola Mundo Sockets'\npkt = empaquetar_mensaje(msg)\nassert len(pkt) == 4 + len(msg.encode('utf-8'))\nassert desempaquetar_mensaje(pkt) == msg\nprint('✅ Protocolo de mensajes por bytes verificado!')\n"
            }
        ]
    },
    {
        "id": "semana-14",
        "nombre": "Semana 14: GUI Avanzada con QThreads",
        "folder": "semana-14-interfaces_graficas_2",
        "dificultad": 5,
        "descripcion": "Separación Front/Back, comunicación asíncrona mediante QThread y señales para no congelar la interfaz.",
        "actividad_id": "AC7",
        "ejercicios_guiados": []
    },
    {
        "id": "semana-15",
        "nombre": "Semana 15: Tópicos Avanzados & Grafos",
        "folder": "semana-15-topicos-avanzados",
        "dificultad": 5,
        "descripcion": "Expresiones regulares (Regex), representación de grafos (listas y matrices de adyacencia), algoritmos de búsqueda (BFS y DFS), NumPy y Pandas.",
        "actividad_id": "ACBonus",
        "ejercicios_guiados": [
            {
                "id": "s15-e1",
                "titulo": "1. Validación de Correos con Regex",
                "nivel": "Fácil-Medio",
                "dificultad_num": 2,
                "objetivo": "Utilizar expresiones regulares del módulo `re` para validar formatos de texto.",
                "descripcion": "Escribe `es_correo_uc_valido(correo: str) -> bool` que retorne True si el correo tiene formato `usuario@uc.cl` o `usuario@estudiante.uc.cl`.",
                "codigo_inicial": "import re\n\ndef es_correo_uc_valido(correo: str) -> bool:\n    patron = r'^[a-zA-Z0-9._%+-]+@(estudiante\\.)?uc\\.cl$'\n    return bool(re.match(patron, correo))\n",
                "tests_code": "assert es_correo_uc_valido('damin.bravo@estudiante.uc.cl') == True\nassert es_correo_uc_valido('profesor@uc.cl') == True\nassert es_correo_uc_valido('test@gmail.com') == False\nprint('✅ Regex de correo validada!')\n"
            },
            {
                "id": "s15-e2",
                "titulo": "2. Búsqueda en Amplitud (BFS) en un Grafo",
                "nivel": "Avanzado",
                "dificultad_num": 4,
                "objetivo": "Implementar BFS para encontrar el camino más corto en un grafo no ponderado.",
                "descripcion": "Dado un grafo representado como diccionario de adyacencia `grafo = {'A': ['B', 'C'], ...}`, escribe `camino_mas_corto(grafo, inicio, fin) -> list[str]`.",
                "codigo_inicial": "from collections import deque\n\ndef camino_mas_corto(grafo: dict, inicio: str, fin: str) -> list[str]:\n    cola = deque([[inicio]])\n    visitados = {inicio}\n    while cola:\n        camino = cola.popleft()\n        nodo = camino[-1]\n        if nodo == fin:\n            return camino\n        for vecino in grafo.get(nodo, []):\n            if vecino not in visitados:\n                visitados.add(vecino)\n                cola.append(camino + [vecino])\n    return []\n",
                "tests_code": "g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}\nassert camino_mas_corto(g, 'A', 'E') == ['A', 'B', 'D', 'E'] or camino_mas_corto(g, 'A', 'E') == ['A', 'C', 'D', 'E']\nprint('✅ BFS para camino más corto completado!')\n"
            }
        ]
    }
]

def parse_notebook(folder_name, nb_filename):
    """Lee un notebook y extrae bloques de teoría y ejemplos de código."""
    matches = glob.glob(os.path.join(CONTENIDOS_DIR, folder_name, nb_filename))
    if not matches:
        return None
    try:
        with open(matches[0], "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        return None

    bloques = []
    cells = nb.get("cells", [])
    
    # Ignorar copyright header
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
            # Extraer outputs
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

def cargar_actividades():
    """Lee las actividades de Syllabus y las compila con archivos y enunciados."""
    actividades = []
    ac_names = ["AC1", "AC2", "AC3", "AC4", "AC5", "AC6", "AC7", "ACBonus"]
    
    for ac_id in ac_names:
        ac_path = os.path.join(ACTIVIDADES_DIR, ac_id)
        if not os.path.exists(ac_path):
            continue
            
        archivos_soporte = {}
        for root, dirs, files in os.walk(ac_path):
            for f in files:
                if f.endswith(('.py', '.dcc', '.txt', '.json', '.MD', '.md')) and not f.endswith('Enunciado.pdf'):
                    fpath = os.path.join(root, f)
                    relpath = os.path.relpath(fpath, ac_path).replace('\\', '/')
                    try:
                        with open(fpath, 'r', encoding='utf-8', errors='replace') as file_obj:
                            archivos_soporte[relpath] = file_obj.read()
                    except:
                        pass
        
        # Enunciado resumido / objetivo
        titulo_ac = f"{ac_id}: Actividad Práctica Evaluada"
        if ac_id == "AC1":
            titulo_ac = "AC1: Tabla de Medallistas Olímpicos (OOP y Colecciones)"
            desc = "Implementar un sistema de seguimiento de medallistas olímpicos usando Programación Orientada a Objetos. Deberás completar el método `agregar_medallista` de la clase `TablaPuntajes` y las funciones auxiliares de lectura de archivos."
        elif ac_id == "AC2":
            titulo_ac = "AC2: Estadísticas de Premios (NamedTuples & Dicts)"
            desc = "Procesar y calcular estadísticas históricas de ganadores de premios (Oscars, Grammys, Tonys, Emmys) usando namedtuples, diccionarios y conjuntos para responder consultas con eficiencia."
        elif ac_id == "AC3":
            titulo_ac = "AC3: Simulación Genética (Multiherencia & Mixins)"
            desc = "Construir una jerarquía de genes, rasgos y dominancia utilizando clases abstractas (ABC), herencia múltiple y llamada adecuada a super() para simular herencia biológica."
        elif ac_id == "AC4":
            titulo_ac = "AC4: Búsqueda en Tableros y Caminos"
            desc = "Modelar tableros con obstáculos y encontrar caminos válidos utilizando algoritmos de búsqueda y estructuras de datos eficientes."
        elif ac_id == "AC5":
            titulo_ac = "AC5: Simulación de Eventos y Manejo Asíncrono"
            desc = "Crear un motor de eventos concurrentes utilizando programación funcional, generadores y cola de prioridades."
        elif ac_id == "AC6":
            titulo_ac = "AC6: Cliente y Servidor de Mensajería (TCP Sockets)"
            desc = "Implementar un protocolo de comunicación en red sobre TCP/IP con codificación en bytes, intercambio de paquetes estructurados y manejo de conexiones simultáneas."
        elif ac_id == "AC7":
            titulo_ac = "AC7: Laberinto y Algoritmos Heurísticos"
            desc = "Resolver laberintos y generar estadísticas de rendimiento de búsqueda utilizando grafos, colas de prioridad y heurísticas avanzadas."
        else:
            titulo_ac = f"{ac_id}: Consultas y Serialización"
            desc = "Descarga, análisis, serialización y consultas sobre datos semiestructurados."

        actividades.append({
            "id": ac_id,
            "titulo": titulo_ac,
            "tipo": "actividad",
            "dificultad": 4 if ac_id in ["AC1", "AC2"] else 5,
            "descripcion": desc,
            "archivos": archivos_soporte,
            "codigo_inicial": archivos_soporte.get("main.py", archivos_soporte.get("entities.py", "# Desarrolla tu solución aquí\n")),
        })
    return actividades

def cargar_evaluaciones():
    return [
        {
            "id": "I1",
            "titulo": "Interrogación 1 (I1)",
            "tipo": "evaluacion",
            "dificultad": 4,
            "descripcion": "Evaluación sumativa que cubre las Semanas 1 a 4: OOP Avanzado, Manejo de Archivos, Estructuras de Datos (Listas, Tuplas, Stacks, Colas, Dicts, Sets) y Excepciones.",
            "preguntas": [
                {
                    "id": "i1-p1",
                    "titulo": "Pregunta 1: Modelamiento OOP con Clases Abstractas",
                    "descripcion": "Diseña una jerarquía de clases para un sistema de biblioteca universitaria con `Recurso` (abstracto), `Libro` y `Revista`. Debe validar disponibilidad con propiedades y excepciones personalizadas.",
                    "codigo_inicial": "from abc import ABC, abstractmethod\n\nclass Recurso(ABC):\n    def __init__(self, titulo: str, codigo: str):\n        self.titulo = titulo\n        self.codigo = codigo\n        self._prestado = False\n\n    @abstractmethod\n    def dias_prestamo(self) -> int:\n        pass\n"
                },
                {
                    "id": "i1-p2",
                    "titulo": "Pregunta 2: Estructuras de Datos y Algoritmo de Prioridad",
                    "descripcion": "Implementa una cola de atención de urgencias donde los pacientes con mayor gravedad son atendidos primero, manteniendo orden FIFO en caso de igual gravedad.",
                    "codigo_inicial": "from collections import deque\n\nclass ColaUrgencia:\n    def __init__(self):\n        self.pacientes = []\n\n    def ingresar(self, nombre: str, gravedad: int):\n        # 1: Máxima gravedad, 5: Mínima\n        pass\n\n    def atender(self) -> str:\n        pass\n"
                }
            ]
        },
        {
            "id": "I2",
            "titulo": "Interrogación 2 (I2)",
            "tipo": "evaluacion",
            "dificultad": 5,
            "descripcion": "Evaluación sumativa que cubre las Semanas 6 a 11: Iteradores y Generadores, Programación Funcional, Networking (Sockets TCP), Concurrencia (Threading) y Serialización.",
            "preguntas": [
                {
                    "id": "i2-p1",
                    "titulo": "Pregunta 1: Pipeline Funcional y Generadores",
                    "descripcion": "Diseña un pipeline usando generadores para procesar un flujo de transacciones financieras en tiempo real con consumo de memoria constante O(1).",
                    "codigo_inicial": "def filtrar_transacciones(flujo, monto_minimo):\n    for t in flujo:\n        if t['monto'] >= monto_minimo:\n            yield t\n"
                },
                {
                    "id": "i2-p2",
                    "titulo": "Pregunta 2: Concurrencia Segura con Sockets",
                    "descripcion": "Implementa un despachador de hilos con ThreadPool y Lock para atender múltiples clientes sin sobrecargar la memoria ni generar bloqueos mutuos (Deadlock).",
                    "codigo_inicial": "import threading\n\nclass DespachadorConcurrente:\n    def __init__(self, max_hilos: int = 5):\n        self.lock = threading.Lock()\n        self.activos = 0\n"
                }
            ]
        },
        {
            "id": "Examen",
            "titulo": "Examen Final",
            "tipo": "evaluacion",
            "dificultad": 5,
            "descripcion": "Evaluación integradora de todos los contenidos del semestre IIC2233.",
            "preguntas": [
                {
                    "id": "ex-p1",
                    "titulo": "Pregunta Integrativa: Arquitectura Distribuida Completa",
                    "descripcion": "Construye un sistema distribuido que integre modelo OOP, serialización binaria, comunicación por sockets TCP y análisis con grafos.",
                    "codigo_inicial": "# Sistema Integrador ClearnP.A\n"
                }
            ]
        }
    ]

def build():
    print("Compilando contenidos del curso...")
    semanas = []
    
    for cfg in SEMANAS_CONFIG:
        semana_folder = cfg["folder"]
        folder_path = os.path.join(CONTENIDOS_DIR, semana_folder)
        
        # Encontrar notebooks en este folder
        lecciones = []
        if os.path.isdir(folder_path):
            nb_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".ipynb") and not ".ipynb_checkpoints" in f])
            for nb_file in nb_files:
                bloques = parse_notebook(semana_folder, nb_file)
                # Título amigable
                clean_title = nb_file.replace(".ipynb", "").replace("-", " ").replace("_", " ").capitalize()
                clean_title = re.sub(r'^\d+\s*', '', clean_title)
                
                lecciones.append({
                    "id": nb_file.replace(".ipynb", "").replace(".", "_"),
                    "filename": nb_file,
                    "titulo": clean_title,
                    "bloques": bloques or []
                })
        
        semanas.append({
            "id": cfg["id"],
            "nombre": cfg["nombre"],
            "dificultad": cfg["dificultad"],
            "descripcion": cfg["descripcion"],
            "actividad_id": cfg["actividad_id"],
            "lecciones": lecciones,
            "ejercicios_guiados": cfg["ejercicios_guiados"]
        })
        print(f"  ✓ {cfg['nombre']}: {len(lecciones)} lecciones, {len(cfg['ejercicios_guiados'])} ejercicios guiados")
        
    actividades = cargar_actividades()
    print(f"  ✓ {len(actividades)} Actividades cargadas")
    
    evaluaciones = cargar_evaluaciones()
    print(f"  ✓ {len(evaluaciones)} Evaluaciones cargadas")

    curso_data = {
        "curso": {
            "id": "iic2233-2026-1",
            "codigo": "IIC2233",
            "nombre": "Programación Avanzada",
            "periodo": "2026-1",
            "universidad": "Pontificia Universidad Católica de Chile",
            "total_semanas": len(semanas),
            "total_actividades": len(actividades),
            "total_evaluaciones": len(evaluaciones)
        },
        "semanas": semanas,
        "actividades": actividades,
        "evaluaciones": evaluaciones
    }

    # Guardar en local clearnP.A
    output_dir = r"C:\Users\ThinkPad\OneDrive\Desktop\clearnP.A\data"
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "curso.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(curso_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado en {json_path} ({os.path.getsize(json_path) / 1024:.1f} KB)")

    # Guardar también en static/data para el frontend
    static_data_dir = r"C:\Users\ThinkPad\OneDrive\Desktop\clearnP.A\app\static\data"
    os.makedirs(static_data_dir, exist_ok=True)
    static_json_path = os.path.join(static_data_dir, "curso.json")
    with open(static_json_path, "w", encoding="utf-8") as f:
        json.dump(curso_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado en {static_json_path}")

if __name__ == "__main__":
    build()

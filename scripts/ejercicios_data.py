# -*- coding: utf-8 -*-
"""
Datos de ejercicios y actividades para ClearnP.A
Contiene 12 secciones con 7 ejercicios progresivos cada una (84 ejercicios en total)
y las 8 Actividades en formato UN SOLO ARCHIVO (Single-File).
"""

SEMANAS_DETALLADAS = [
    # ── SEMANA 1: INTRODUCCIÓN & OOP BÁSICO ──
    {
        "id": "semana-01",
        "nombre": "Semana 1: Introducción & OOP Básico",
        "folder": "semana-01-introduccion",
        "dificultad": 1,
        "descripcion": "Repaso de programación orientada a objetos en Python, atributos de instancia y clase, encapsulamiento y lectura de archivos.",
        "actividad_id": None,
        "ejercicios": [
            {
                "id": "s01-e1",
                "titulo": "1. Creando tu primera Clase: Mascota",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Definir una clase básica con constructor `__init__` y atributos de instancia.",
                "descripcion": "Crea una clase `Mascota` que reciba `nombre` (str) y `especie` (str). Debe implementar el método `presentarse()` que retorne: `'Hola, soy {nombre} y soy un {especie}.'`",
                "codigo_inicial": "class Mascota:\n    def __init__(self, nombre: str, especie: str):\n        # Inicializa los atributos\n        pass\n\n    def presentarse(self) -> str:\n        # Retorna el saludo esperado\n        pass\n",
                "tests_code": "m = Mascota('Pelusa', 'Gato')\nassert m.presentarse() == 'Hola, soy Pelusa y soy un Gato.'\nm2 = Mascota('Bobby', 'Perro')\nassert m2.presentarse() == 'Hola, soy Bobby y soy un Perro.'\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s01-e2",
                "titulo": "2. Métodos de Instancia y Cálculos: Rectángulo",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Calcular métricas de un objeto usando sus atributos internos.",
                "descripcion": "Crea una clase `Rectangulo` que reciba `ancho` y `alto`. Debe tener dos métodos: `area() -> float` y `perimetro() -> float`.",
                "codigo_inicial": "class Rectangulo:\n    def __init__(self, ancho: float, alto: float):\n        self.ancho = ancho\n        self.alto = alto\n\n    def area(self) -> float:\n        pass\n\n    def perimetro(self) -> float:\n        pass\n",
                "tests_code": "r = Rectangulo(4, 5)\nassert r.area() == 20\nassert r.perimetro() == 18\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s01-e3",
                "titulo": "3. Representación de Objetos: __str__ y __repr__",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Implementar métodos dunder para formatear objetos como texto.",
                "descripcion": "Crea una clase `Punto2D` con coordenadas `x` e `y`. Al imprimir el objeto (`__str__`) debe retornar `'(x, y)'`. La representación formal (`__repr__`) debe ser `'Punto2D(x=..., y=...)'`.",
                "codigo_inicial": "class Punto2D:\n    def __init__(self, x: float, y: float):\n        self.x = x\n        self.y = y\n\n    def __str__(self) -> str:\n        pass\n\n    def __repr__(self) -> str:\n        pass\n",
                "tests_code": "p = Punto2D(3, 7)\nassert str(p) == '(3, 7)'\nassert repr(p) == 'Punto2D(x=3, y=7)'\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s01-e4",
                "titulo": "4. Encapsulamiento con @property y @setter",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Validar modificaciones de atributos usando getters y setters con decoradores.",
                "descripcion": "Crea `CuentaBancaria(titular, saldo_inicial=0)`. El atributo `saldo` no puede ser negativo. Si se intenta asignar un valor menor a cero, debe lanzar `ValueError('Saldo no puede ser negativo')`.",
                "codigo_inicial": "class CuentaBancaria:\n    def __init__(self, titular: str, saldo_inicial: float = 0):\n        self.titular = titular\n        self._saldo = 0\n        self.saldo = saldo_inicial\n\n    @property\n    def saldo(self) -> float:\n        return self._saldo\n\n    @saldo.setter\n    def saldo(self, valor: float):\n        # Valida que valor >= 0\n        pass\n",
                "tests_code": "c = CuentaBancaria('Matías', 100)\nassert c.saldo == 100\nc.saldo = 250\nassert c.saldo == 250\ntry:\n    c.saldo = -5\n    assert False, 'Debió lanzar ValueError'\nexcept ValueError:\n    pass\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s01-e5",
                "titulo": "5. Atributos de Clase y Conteo Global",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Diferenciar entre atributos compartidos por la clase y atributos propios de cada instancia.",
                "descripcion": "Crea una clase `Usuario` con atributo de clase `total_usuarios = 0`. Cada vez que se instancie un `Usuario(username)`, `total_usuarios` debe incrementarse en 1. Además, cada usuario debe tener un atributo `id` autoincremental igual al valor de `total_usuarios` al momento de crearse.",
                "codigo_inicial": "class Usuario:\n    total_usuarios = 0\n\n    def __init__(self, username: str):\n        # Incrementa el contador de clase y asigna self.id\n        pass\n",
                "tests_code": "Usuario.total_usuarios = 0\nu1 = Usuario('ana')\nu2 = Usuario('carlos')\nassert u1.id == 1\nassert u2.id == 2\nassert Usuario.total_usuarios == 2\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s01-e6",
                "titulo": "6. Lectura y Procesamiento de Archivo CSV",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Parsear líneas de texto simulando la carga de datos del curso.",
                "descripcion": "Escribe una función `procesar_alumnos(texto_csv: str) -> dict[str, float]` que reciba un texto con formato `'nombre,nota'` (una por línea) y retorne un diccionario con los nombres como clave y las notas como float. Ignora líneas vacías.",
                "codigo_inicial": "def procesar_alumnos(texto_csv: str) -> dict[str, float]:\n    # Divide por saltos de línea y parsea cada par\n    pass\n",
                "tests_code": "data = 'Lucas,6.5\\nSofia,7.0\\nPedro,5.2'\nres = procesar_alumnos(data)\nassert res == {'Lucas': 6.5, 'Sofia': 7.0, 'Pedro': 5.2}\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s01-e7",
                "titulo": "7. Reto Integrador: Curso y Promedios",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Integrar clases, colecciones y validación en un modelo completo.",
                "descripcion": "Crea `Estudiante(nombre)` con lista interna de notas. Implementa `agregar_nota(nota: float)` (valida 1.0 <= nota <= 7.0, sino lanza `ValueError`), y `promedio() -> float` (retorna 0.0 si no tiene notas). Luego crea `Curso(nombre)` con método `agregar_estudiante(e: Estudiante)` y `mejor_estudiante() -> str` que retorna el nombre del estudiante con mayor promedio.",
                "codigo_inicial": "class Estudiante:\n    def __init__(self, nombre: str):\n        self.nombre = nombre\n        self.notas = []\n\n    def agregar_nota(self, nota: float):\n        pass\n\n    def promedio(self) -> float:\n        pass\n\nclass Curso:\n    def __init__(self, nombre: str):\n        self.nombre = nombre\n        self.estudiantes = []\n\n    def agregar_estudiante(self, estudiante: Estudiante):\n        self.estudiantes.append(estudiante)\n\n    def mejor_estudiante(self) -> str:\n        pass\n",
                "tests_code": "e1 = Estudiante('Valeria')\ne1.agregar_nota(6.5)\ne1.agregar_nota(7.0)\ne2 = Estudiante('Diego')\ne2.agregar_nota(5.0)\ne2.agregar_nota(5.5)\nc = Curso('Programación Avanzada')\nc.agregar_estudiante(e1)\nc.agregar_estudiante(e2)\nassert round(e1.promedio(), 2) == 6.75\nassert c.mejor_estudiante() == 'Valeria'\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 2: MODULARIZACIÓN & ENTORNO ──
    {
        "id": "semana-02",
        "nombre": "Semana 2: Modularización & Entorno",
        "folder": "semana-02-entorno_de_trabajo",
        "dificultad": 1,
        "descripcion": "Manejo de rutas de archivos con os y pathlib, modularización, separación en módulos y buenas prácticas PEP 8.",
        "actividad_id": None,
        "ejercicios": [
            {
                "id": "s02-e1",
                "titulo": "1. Limpieza y Normalización de Nombres de Archivo",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Manipular strings para formatear nombres de archivo seguros.",
                "descripcion": "Escribe `limpiar_nombre(archivo: str) -> str` que elimine espacios a los lados, convierta espacios internos en guiones bajos `_`, y lo pase a minúsculas.",
                "codigo_inicial": "def limpiar_nombre(archivo: str) -> str:\n    pass\n",
                "tests_code": "assert limpiar_nombre('  Documento Final 2026.pdf  ') == 'documento_final_2026.pdf'\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s02-e2",
                "titulo": "2. Extracción de Extensión con os.path",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Usar funciones del módulo estándar `os.path`.",
                "descripcion": "Implementa `obtener_extension(ruta: str) -> str` que retorne solo la extensión del archivo en minúsculas y sin el punto inicial (ej. `'pdf'`, `'py'`, `'csv'`). Si no tiene extensión, retorna `''`.",
                "codigo_inicial": "import os\n\ndef obtener_extension(ruta: str) -> str:\n    pass\n",
                "tests_code": "assert obtener_extension('datos/resultados.DCC') == 'dcc'\nassert obtener_extension('main.py') == 'py'\nassert obtener_extension('README') == ''\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s02-e3",
                "titulo": "3. Unir Rutas Multiplataforma con os.path.join",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Construir rutas compatibles entre Windows, Linux y Mac.",
                "descripcion": "Crea una función `construir_ruta(carpeta_base: str, subcarpeta: str, archivo: str) -> str` que use `os.path.join` y normalice los separadores.",
                "codigo_inicial": "import os\n\ndef construir_ruta(carpeta_base: str, subcarpeta: str, archivo: str) -> str:\n    return os.path.join(carpeta_base, subcarpeta, archivo)\n",
                "tests_code": "r = construir_ruta('app', 'static', 'style.css')\nassert 'app' in r and 'style.css' in r\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s02-e4",
                "titulo": "4. Manejo Moderno de Rutas con pathlib",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Utilizar la clase `Path` de `pathlib` para inspeccionar archivos.",
                "descripcion": "Escribe `analizar_ruta(ruta_str: str) -> dict` que retorne un diccionario con: `'nombre'` (el nombre del archivo con extensión), `'stem'` (el nombre sin extensión) y `'sufijo'` (la extensión con punto, ej. `'.txt'`).",
                "codigo_inicial": "from pathlib import Path\n\ndef analizar_ruta(ruta_str: str) -> dict:\n    p = Path(ruta_str)\n    return {\n        'nombre': p.name,\n        'stem': p.stem,\n        'sufijo': p.suffix\n    }\n",
                "tests_code": "d = analizar_ruta('reportes/marzo/balance_2026.xlsx')\nassert d['nombre'] == 'balance_2026.xlsx'\nassert d['stem'] == 'balance_2026'\nassert d['sufijo'] == '.xlsx'\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s02-e5",
                "titulo": "5. Filtro de Archivos por Extensión",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Filtrar y clasificar listas de archivos.",
                "descripcion": "Escribe `filtrar_archivos_python(lista_archivos: list[str]) -> list[str]` que reciba una lista de rutas de archivo y retorne solo aquellas que terminen en `.py`, ignorando mayúsculas/minúsculas.",
                "codigo_inicial": "def filtrar_archivos_python(lista_archivos: list[str]) -> list[str]:\n    pass\n",
                "tests_code": "archivos = ['main.py', 'TEST.PY', 'datos.csv', 'utils.py', 'notas.txt']\nassert filtrar_archivos_python(archivos) == ['main.py', 'TEST.PY', 'utils.py']\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s02-e6",
                "titulo": "6. Simulación de Buscador de Módulos (Sys.path)",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Entender cómo Python busca e importa módulos.",
                "descripcion": "Implementa `buscar_modulo(nombre_modulo: str, rutas_busqueda: list[str]) -> str | None` que recorra las carpetas en `rutas_busqueda` y retorne la primera ruta completa donde se encontraría `{nombre_modulo}.py`.",
                "codigo_inicial": "import os\n\ndef buscar_modulo(nombre_modulo: str, rutas_busqueda: list[str]) -> str:\n    for ruta in rutas_busqueda:\n        candidato = os.path.join(ruta, f'{nombre_modulo}.py')\n        return candidato # Completa con la lógica de verificación\n",
                "tests_code": "rutas = ['src', 'lib', 'core']\n# Si buscamos 'entities', en 'src' debe dar 'src/entities.py' o 'src\\entities.py'\nr = os.path.join('src', 'entities.py')\nprint('✅ Ejercicio 6 completado conceptualmente!')\n"
            },
            {
                "id": "s02-e7",
                "titulo": "7. Reto Integrador: Clasificador de Archivos de Proyecto",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Organizar un árbol de archivos en categorías semánticas.",
                "descripcion": "Escribe `clasificar_archivos(rutas: list[str]) -> dict[str, list[str]]` que clasifique los archivos en 3 categorías: `'codigo'` (.py), `'datos'` (.csv, .json, .dcc) y `'documentos'` (.pdf, .md, .txt). Retorna las listas ordenadas alfabéticamente.",
                "codigo_inicial": "def clasificar_archivos(rutas: list[str]) -> dict[str, list[str]]:\n    categorias = {'codigo': [], 'datos': [], 'documentos': []}\n    # Completa la clasificación según la extensión\n    return categorias\n",
                "tests_code": "archivos = ['main.py', 'enunciado.pdf', 'results.dcc', 'entities.py', 'data.json', 'README.md']\nres = clasificar_archivos(archivos)\nassert 'main.py' in res['codigo'] and 'entities.py' in res['codigo']\nassert 'results.dcc' in res['datos'] and 'data.json' in res['datos']\nassert 'enunciado.pdf' in res['documentos']\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 3: ESTRUCTURAS DE DATOS ──
    {
        "id": "semana-03",
        "nombre": "Semana 3: Estructuras de Datos",
        "folder": "semana-03-estructuras_de_datos",
        "dificultad": 2,
        "descripcion": "Tuplas, namedtuples, pilas (Stack LIFO), colas (FIFO), diccionarios, sets y empaquetamiento con *args y **kwargs.",
        "actividad_id": "AC2",
        "ejercicios": [
            {
                "id": "s03-e1",
                "titulo": "1. Desempaquetado de Tuplas y Coordenadas",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Manejar tuplas inmutables y desempaquetado de variables.",
                "descripcion": "Escribe `calcular_distancia_origen(punto: tuple[float, float]) -> float` que reciba una tupla `(x, y)` y retorne `sqrt(x² + y²)`.",
                "codigo_inicial": "import math\n\ndef calcular_distancia_origen(punto: tuple[float, float]) -> float:\n    x, y = punto\n    return math.sqrt(x**2 + y**2)\n",
                "tests_code": "assert calcular_distancia_origen((3, 4)) == 5.0\nassert calcular_distancia_origen((0, 0)) == 0.0\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s03-e2",
                "titulo": "2. Registros Inmutables con NamedTuples",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Crear y manipular `collections.namedtuple` para representar entidades.",
                "descripcion": "Crea una `namedtuple` llamada `Medalla` con campos `'pais'`, `'deporte'` y `'tipo'` ('Oro', 'Plata' o 'Bronce'). Escribe `es_oro(m: Medalla) -> bool` que retorne True si la medalla es de Oro.",
                "codigo_inicial": "from collections import namedtuple\n\n# Define Medalla aquí\nMedalla = namedtuple('Medalla', ['pais', 'deporte', 'tipo'])\n\ndef es_oro(m: Medalla) -> bool:\n    return m.tipo == 'Oro'\n",
                "tests_code": "m1 = Medalla('Chile', 'Tiro con Arco', 'Oro')\nm2 = Medalla('Argentina', 'Fútbol', 'Plata')\nassert es_oro(m1) == True\nassert es_oro(m2) == False\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s03-e3",
                "titulo": "3. Pila (Stack LIFO): Inversor de Textos",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Utilizar las operaciones `append` (push) y `pop` de una lista como pila LIFO.",
                "descripcion": "Implementa `invertir_cadena(texto: str) -> str` utilizando obligatoriamente una pila (`stack = []`).",
                "codigo_inicial": "def invertir_cadena(texto: str) -> str:\n    stack = []\n    for char in texto:\n        stack.append(char)\n    # Desapila para armar el texto invertido\n    invertido = ''\n    while stack:\n        invertido += stack.pop()\n    return invertido\n",
                "tests_code": "assert invertir_cadena('Python') == 'nohtyP'\nassert invertir_cadena('reconocer') == 'reconocer'\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s03-e4",
                "titulo": "4. Verificador de Paréntesis Balanceados con Pila",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Algoritmo clásico de validación de sintaxis usando Stack.",
                "descripcion": "Escribe `es_balanceado(cadena: str) -> bool` que verifique si los delimitadores `()`, `[]` y `{}` están correctamente emparejados.",
                "codigo_inicial": "def es_balanceado(cadena: str) -> bool:\n    stack = []\n    pares = {')': '(', ']': '[', '}': '{'}\n    for c in cadena:\n        if c in '([{':\n            stack.append(c)\n        elif c in ')]}':\n            if not stack or stack.pop() != pares[c]:\n                return False\n    return len(stack) == 0\n",
                "tests_code": "assert es_balanceado('({[]})') == True\nassert es_balanceado('([)]') == False\nassert es_balanceado('(((') == False\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s03-e5",
                "titulo": "5. Cola (Queue FIFO) con collections.deque",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Utilizar `deque` con `append` y `popleft` para simular atención de clientes.",
                "descripcion": "Crea una clase `FilaAtencion` con métodos: `llegar(nombre: str)` (agrega al final) y `atender() -> str | None` (atiende y retorna al primero de la fila; si está vacía retorna None).",
                "codigo_inicial": "from collections import deque\n\nclass FilaAtencion:\n    def __init__(self):\n        self.cola = deque()\n\n    def llegar(self, nombre: str):\n        pass\n\n    def atender(self) -> str:\n        pass\n",
                "tests_code": "f = FilaAtencion()\nf.llegar('Pedro')\nf.llegar('Lucía')\nassert f.atender() == 'Pedro'\nassert f.atender() == 'Lucía'\nassert f.atender() is None\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s03-e6",
                "titulo": "6. Conteo y Agrupación con defaultdict",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Evitar `KeyError` agrupando elementos eficientemente.",
                "descripcion": "Escribe `agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]` usando `defaultdict(list)` para agrupar palabras según su cantidad de letras.",
                "codigo_inicial": "from collections import defaultdict\n\ndef agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:\n    agrupados = defaultdict(list)\n    # Itera y agrupa\n    return dict(agrupados)\n",
                "tests_code": "p = ['sol', 'mar', 'cielo', 'luna', 'estrella']\nres = agrupar_por_longitud(p)\nassert set(res[3]) == {'sol', 'mar'}\nassert res[5] == ['cielo']\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s03-e7",
                "titulo": "7. Reto Integrador: Amigos en Común con Sets",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Operaciones de conjuntos (unión, intersección, diferencia simétrica).",
                "descripcion": "Implementa una clase `RedSocial` con `agregar_amigo(u1, u2)` y `amigos_en_comun(u1, u2) -> set[str]`. Luego añade `sugerir_amigos(u: str) -> set[str]` que retorne los amigos de sus amigos que NO sean ya sus amigos ni él mismo.",
                "codigo_inicial": "from collections import defaultdict\n\nclass RedSocial:\n    def __init__(self):\n        self.grafo = defaultdict(set)\n\n    def agregar_amigo(self, u1: str, u2: str):\n        self.grafo[u1].add(u2)\n        self.grafo[u2].add(u1)\n\n    def amigos_en_comun(self, u1: str, u2: str) -> set[str]:\n        return self.grafo[u1] & self.grafo[u2]\n\n    def sugerir_amigos(self, u: str) -> set[str]:\n        sugerencias = set()\n        for amigo in self.grafo[u]:\n            sugerencias |= self.grafo[amigo]\n        return sugerencias - self.grafo[u] - {u}\n",
                "tests_code": "rs = RedSocial()\nrs.agregar_amigo('Ana', 'Beto')\nrs.agregar_amigo('Ana', 'Carlos')\nrs.agregar_amigo('Beto', 'Daniel')\nassert rs.amigos_en_comun('Ana', 'Daniel') == set()\nassert rs.sugerir_amigos('Ana') == {'Daniel'}\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 4: OOP AVANZADO & PATRONES ──
    {
        "id": "semana-04",
        "nombre": "Semana 4: OOP Avanzado & Patrones",
        "folder": "semana-04-oop_avanzado",
        "dificultad": 3,
        "descripcion": "Herencia simple, super(), polimorfismo, clases abstractas (ABC), multiherencia, MRO y decoradores.",
        "actividad_id": "AC1",
        "ejercicios": [
            {
                "id": "s04-e1",
                "titulo": "1. Herencia Simple y super()",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Reutilizar atributos del constructor de la clase padre.",
                "descripcion": "Crea `Persona(nombre, rut)` y luego `Estudiante(nombre, rut, carrera)` que herede de `Persona` usando `super().__init__(nombre, rut)`.",
                "codigo_inicial": "class Persona:\n    def __init__(self, nombre: str, rut: str):\n        self.nombre = nombre\n        self.rut = rut\n\nclass Estudiante(Persona):\n    def __init__(self, nombre: str, rut: str, carrera: str):\n        # Llama a super y asigna carrera\n        pass\n",
                "tests_code": "e = Estudiante('Catalina', '20123456-7', 'Ingeniería')\nassert e.nombre == 'Catalina' and e.carrera == 'Ingeniería'\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s04-e2",
                "titulo": "2. Polimorfismo y Sobreescritura",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Hacer que diferentes clases respondan al mismo método con comportamientos distintos.",
                "descripcion": "Crea una clase base `Notificacion` con método `enviar(msg)` que retorne `'Enviando: ' + msg`. Sobreescribe en `Email(Notificacion)` para retornar `'Email: ' + msg` y en `SMS(Notificacion)` para retornar `'SMS: ' + msg`.",
                "codigo_inicial": "class Notificacion:\n    def enviar(self, msg: str) -> str:\n        return f'Enviando: {msg}'\n\nclass Email(Notificacion):\n    pass\n\nclass SMS(Notificacion):\n    pass\n",
                "tests_code": "assert Email().enviar('Hola') == 'Email: Hola'\nassert SMS().enviar('Hola') == 'SMS: Hola'\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s04-e3",
                "titulo": "3. Clases Abstractas con ABC",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Obligar a las subclases a implementar métodos obligatorios.",
                "descripcion": "Crea `Figura(ABC)` con `@abstractmethod def area(self) -> float: pass`. Luego implementa `Cuadrado(lado: float)` con el cálculo de su área.",
                "codigo_inicial": "from abc import ABC, abstractmethod\n\nclass Figura(ABC):\n    @abstractmethod\n    def area(self) -> float:\n        pass\n\nclass Cuadrado(Figura):\n    def __init__(self, lado: float):\n        self.lado = lado\n    def area(self) -> float:\n        return self.lado ** 2\n",
                "tests_code": "c = Cuadrado(5)\nassert c.area() == 25\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s04-e4",
                "titulo": "4. Multiherencia y MRO (Method Resolution Order)",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Comprender el orden en que Python busca métodos en herencia múltiple.",
                "descripcion": "Crea `Nadador` con método `desplazarse() -> 'Nadando'`, `Volador` con `desplazarse() -> 'Volando'` y `Pato(Volador, Nadador)`. Verifica que el MRO priorice el primer padre listado.",
                "codigo_inicial": "class Nadador:\n    def desplazarse(self) -> str:\n        return 'Nadando'\n\nclass Volador:\n    def desplazarse(self) -> str:\n        return 'Volando'\n\nclass Pato(Volador, Nadador):\n    pass\n",
                "tests_code": "p = Pato()\nassert p.desplazarse() == 'Volando'\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s04-e5",
                "titulo": "5. Mixins de Funcionalidad",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Crear clases que agregan capacidades reutilizables sin jerarquía rígida.",
                "descripcion": "Crea un mixin `LoggeableMixin` que tenga un método `log(self, mensaje: str) -> str` retornando `f'[{self.__class__.__name__}] {mensaje}'`. Úsalo en una clase `Servicio(LoggeableMixin)`.",
                "codigo_inicial": "class LoggeableMixin:\n    def log(self, mensaje: str) -> str:\n        return f'[{self.__class__.__name__}] {mensaje}'\n\nclass Servicio(LoggeableMixin):\n    pass\n",
                "tests_code": "s = Servicio()\nassert s.log('Inicio de proceso') == '[Servicio] Inicio de proceso'\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s04-e6",
                "titulo": "6. Decorador de Funciones: Temporizador y Wrapper",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Envolver funciones para añadir comportamiento previo o posterior.",
                "descripcion": "Crea un decorador `@en_mayusculas` que tome una función que retorna un string y transforme el resultado a mayúsculas.",
                "codigo_inicial": "import functools\n\ndef en_mayusculas(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        resultado = func(*args, **kwargs)\n        return str(resultado).upper()\n    return wrapper\n\n@en_mayusculas\ndef saludar(nombre: str) -> str:\n    return f'hola, {nombre}'\n",
                "tests_code": "assert saludar('ignacio') == 'HOLA, IGNACIO'\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s04-e7",
                "titulo": "7. Reto Integrador: Jerarquía de Vehículos con Mixin",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Integrar clases abstractas, herencia múltiple y validaciones.",
                "descripcion": "Crea una clase abstracta `Vehiculo(ABC)` con atributo `velocidad` y método abstracto `acelerar(delta)`. Crea el mixin `CombustibleMixin` con `cargar_combustible(litros)`. Implementa `Auto(Vehiculo, CombustibleMixin)` que acelere aumentando la velocidad y disminuya 0.1L de combustible por unidad de velocidad incrementada.",
                "codigo_inicial": "from abc import ABC, abstractmethod\n\nclass CombustibleMixin:\n    def __init__(self, **kwargs):\n        super().__init__(**kwargs)\n        self.combustible = 50.0\n\n    def cargar_combustible(self, litros: float):\n        self.combustible += litros\n\nclass Vehiculo(ABC):\n    def __init__(self, velocidad: float = 0.0, **kwargs):\n        super().__init__(**kwargs)\n        self.velocidad = velocidad\n\n    @abstractmethod\n    def acelerar(self, delta: float):\n        pass\n\nclass Auto(CombustibleMixin, Vehiculo):\n    def acelerar(self, delta: float):\n        self.velocidad += delta\n        self.combustible -= delta * 0.1\n",
                "tests_code": "a = Auto(velocidad=10.0)\na.acelerar(20)\nassert a.velocidad == 30.0\nassert a.combustible == 48.0\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 5/6: EXCEPCIONES E ITERADORES ──
    {
        "id": "semana-06",
        "nombre": "Semana 6: Excepciones e Iteradores",
        "folder": "semana-06-excepciones_iterables_e_iteradores",
        "dificultad": 3,
        "descripcion": "Manejo de excepciones (try, except, else, finally), errores personalizados, protocolo iterable (__iter__, __next__), generadores con yield y listas ligadas.",
        "actividad_id": "AC3",
        "ejercicios": [
            {
                "id": "s06-e1",
                "titulo": "1. Manejo Seguro con Try / Except",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Evitar caídas de programa por división por cero o tipos incompatibles.",
                "descripcion": "Escribe `division_segura(a, b) -> float | None` que intente dividir `a / b`. Si ocurre `ZeroDivisionError` o `TypeError`, retorna `None` sin romper el flujo.",
                "codigo_inicial": "def division_segura(a, b):\n    try:\n        return a / b\n    except (ZeroDivisionError, TypeError):\n        return None\n",
                "tests_code": "assert division_segura(10, 2) == 5.0\nassert division_segura(10, 0) is None\nassert division_segura('10', 2) is None\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s06-e2",
                "titulo": "2. Creación de Excepciones Propias",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Heredar de `Exception` para crear errores semánticos en el dominio del problema.",
                "descripcion": "Crea una excepción `ProductoAgotadoError(Exception)`. Escribe una función `vender_producto(stock: int, cantidad: int) -> int` que retorne el nuevo stock o lance `ProductoAgotadoError('No hay stock suficiente')` si `cantidad > stock`.",
                "codigo_inicial": "class ProductoAgotadoError(Exception):\n    pass\n\ndef vender_producto(stock: int, cantidad: int) -> int:\n    if cantidad > stock:\n        raise ProductoAgotadoError('No hay stock suficiente')\n    return stock - cantidad\n",
                "tests_code": "assert vender_producto(10, 3) == 7\ntry:\n    vender_producto(5, 6)\n    assert False, 'Debio lanzar ProductoAgotadoError'\nexcept ProductoAgotadoError:\n    pass\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s06-e3",
                "titulo": "3. Cláusulas Else y Finally",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Comprender cuándo se ejecuta `else` y cuándo `finally`.",
                "descripcion": "Escribe `procesar_transaccion(saldo: float, monto: float) -> tuple[bool, str]` que intente descontar `monto`. Si `saldo < monto`, lanza `ValueError`. Usa `else` para registrar `'Exito'` y `finally` para retornar el estado.",
                "codigo_inicial": "def procesar_transaccion(saldo: float, monto: float) -> tuple[bool, str]:\n    try:\n        if saldo < monto:\n            raise ValueError('Saldo insuficiente')\n    except ValueError as e:\n        return (False, str(e))\n    else:\n        return (True, 'Transacción completada')\n",
                "tests_code": "assert procesar_transaccion(100, 50) == (True, 'Transacción completada')\nassert procesar_transaccion(20, 50)[0] == False\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s06-e4",
                "titulo": "4. Protocolo de Iteración: Contador Personalizado",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Implementar `__iter__` y `__next__` con `StopIteration`.",
                "descripcion": "Crea una clase `RangoDescendente(inicio, fin)` que itere desde `inicio` hasta `fin` de 1 en 1 hacia abajo.",
                "codigo_inicial": "class RangoDescendente:\n    def __init__(self, inicio: int, fin: int):\n        self.actual = inicio\n        self.fin = fin\n\n    def __iter__(self):\n        return self\n\n    def __next__(self) -> int:\n        if self.actual < self.fin:\n            raise StopIteration\n        val = self.actual\n        self.actual -= 1\n        return val\n",
                "tests_code": "valores = list(RangoDescendente(5, 2))\nassert valores == [5, 4, 3, 2]\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s06-e5",
                "titulo": "5. Funciones Generadoras con yield: Fibonacci",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Producir secuencias con evaluación perezosa (lazy evaluation) en O(1) de memoria.",
                "descripcion": "Escribe una función generadora `fibonacci(n: int)` que produzca con `yield` los primeros `n` números de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5...).",
                "codigo_inicial": "def fibonacci(n: int):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n",
                "tests_code": "assert list(fibonacci(6)) == [0, 1, 1, 2, 3, 5]\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s06-e6",
                "titulo": "6. Generador con Filtro en Memoria Constante",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Encadenar generadores para procesar grandes flujos sin cargar listas completas en RAM.",
                "descripcion": "Crea una función generadora `filtrar_multiplos(generador, divisor: int)` que reciba cualquier generador de enteros y solo produzca con `yield` aquellos que sean divisibles por `divisor`.",
                "codigo_inicial": "def filtrar_multiplos(generador, divisor: int):\n    for numero in generador:\n        if numero % divisor == 0:\n            yield numero\n",
                "tests_code": "gen = (x for x in range(1, 15))\nassert list(filtrar_multiplos(gen, 3)) == [3, 6, 9, 12]\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s06-e7",
                "titulo": "7. Reto Integrador: Lista Ligada Iterable",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Construir una estructura de datos clásica con soporte completo de iteración.",
                "descripcion": "Implementa `Nodo(valor, siguiente=None)` y `ListaLigada()` con métodos `agregar(valor)` (al final) y soporte para `for elemento in lista:` usando un generador en `__iter__`.",
                "codigo_inicial": "class Nodo:\n    def __init__(self, valor, siguiente=None):\n        self.valor = valor\n        self.siguiente = siguiente\n\nclass ListaLigada:\n    def __init__(self):\n        self.cabeza = None\n\n    def agregar(self, valor):\n        if not self.cabeza:\n            self.cabeza = Nodo(valor)\n            return\n        actual = self.cabeza\n        while actual.siguiente:\n            actual = actual.siguiente\n        actual.siguiente = Nodo(valor)\n\n    def __iter__(self):\n        actual = self.cabeza\n        while actual:\n            yield actual.valor\n            actual = actual.siguiente\n",
                "tests_code": "ll = ListaLigada()\nll.agregar(10)\nll.agregar(20)\nll.agregar(30)\nassert list(ll) == [10, 20, 30]\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 7: PROGRAMACIÓN FUNCIONAL ──
    {
        "id": "semana-07",
        "nombre": "Semana 7: Programación Funcional",
        "folder": "semana-07-programacion_funcional",
        "dificultad": 4,
        "descripcion": "Funciones puras, inmutabilidad, funciones anónimas lambda, map, filter, functools.reduce y comprensiones avanzadas.",
        "actividad_id": "AC4",
        "ejercicios": [
            {
                "id": "s07-e1",
                "titulo": "1. Funciones Lambda y Ordenamiento",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Usar funciones anónimas en una sola línea para transformar o comparar.",
                "descripcion": "Dada una lista de tuplas `(nombre, edad)`, usa `sorted(..., key=lambda ...)` para ordenar a las personas de menor a mayor edad.",
                "codigo_inicial": "def ordenar_por_edad(personas: list[tuple[str, int]]) -> list[tuple[str, int]]:\n    return sorted(personas, key=lambda p: p[1])\n",
                "tests_code": "data = [('Javier', 25), ('Camila', 19), ('Tomas', 22)]\nassert ordenar_por_edad(data) == [('Camila', 19), ('Tomas', 22), ('Javier', 25)]\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s07-e2",
                "titulo": "2. Transformación con map()",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Aplicar una transformación a todos los elementos sin bucle `for`.",
                "descripcion": "Escribe `convertir_celsius_a_fahrenheit(temperaturas: list[float]) -> list[float]` usando `map` y lambda con la fórmula `(C * 9/5) + 32`.",
                "codigo_inicial": "def convertir_celsius_a_fahrenheit(temperaturas: list[float]) -> list[float]:\n    return list(map(lambda c: (c * 9/5) + 32, temperaturas))\n",
                "tests_code": "assert convertir_celsius_a_fahrenheit([0, 100]) == [32.0, 212.0]\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s07-e3",
                "titulo": "3. Filtrado Condicional con filter()",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Seleccionar elementos que cumplen un predicado booleano.",
                "descripcion": "Implementa `filtrar_aprobados(calificaciones: dict[str, float], nota_minima: float = 4.0) -> list[str]` usando `filter` para retornar los nombres de los alumnos aprobados.",
                "codigo_inicial": "def filtrar_aprobados(calificaciones: dict[str, float], nota_minima: float = 4.0) -> list[str]:\n    return list(filter(lambda alumno: calificaciones[alumno] >= nota_minima, calificaciones))\n",
                "tests_code": "notas = {'Andres': 3.8, 'Sofia': 6.2, 'Mateo': 4.0, 'Loreto': 5.5}\nassert set(filtrar_aprobados(notas)) == {'Sofia', 'Mateo', 'Loreto'}\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s07-e4",
                "titulo": "4. Reducción con functools.reduce",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Colapsar una secuencia en un único valor acumulado.",
                "descripcion": "Escribe `producto_total(numeros: list[int]) -> int` usando `reduce` para calcular la multiplicación de todos los elementos. Si está vacía retorna 1.",
                "codigo_inicial": "from functools import reduce\n\ndef producto_total(numeros: list[int]) -> int:\n    if not numeros:\n        return 1\n    return reduce(lambda acumulado, actual: acumulado * actual, numeros)\n",
                "tests_code": "assert producto_total([2, 3, 4]) == 24\nassert producto_total([]) == 1\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s07-e5",
                "titulo": "5. Comprensiones de Diccionarios y Cuadrados",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Crear diccionarios mapeados en una sola expresión.",
                "descripcion": "Escribe `mapa_de_cuadrados(numeros: list[int]) -> dict[int, int]` que asocie cada número par con su valor elevado al cuadrado usando dict comprehension.",
                "codigo_inicial": "def mapa_de_cuadrados(numeros: list[int]) -> dict[int, int]:\n    return {n: n**2 for n in numeros if n % 2 == 0}\n",
                "tests_code": "assert mapa_de_cuadrados([1, 2, 3, 4]) == {2: 4, 4: 16}\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s07-e6",
                "titulo": "6. Currificación y Clausuras (Closures)",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Construir funciones generadoras de funciones con ámbito léxico.",
                "descripcion": "Escribe una función `crear_multiplicador(factor: float)` que retorne una nueva función `multiplicar(x: float)` que multiplique su argumento por `factor`.",
                "codigo_inicial": "def crear_multiplicador(factor: float):\n    def multiplicar(x: float) -> float:\n        return x * factor\n    return multiplicar\n",
                "tests_code": "duplicar = crear_multiplicador(2)\ntriplicar = crear_multiplicador(3)\nassert duplicar(10) == 20\nassert triplicar(10) == 30\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s07-e7",
                "titulo": "7. Reto Integrador: Pipeline de Análisis de Ventas",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Diseñar un pipeline de datos que encadene transformaciones funcionales.",
                "descripcion": "Dada una lista de ventas `{'producto': str, 'precio': float, 'unidades': int, 'categoria': str}`, escribe `resumen_ventas_categoria(ventas: list[dict], categoria: str) -> float` que filtre por esa categoría, calcule el ingreso de cada venta (`precio * unidades`) y reduzca con `reduce` para retornar el ingreso total.",
                "codigo_inicial": "from functools import reduce\n\ndef resumen_ventas_categoria(ventas: list[dict], categoria: str) -> float:\n    # Filtra por categoría\n    # Mapea a ingreso total de cada venta\n    # Reduce a la suma total\n    pass\n",
                "tests_code": "v = [\n    {'producto': 'Mouse', 'precio': 15.0, 'unidades': 2, 'categoria': 'Tecnologia'},\n    {'producto': 'Silla', 'precio': 80.0, 'unidades': 1, 'categoria': 'Hogar'},\n    {'producto': 'Teclado', 'precio': 30.0, 'unidades': 3, 'categoria': 'Tecnologia'},\n]\n# Tecnologia: 15*2 + 30*3 = 30 + 90 = 120.0\n# Completa la función para que pase el test\ndef sol(ventas, cat):\n    fil = filter(lambda x: x['categoria'] == cat, ventas)\n    montos = map(lambda x: x['precio'] * x['unidades'], fil)\n    return sum(montos)\nassert sol(v, 'Tecnologia') == 120.0\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 8: CONCURRENCIA Y THREADS (DEDICADA) ──
    {
        "id": "semana-08-threading",
        "nombre": "Semana 8: Concurrencia y Threads",
        "folder": "semana-09-threading",
        "dificultad": 4,
        "descripcion": "Programación concurrente en Python con threading: creación de hilos, join, demonios, race conditions, sincronización con Lock, eventos y prevención de deadlocks.",
        "actividad_id": "AC5",
        "ejercicios": [
            {
                "id": "s08-e1",
                "titulo": "1. Creación e Inicio de un Thread",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Instanciar un `threading.Thread` pasando una función objetivo con `target` y argumentos.",
                "descripcion": "Escribe `ejecutar_en_paralelo(funcion, argumentos: tuple)` que cree un hilo con la función dada, lo inicie con `.start()`, espere su término con `.join()` y retorne el hilo creado.",
                "codigo_inicial": "import threading\n\ndef ejecutar_en_paralelo(funcion, argumentos: tuple) -> threading.Thread:\n    t = threading.Thread(target=funcion, args=argumentos)\n    t.start()\n    t.join()\n    return t\n",
                "tests_code": "salida = []\ndef tarea(x):\n    salida.append(x * 2)\nt = ejecutar_en_paralelo(tarea, (21,))\nassert salida == [42]\nassert not t.is_alive()\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s08-e2",
                "titulo": "2. Hilo Personalizado Heredando de Thread",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Crear hilos mediante herencia sobreescribiendo el método `run()`.",
                "descripcion": "Implementa la clase `DescargadorSimulado(threading.Thread)` que reciba `url: str`. Debe tener un atributo `completado = False` que cambie a `True` cuando termine de ejecutarse en `run()`.",
                "codigo_inicial": "import threading\n\nclass DescargadorSimulado(threading.Thread):\n    def __init__(self, url: str):\n        super().__init__()\n        self.url = url\n        self.completado = False\n\n    def run(self):\n        # Simula la tarea y marca completado = True\n        self.completado = True\n",
                "tests_code": "d = DescargadorSimulado('https://clearn.cl/api')\nd.start()\nd.join()\nassert d.completado == True\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s08-e3",
                "titulo": "3. Hilos Demonio (Daemon Threads)",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Configurar hilos de soporte secundario que no bloquean la salida del programa.",
                "descripcion": "Escribe `crear_demonio(funcion_fondo) -> threading.Thread` que instancie un hilo con `daemon=True` y verifique que `t.daemon` sea verdadero.",
                "codigo_inicial": "import threading\n\ndef crear_demonio(funcion_fondo) -> threading.Thread:\n    t = threading.Thread(target=funcion_fondo, daemon=True)\n    return t\n",
                "tests_code": "t = crear_demonio(lambda: None)\nassert t.daemon == True\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s08-e4",
                "titulo": "4. Carrera Crítica (Race Condition) y Bloqueo con Lock",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Proteger secciones críticas de código concurrente usando `threading.Lock`.",
                "descripcion": "Crea una clase `ContadorConcurrente` con atributo `valor = 0` y un `self.lock = threading.Lock()`. El método `incrementar()` debe estar protegido con `with self.lock:` para evitar que múltiples hilos corrompan el conteo.",
                "codigo_inicial": "import threading\n\nclass ContadorConcurrente:\n    def __init__(self):\n        self.valor = 0\n        self.lock = threading.Lock()\n\n    def incrementar(self):\n        with self.lock:\n            self.valor += 1\n",
                "tests_code": "c = ContadorConcurrente()\nhilos = [threading.Thread(target=lambda: [c.incrementar() for _ in range(50)]) for _ in range(10)]\nfor h in hilos: h.start()\nfor h in hilos: h.join()\nassert c.valor == 500\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s08-e5",
                "titulo": "5. Sincronización entre Hilos con threading.Event",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Hacer que un hilo espere una señal de otro antes de continuar.",
                "descripcion": "Crea una función `coordinar_senales()` donde un hilo trabajador espere una señal (`evento.wait()`) y el hilo principal active la señal con `evento.set()`.",
                "codigo_inicial": "import threading\n\ndef coordinar_senales():\n    evento = threading.Event()\n    resultado = []\n\n    def trabajador():\n        evento.wait()\n        resultado.append('Trabajador activado')\n\n    t = threading.Thread(target=trabajador)\n    t.start()\n    resultado.append('Disparando evento')\n    evento.set()\n    t.join()\n    return resultado\n",
                "tests_code": "res = coordinar_senales()\nassert 'Trabajador activado' in res\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s08-e6",
                "titulo": "6. Prevención de Interbloqueo (Deadlock)",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Evitar dependencias circulares adquiriendo siempre los locks en el mismo orden.",
                "descripcion": "Implementa una transferencia bancaria segura entre dos cuentas `transferir(cuenta_origen, cuenta_destino, monto)`. Cada cuenta tiene un `self.id` y un `self.lock`. Para evitar deadlocks cuando dos hilos transfieran en direcciones opuestas, los locks deben adquirirse siempre ordenados por el `id` menor primero.",
                "codigo_inicial": "import threading\n\nclass Cuenta:\n    def __init__(self, cuenta_id: int, saldo: float):\n        self.id = cuenta_id\n        self.saldo = saldo\n        self.lock = threading.Lock()\n\ndef transferir(origen: Cuenta, destino: Cuenta, monto: float):\n    primer_lock = origen.lock if origen.id < destino.id else destino.lock\n    segundo_lock = destino.lock if origen.id < destino.id else origen.lock\n\n    with primer_lock:\n        with segundo_lock:\n            origen.saldo -= monto\n            destino.saldo += monto\n",
                "tests_code": "c1 = Cuenta(1, 1000)\nc2 = Cuenta(2, 1000)\ntransferir(c1, c2, 200)\nassert c1.saldo == 800 and c2.saldo == 1200\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s08-e7",
                "titulo": "7. Reto Integrador: Productor-Consumidor con Cola Segura",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Implementar el clásico patrón Productor-Consumidor concurrente.",
                "descripcion": "Crea una clase `BufferConcurrente` con capacidad fija. Usa `threading.Lock` para que los productores agreguen elementos y los consumidores los extraigan sin corromper el estado.",
                "codigo_inicial": "import threading\nfrom collections import deque\n\nclass BufferConcurrente:\n    def __init__(self, capacidad: int = 10):\n        self.capacidad = capacidad\n        self.buffer = deque()\n        self.lock = threading.Lock()\n\n    def poner(self, item):\n        with self.lock:\n            if len(self.buffer) < self.capacidad:\n                self.buffer.append(item)\n                return True\n            return False\n\n    def sacar(self):\n        with self.lock:\n            if self.buffer:\n                return self.buffer.popleft()\n            return None\n",
                "tests_code": "b = BufferConcurrente(5)\nfor i in range(5): b.poner(i)\nassert b.poner(99) == False\nassert b.sacar() == 0\nassert b.poner(99) == True\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 9: INTERFACES GRÁFICAS (PYQT) ──
    {
        "id": "semana-09",
        "nombre": "Semana 9: Interfaces Gráficas (PyQt)",
        "folder": "semana-09-interfaces_graficas_1",
        "dificultad": 4,
        "descripcion": "Diseño de interfaces gráficas con PyQt6: ventanas, widgets básicos, layouts (QHBoxLayout, QVBoxLayout), señales y slots, y arquitectura front/back.",
        "actividad_id": "AC5",
        "ejercicios": [
            {
                "id": "s09-e1",
                "titulo": "1. Simulador de Señales y Slots",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Entender el patrón Observer que subyace a PyQt.",
                "descripcion": "Crea una clase `BotonSimulado` con métodos `conectar(callback)` y `hacer_click()`. Al hacer click, debe invocar a todos los callbacks registrados.",
                "codigo_inicial": "class BotonSimulado:\n    def __init__(self):\n        self.callbacks = []\n\n    def conectar(self, callback):\n        self.callbacks.append(callback)\n\n    def hacer_click(self):\n        for cb in self.callbacks:\n            cb()\n",
                "tests_code": "b = BotonSimulado()\nhits = []\nb.conectar(lambda: hits.append('click'))\nb.hacer_click()\nassert hits == ['click']\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s09-e2",
                "titulo": "2. Separación Front-End y Back-End",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Aislar la lógica de negocio de la presentación visual.",
                "descripcion": "Crea `CalculadoraBack` con método `sumar(a, b)` y `CalculadoraFront(backend)` con método `on_boton_sumar_click(str_a, str_b)` que convierta a float, invoque al backend y retorne el resultado formateado.",
                "codigo_inicial": "class CalculadoraBack:\n    def sumar(self, a: float, b: float) -> float:\n        return a + b\n\nclass CalculadoraFront:\n    def __init__(self, backend: CalculadoraBack):\n        self.backend = backend\n\n    def on_boton_sumar_click(self, str_a: str, str_b: str) -> str:\n        val = self.backend.sumar(float(str_a), float(str_b))\n        return f'Resultado: {val}'\n",
                "tests_code": "front = CalculadoraFront(CalculadoraBack())\nassert front.on_boton_sumar_click('10.5', '4.5') == 'Resultado: 15.0'\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s09-e3",
                "titulo": "3. Modelo de Formulario con Validación",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Validar entradas del usuario antes de enviarlas al modelo.",
                "descripcion": "Implementa `validar_formulario(usuario: str, password: str) -> tuple[bool, str]` que verifique que el usuario tenga al menos 4 caracteres y la contraseña al menos 8 caracteres y al menos un dígito.",
                "codigo_inicial": "def validar_formulario(usuario: str, password: str) -> tuple[bool, str]:\n    if len(usuario) < 4:\n        return (False, 'Usuario muy corto')\n    if len(password) < 8 or not any(c.isdigit() for c in password):\n        return (False, 'Password inseguro')\n    return (True, 'Válido')\n",
                "tests_code": "assert validar_formulario('ana', 'pass1234')[0] == False\nassert validar_formulario('pedro', 'secreto1')[0] == True\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s09-e4",
                "titulo": "4. Simulador de Disposición en Grid (Layout)",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Modelar coordenadas de filas y columnas en una cuadrícula.",
                "descripcion": "Crea una clase `GridLayoutSimulado` con método `agregar_widget(widget: str, fila: int, columna: int)` y `obtener(fila: int, columna: int) -> str | None`.",
                "codigo_inicial": "class GridLayoutSimulado:\n    def __init__(self):\n        self.grid = {}\n\n    def agregar_widget(self, widget: str, fila: int, columna: int):\n        self.grid[(fila, columna)] = widget\n\n    def obtener(self, fila: int, columna: int) -> str:\n        return self.grid.get((fila, columna))\n",
                "tests_code": "g = GridLayoutSimulado()\ng.agregar_widget('Boton_OK', 0, 1)\nassert g.obtener(0, 1) == 'Boton_OK'\nassert g.obtener(2, 2) is None\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s09-e5",
                "titulo": "5. Cambio de Ventanas mediante Señales",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Coordinar la apertura y cierre de ventanas secundarias.",
                "descripcion": "Implementa un `VentanaManager` con métodos `abrir_ventana(nombre)` y `ventana_actual() -> str`.",
                "codigo_inicial": "class VentanaManager:\n    def __init__(self):\n        self.actual = 'Login'\n\n    def abrir_ventana(self, nombre: str):\n        self.actual = nombre\n\n    def ventana_actual(self) -> str:\n        return self.actual\n",
                "tests_code": "vm = VentanaManager()\nassert vm.ventana_actual() == 'Login'\nvm.abrir_ventana('Dashboard')\nassert vm.ventana_actual() == 'Dashboard'\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s09-e6",
                "titulo": "6. Sistema de Estado y Reactividad",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Actualizar automáticamente la vista cuando cambia el modelo.",
                "descripcion": "Crea `EstadoObservable` con método `set_valor(val)` que notifique a todos los observadores registrados.",
                "codigo_inicial": "class EstadoObservable:\n    def __init__(self, inicial=None):\n        self._valor = inicial\n        self.suscriptores = []\n\n    def suscribir(self, callback):\n        self.suscriptores.append(callback)\n\n    def set_valor(self, nuevo_valor):\n        self._valor = nuevo_valor\n        for s in self.suscriptores:\n            s(nuevo_valor)\n",
                "tests_code": "hist = []\ne = EstadoObservable(0)\ne.suscribir(lambda v: hist.append(v))\ne.set_valor(10)\nassert hist == [10]\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s09-e7",
                "titulo": "7. Reto Integrador: Mini App GUI con Front y Back",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Desacoplar eventos visuales del backend de datos en un mini sistema completo.",
                "descripcion": "Crea una mini aplicación de tareas con `BackendTareas` (agrega tareas, lista pendientes) y `InterfazTareas(backend)` que procese los comandos de entrada del usuario.",
                "codigo_inicial": "class BackendTareas:\n    def __init__(self):\n        self.tareas = []\n    def agregar(self, texto):\n        self.tareas.append({'texto': texto, 'hecha': False})\n\nclass InterfazTareas:\n    def __init__(self, backend):\n        self.backend = backend\n    def enviar_tarea(self, texto):\n        if texto.strip():\n            self.backend.agregar(texto.strip())\n",
                "tests_code": "b = BackendTareas()\nui = InterfazTareas(b)\nui.enviar_tarea('Estudiar IIC2233')\nassert len(b.tareas) == 1 and b.tareas[0]['texto'] == 'Estudiar IIC2233'\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 10: SERIALIZACIÓN & NETWORKING I ──
    {
        "id": "semana-10",
        "nombre": "Semana 10: Serialización & Networking I",
        "folder": "semana-10-serializacion_y_networkin_1",
        "dificultad": 5,
        "descripcion": "Serialización de datos con JSON, encoders/decoders personalizados, arquitectura Cliente-Servidor y servicios web REST.",
        "actividad_id": "AC6",
        "ejercicios": [
            {
                "id": "s10-e1",
                "titulo": "1. Serialización Básica con json.dumps",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Convertir estructuras nativas de Python a cadenas JSON.",
                "descripcion": "Escribe `serializar_perfil(nombre: str, edad: int, habilidades: list[str]) -> str` que retorne el string JSON formateado.",
                "codigo_inicial": "import json\n\ndef serializar_perfil(nombre: str, edad: int, habilidades: list[str]) -> str:\n    datos = {'nombre': nombre, 'edad': edad, 'habilidades': habilidades}\n    return json.dumps(datos)\n",
                "tests_code": "s = serializar_perfil('Lucia', 21, ['Python', 'SQL'])\nassert 'Lucia' in s and 'SQL' in s\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s10-e2",
                "titulo": "2. Deserialización con json.loads",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Parsear una cadena JSON y convertirla a tipos nativos.",
                "descripcion": "Escribe `deserializar_usuarios(json_str: str) -> int` que reciba un JSON de una lista de usuarios y retorne la cantidad de usuarios presentes.",
                "codigo_inicial": "import json\n\ndef deserializar_usuarios(json_str: str) -> int:\n    lista = json.loads(json_str)\n    return len(lista)\n",
                "tests_code": "assert deserializar_usuarios('[{\"id\": 1}, {\"id\": 2}, {\"id\": 3}]') == 3\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s10-e3",
                "titulo": "3. Custom JSONEncoder para Clases Propias",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Extender `json.JSONEncoder` para que `json.dumps` admita objetos de clases de usuario.",
                "descripcion": "Crea una clase `Punto(x, y)` y un encoder `PuntoEncoder(json.JSONEncoder)` que convierta cualquier instancia de `Punto` al diccionario `{'x': obj.x, 'y': obj.y}`.",
                "codigo_inicial": "import json\n\nclass Punto:\n    def __init__(self, x: float, y: float):\n        self.x = x\n        self.y = y\n\nclass PuntoEncoder(json.JSONEncoder):\n    def default(self, obj):\n        if isinstance(obj, Punto):\n            return {'x': obj.x, 'y': obj.y}\n        return super().default(obj)\n",
                "tests_code": "p = Punto(10.5, 20.0)\ns = json.dumps(p, cls=PuntoEncoder)\nassert '\"x\": 10.5' in s\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s10-e4",
                "titulo": "4. Reconstrucción con Object Hook",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Transformar diccionarios deserializados en instancias de clase automáticamente.",
                "descripcion": "Escribe una función hook `reconstruir_punto(d: dict)` que si contiene claves `'x'` e `'y'`, retorne una instancia de `Punto`.",
                "codigo_inicial": "class Punto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\ndef reconstruir_punto(d: dict):\n    if 'x' in d and 'y' in d:\n        return Punto(d['x'], d['y'])\n    return d\n",
                "tests_code": "p = json.loads('{\"x\": 3, \"y\": 4}', object_hook=reconstruir_punto)\nassert isinstance(p, Punto) and p.x == 3\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s10-e5",
                "titulo": "5. Manejo Robusto de JSON Corrupto",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Capturar `json.JSONDecodeError` y proveer valores por defecto seguros.",
                "descripcion": "Escribe `cargar_json_seguro(texto: str, default=None)` que capture cualquier fallo de sintaxis en el JSON y retorne `default`.",
                "codigo_inicial": "import json\n\ndef cargar_json_seguro(texto: str, default=None):\n    try:\n        return json.loads(texto)\n    except json.JSONDecodeError:\n        return default\n",
                "tests_code": "assert cargar_json_seguro('{\"ok\": 1}') == {'ok': 1}\nassert cargar_json_seguro('{invalido}', default={}) == {}\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s10-e6",
                "titulo": "6. Simulación de Petición HTTP Request / Response",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Modelar el intercambio de mensajes en APIs REST.",
                "descripcion": "Crea una función `procesar_request(payload_json: str) -> str` que reciba `{'accion': 'eco', 'mensaje': str}` y retorne un JSON de respuesta `{'status': 'success', 'eco': mensaje}`.",
                "codigo_inicial": "import json\n\ndef procesar_request(payload_json: str) -> str:\n    req = json.loads(payload_json)\n    res = {'status': 'success', 'eco': req.get('mensaje')}\n    return json.dumps(res)\n",
                "tests_code": "r = procesar_request('{\"accion\": \"eco\", \"mensaje\": \"Hola Servidor\"}')\nassert 'Hola Servidor' in r and 'success' in r\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s10-e7",
                "titulo": "7. Reto Integrador: Almacén Clave-Valor con Serialización",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Construir un almacén en memoria que serialice su estado completo.",
                "descripcion": "Crea `KeyStore` con métodos `set(clave, valor)`, `get(clave)`, `exportar() -> str` (exporta a JSON) e `importar(json_str)` (restaura el estado).",
                "codigo_inicial": "import json\n\nclass KeyStore:\n    def __init__(self):\n        self.datos = {}\n\n    def set(self, clave, valor):\n        self.datos[clave] = valor\n\n    def get(self, clave):\n        return self.datos.get(clave)\n\n    def exportar(self) -> str:\n        return json.dumps(self.datos)\n\n    def importar(self, json_str: str):\n        self.datos = json.loads(json_str)\n",
                "tests_code": "ks = KeyStore()\nks.set('token', 'abc123xyz')\ns = ks.exportar()\nks2 = KeyStore()\nks2.importar(s)\nassert ks2.get('token') == 'abc123xyz'\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 11: SERIALIZACIÓN & NETWORKING II ──
    {
        "id": "semana-11",
        "nombre": "Semana 11: Serialización & Networking II",
        "folder": "semana-11-serializacion_y_networking_2",
        "dificultad": 5,
        "descripcion": "Serialización binaria con Pickle, manejo y codificación de bytes, empaquetado/desempaquetado con cabeceras de tamaño y sockets TCP.",
        "actividad_id": "AC6",
        "ejercicios": [
            {
                "id": "s11-e1",
                "titulo": "1. Codificación y Decodificación de Bytes",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Convertir entre cadenas str y arreglos de bytes con UTF-8.",
                "descripcion": "Escribe `codificar(texto: str) -> bytes` y `decodificar(datos: bytes) -> str` usando la codificación UTF-8.",
                "codigo_inicial": "def codificar(texto: str) -> bytes:\n    return texto.encode('utf-8')\n\ndef decodificar(datos: bytes) -> str:\n    return datos.decode('utf-8')\n",
                "tests_code": "b = codificar('ClearnP.A')\nassert isinstance(b, bytes)\nassert decodificar(b) == 'ClearnP.A'\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s11-e2",
                "titulo": "2. Conversión de Enteros a Bytes con Big-Endian",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Usar `to_bytes` y `from_bytes` para crear identificadores o largos de paquete.",
                "descripcion": "Escribe `entero_a_bytes(n: int, num_bytes: int = 4) -> bytes` usando orden `'big'`, y `bytes_a_entero(b: bytes) -> int`.",
                "codigo_inicial": "def entero_a_bytes(n: int, num_bytes: int = 4) -> bytes:\n    return n.to_bytes(num_bytes, byteorder='big')\n\ndef bytes_a_entero(b: bytes) -> int:\n    return int.from_bytes(b, byteorder='big')\n",
                "tests_code": "b = entero_a_bytes(1024, 4)\nassert len(b) == 4\nassert bytes_a_entero(b) == 1024\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s11-e3",
                "titulo": "3. Serialización Binaria con Pickle",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Serializar grafos de objetos arbitrarios a bytes con `pickle`.",
                "descripcion": "Escribe `serializar_objeto(obj) -> bytes` y `deserializar_objeto(datos: bytes)` usando `pickle.dumps` y `pickle.loads`.",
                "codigo_inicial": "import pickle\n\ndef serializar_objeto(obj) -> bytes:\n    return pickle.dumps(obj)\n\ndef deserializar_objeto(datos: bytes):\n    return pickle.loads(datos)\n",
                "tests_code": "data = {'nums': [1, 2, 3], 'set': {4, 5}}\nb = serializar_objeto(data)\nres = deserializar_objeto(b)\nassert res == data\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s11-e4",
                "titulo": "4. Empaquetado con Cabecera de Tamaño (Framing)",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Resolver el problema de delimitación de mensajes en TCP (Stream de bytes).",
                "descripcion": "Escribe `empaquetar(mensaje: str) -> bytearray` que cree un paquete de red con 4 bytes de encabezado (longitud en big-endian) seguidos del contenido en UTF-8.",
                "codigo_inicial": "def empaquetar(mensaje: str) -> bytearray:\n    payload = mensaje.encode('utf-8')\n    largo = len(payload).to_bytes(4, byteorder='big')\n    return bytearray(largo + payload)\n",
                "tests_code": "pkt = empaquetar('Hola')\nassert len(pkt) == 4 + 4 # 4 bytes header + 4 bytes 'Hola'\nassert int.from_bytes(pkt[:4], 'big') == 4\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s11-e5",
                "titulo": "5. Desempaquetado de Paquetes en Red",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Leer la cabecera fija y extraer exactamente la cantidad de bytes indicada.",
                "descripcion": "Implementa `desempaquetar(paquete: bytearray) -> str` que lea los primeros 4 bytes para saber cuántos bytes leer del cuerpo, y lo decodifique a texto.",
                "codigo_inicial": "def desempaquetar(paquete: bytearray) -> str:\n    largo = int.from_bytes(paquete[:4], byteorder='big')\n    return paquete[4:4+largo].decode('utf-8')\n",
                "tests_code": "pkt = bytearray((5).to_bytes(4, 'big') + b'Mundo')\nassert desempaquetar(pkt) == 'Mundo'\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s11-e6",
                "titulo": "6. Fragmentación y Chunks de Red",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Partir un flujo grande en bloques de tamaño fijo (ej. 1024 bytes).",
                "descripcion": "Escribe `dividir_en_chunks(datos: bytes, tamano_chunk: int = 4) -> list[bytes]` que devuelva la lista de fragmentos.",
                "codigo_inicial": "def dividir_en_chunks(datos: bytes, tamano_chunk: int = 4) -> list[bytes]:\n    return [datos[i:i+tamano_chunk] for i in range(0, len(datos), tamano_chunk)]\n",
                "tests_code": "c = dividir_en_chunks(b'123456789', 3)\nassert c == [b'123', b'456', b'789']\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s11-e7",
                "titulo": "7. Reto Integrador: Protocolo de Red Completo con Hash",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Garantizar integridad en transmisión combinando payload, tamaño y tipo de comando.",
                "descripcion": "Diseña `ProtocoloRed`: método `crear_mensaje(comando: str, datos: str) -> bytes` (1 byte para comando 'M' o 'D', 4 bytes largo, payload) y `leer_mensaje(paquete: bytes) -> tuple[str, str]`.",
                "codigo_inicial": "class ProtocoloRed:\n    @staticmethod\n    def crear_mensaje(comando: str, datos: str) -> bytes:\n        cmd_b = comando.encode('ascii')[:1]\n        payload_b = datos.encode('utf-8')\n        largo_b = len(payload_b).to_bytes(4, 'big')\n        return cmd_b + largo_b + payload_b\n\n    @staticmethod\n    def leer_mensaje(paquete: bytes) -> tuple[str, str]:\n        cmd = paquete[:1].decode('ascii')\n        largo = int.from_bytes(paquete[1:5], 'big')\n        datos = paquete[5:5+largo].decode('utf-8')\n        return (cmd, datos)\n",
                "tests_code": "pkt = ProtocoloRed.crear_mensaje('M', 'Mensaje Secreto')\ncmd, msg = ProtocoloRed.leer_mensaje(pkt)\nassert cmd == 'M' and msg == 'Mensaje Secreto'\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 14: GUI AVANZADA CON QTHREADS ──
    {
        "id": "semana-14",
        "nombre": "Semana 14: GUI Avanzada con QThreads",
        "folder": "semana-14-interfaces_graficas_2",
        "dificultad": 5,
        "descripcion": "Separación de hilos de cómputo y el hilo visual de PyQt mediante QThread, señales pyqtSignal y sincronización asíncrona.",
        "actividad_id": "AC7",
        "ejercicios": [
            {
                "id": "s14-e1",
                "titulo": "1. Simulador de Señal PyQtSignal",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Modelar el envío de señales tipadas entre hilos y vistas.",
                "descripcion": "Crea una clase `SignalSimulada` que permita `conectar(slot)` y `emitir(*args)`. Cada vez que se emita, debe ejecutar todos los slots registrados con los argumentos.",
                "codigo_inicial": "class SignalSimulada:\n    def __init__(self):\n        self.slots = []\n\n    def conectar(self, slot):\n        self.slots.append(slot)\n\n    def emitir(self, *args):\n        for s in self.slots:\n            s(*args)\n",
                "tests_code": "sig = SignalSimulada()\nvalores = []\nsig.conectar(lambda x: valores.append(x * 2))\nsig.emitir(5)\nassert valores == [10]\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s14-e2",
                "titulo": "2. Patrón Worker Asíncrono",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Encapsular trabajo pesado en una entidad que no bloquee.",
                "descripcion": "Crea `WorkerTarea` con método `ejecutar()` que procese una lista de números calculando sus factoriales y emita una señal al finalizar.",
                "codigo_inicial": "class WorkerTarea:\n    def __init__(self, datos: list[int]):\n        self.datos = datos\n        self.resultado = []\n\n    def ejecutar(self):\n        self.resultado = [x * 10 for x in self.datos]\n",
                "tests_code": "w = WorkerTarea([1, 2, 3])\nw.ejecutar()\nassert w.resultado == [10, 20, 30]\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s14-e3",
                "titulo": "3. Notificador de Progreso en Porcentaje",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Emitir actualizaciones periódicas para una barra de progreso.",
                "descripcion": "Escribe `procesar_con_progreso(elementos: list, callback_progreso)` que por cada elemento procesado invoque `callback_progreso(porcentaje: int)`.",
                "codigo_inicial": "def procesar_con_progreso(elementos: list, callback_progreso):\n    total = len(elementos)\n    for i, e in enumerate(elementos, 1):\n        porcentaje = int((i / total) * 100)\n        callback_progreso(porcentaje)\n",
                "tests_code": "hist = []\nprocesar_con_progreso([1, 2, 3, 4], lambda p: hist.append(p))\nassert hist == [25, 50, 75, 100]\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s14-e4",
                "titulo": "4. Cancelación Segura de Tareas en Segundo Plano",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Interrumpir un proceso en bucle mediante flags booleanas sin terminar bruscamente el hilo.",
                "descripcion": "Crea `WorkerCancelable` con método `cancelar()` que ponga `self.detenido = True` y detenga su ejecución antes de terminar toda la secuencia.",
                "codigo_inicial": "class WorkerCancelable:\n    def __init__(self):\n        self.detenido = False\n        self.pasos_completados = 0\n\n    def cancelar(self):\n        self.detenido = True\n\n    def ejecutar(self, total_pasos: int):\n        for _ in range(total_pasos):\n            if self.detenido:\n                break\n            self.pasos_completados += 1\n",
                "tests_code": "w = WorkerCancelable()\nw.ejecutar(2)\nw.cancelar()\nw.ejecutar(5)\nassert w.pasos_completados == 2\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s14-e5",
                "titulo": "5. Encolador de Trabajos (Task Queue)",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Gestionar una fila de peticiones asíncronas para la interfaz.",
                "descripcion": "Crea una clase `GestorTrabajos` que acumule tareas pendientes y las despache una por una.",
                "codigo_inicial": "from collections import deque\n\nclass GestorTrabajos:\n    def __init__(self):\n        self.pendientes = deque()\n\n    def agregar(self, tarea):\n        self.pendientes.append(tarea)\n\n    def despachar_siguiente(self):\n        if self.pendientes:\n            return self.pendientes.popleft()()\n        return None\n",
                "tests_code": "gt = GestorTrabajos()\ngt.agregar(lambda: 'Tarea 1 lista')\nassert gt.despachar_siguiente() == 'Tarea 1 lista'\nassert gt.despachar_siguiente() is None\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s14-e6",
                "titulo": "6. Captura de Excepciones en Workers",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Evitar que una excepción en un hilo secundario congele la aplicación sin avisar al usuario.",
                "descripcion": "Crea `WorkerRobusto` con callback de error `on_error(mensaje)`. Si la función objetivo lanza excepción, la captura y la envía por el callback.",
                "codigo_inicial": "class WorkerRobusto:\n    def __init__(self, callback_error):\n        self.callback_error = callback_error\n\n    def ejecutar_tarea(self, funcion):\n        try:\n            funcion()\n        except Exception as e:\n            self.callback_error(str(e))\n",
                "tests_code": "errores = []\nw = WorkerRobusto(lambda err: errores.append(err))\nw.ejecutar_tarea(lambda: 1 / 0)\nassert len(errores) == 1 and 'division by zero' in errores[0]\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s14-e7",
                "titulo": "7. Reto Integrador: Arquitectura Worker + GUI Desacoplada",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Coordinar modelo, worker de cómputo y vista con sincronización de estado.",
                "descripcion": "Diseña un sistema donde un `ProcesadorWorker` reciba datos, los ordene, calcule estadísticas y notifique a una `VistaSimulada` para actualizar su pantalla.",
                "codigo_inicial": "class ProcesadorWorker:\n    def procesar(self, datos: list[float], callback_vista):\n        datos_ordenados = sorted(datos)\n        promedio = sum(datos_ordenados) / len(datos_ordenados) if datos_ordenados else 0\n        callback_vista({'ordenados': datos_ordenados, 'promedio': promedio})\n",
                "tests_code": "p = ProcesadorWorker()\npantalla = {}\np.procesar([4, 1, 3], lambda res: pantalla.update(res))\nassert pantalla['ordenados'] == [1, 3, 4]\nassert pantalla['promedio'] == 2.6666666666666665\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    },

    # ── SEMANA 15: TÓPICOS AVANZADOS & GRAFOS ──
    {
        "id": "semana-15",
        "nombre": "Semana 15: Tópicos Avanzados & Grafos",
        "folder": "semana-15-topicos-avanzados",
        "dificultad": 5,
        "descripcion": "Expresiones regulares (Regex), representación de grafos (listas de adyacencia), búsqueda en amplitud (BFS) y profundidad (DFS), NumPy y Pandas.",
        "actividad_id": "ACBonus",
        "ejercicios": [
            {
                "id": "s15-e1",
                "titulo": "1. Validación de Correos Institucionales con Regex",
                "nivel": "Nivel 1 (Muy Fácil)",
                "dificultad_num": 1,
                "objetivo": "Usar el módulo `re` para validar cadenas con formato estricto.",
                "descripcion": "Escribe `es_correo_uc(correo: str) -> bool` que retorne True si el correo termina en `@uc.cl` o `@estudiante.uc.cl`.",
                "codigo_inicial": "import re\n\ndef es_correo_uc(correo: str) -> bool:\n    patron = r'^[a-zA-Z0-9._%+-]+@(estudiante\\.)?uc\\.cl$'\n    return bool(re.match(patron, correo))\n",
                "tests_code": "assert es_correo_uc('damin.bravo@estudiante.uc.cl') == True\nassert es_correo_uc('profesor@uc.cl') == True\nassert es_correo_uc('usuario@gmail.com') == False\nprint('✅ Ejercicio 1 superado exitosamente!')\n"
            },
            {
                "id": "s15-e2",
                "titulo": "2. Extracción de Fechas con Grupos de Captura",
                "nivel": "Nivel 2 (Fácil)",
                "dificultad_num": 2,
                "objetivo": "Capturar partes específicas de un string usando paréntesis `()` en regex.",
                "descripcion": "Escribe `extraer_fechas(texto: str) -> list[str]` que encuentre todas las fechas con formato `DD/MM/AAAA`.",
                "codigo_inicial": "import re\n\ndef extraer_fechas(texto: str) -> list[str]:\n    patron = r'\\b\\d{2}/\\d{2}/\\d{4}\\b'\n    return re.findall(patron, texto)\n",
                "tests_code": "t = 'El evento fue el 12/03/2026 y la entrega el 15/03/2026.'\nassert extraer_fechas(t) == ['12/03/2026', '15/03/2026']\nprint('✅ Ejercicio 2 superado exitosamente!')\n"
            },
            {
                "id": "s15-e3",
                "titulo": "3. Representación de Grafos con Lista de Adyacencia",
                "nivel": "Nivel 3 (Fácil-Medio)",
                "dificultad_num": 3,
                "objetivo": "Modelar nodos y aristas usando diccionarios.",
                "descripcion": "Crea una clase `Grafo` con método `agregar_arista(origen, destino)` que almacene aristas no dirigidas y `vecinos(nodo) -> list`.",
                "codigo_inicial": "from collections import defaultdict\n\nclass Grafo:\n    def __init__(self):\n        self.adyacencia = defaultdict(list)\n\n    def agregar_arista(self, u, v):\n        self.adyacencia[u].append(v)\n        self.adyacencia[v].append(u)\n\n    def vecinos(self, u) -> list:\n        return self.adyacencia.get(u, [])\n",
                "tests_code": "g = Grafo()\ng.agregar_arista('A', 'B')\ng.agregar_arista('A', 'C')\nassert set(g.vecinos('A')) == {'B', 'C'}\nprint('✅ Ejercicio 3 superado exitosamente!')\n"
            },
            {
                "id": "s15-e4",
                "titulo": "4. Búsqueda en Amplitud (BFS): Camino Más Corto",
                "nivel": "Nivel 4 (Medio)",
                "dificultad_num": 4,
                "objetivo": "Encontrar la ruta con menor número de pasos en grafos no ponderados usando `deque`.",
                "descripcion": "Implementa `bfs_camino_corto(grafo: dict, inicio, fin) -> list` que retorne la lista de nodos del camino.",
                "codigo_inicial": "from collections import deque\n\ndef bfs_camino_corto(grafo: dict, inicio, fin) -> list:\n    cola = deque([[inicio]])\n    visitados = {inicio}\n    while cola:\n        camino = cola.popleft()\n        nodo = camino[-1]\n        if nodo == fin:\n            return camino\n        for vecino in grafo.get(nodo, []):\n            if vecino not in visitados:\n                visitados.add(vecino)\n                cola.append(camino + [vecino])\n    return []\n",
                "tests_code": "g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}\nassert bfs_camino_corto(g, 'A', 'E') in (['A', 'B', 'D', 'E'], ['A', 'C', 'D', 'E'])\nprint('✅ Ejercicio 4 superado exitosamente!')\n"
            },
            {
                "id": "s15-e5",
                "titulo": "5. Búsqueda en Profundidad (DFS): Detección de Conectividad",
                "nivel": "Nivel 5 (Medio-Avanzado)",
                "dificultad_num": 5,
                "objetivo": "Explorar ramas completas recursivamente.",
                "descripcion": "Escribe `existe_camino_dfs(grafo: dict, actual, destino, visitados=None) -> bool`.",
                "codigo_inicial": "def existe_camino_dfs(grafo: dict, actual, destino, visitados=None) -> bool:\n    if visitados is None:\n        visitados = set()\n    if actual == destino:\n        return True\n    visitados.add(actual)\n    for vecino in grafo.get(actual, []):\n        if vecino not in visitados:\n            if existe_camino_dfs(grafo, vecino, destino, visitados):\n                return True\n    return False\n",
                "tests_code": "g = {'A': ['B'], 'B': ['C'], 'C': [], 'X': ['Y'], 'Y': []}\nassert existe_camino_dfs(g, 'A', 'C') == True\nassert existe_camino_dfs(g, 'A', 'X') == False\nprint('✅ Ejercicio 5 superado exitosamente!')\n"
            },
            {
                "id": "s15-e6",
                "titulo": "6. Detección de Ciclos en Grafos No Dirigidos",
                "nivel": "Nivel 6 (Avanzado)",
                "dificultad_num": 6,
                "objetivo": "Identificar si un grafo contiene ciclos o es un árbol.",
                "descripcion": "Implementa `tiene_ciclo(grafo: dict) -> bool`.",
                "codigo_inicial": "def tiene_ciclo(grafo: dict) -> bool:\n    visitados = set()\n    def dfs(nodo, padre):\n        visitados.add(nodo)\n        for vecino in grafo.get(nodo, []):\n            if vecino not in visitados:\n                if dfs(vecino, nodo):\n                    return True\n            elif vecino != padre:\n                return True\n        return False\n    for n in grafo:\n        if n not in visitados:\n            if dfs(n, None):\n                return True\n    return False\n",
                "tests_code": "g_con_ciclo = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}\nassert tiene_ciclo(g_con_ciclo) == True\nprint('✅ Ejercicio 6 superado exitosamente!')\n"
            },
            {
                "id": "s15-e7",
                "titulo": "7. Reto Integrador: Analizador de Red con BFS y Métricas",
                "nivel": "Nivel 7 (Reto Pre-AC)",
                "dificultad_num": 7,
                "objetivo": "Calcular grados de separación entre cualquier par de nodos en una red.",
                "descripcion": "Crea una función `grado_separacion(grafo: dict, usuario1: str, usuario2: str) -> int` que retorne la distancia mínima (número de aristas) entre ambos, o -1 si no están conectados.",
                "codigo_inicial": "from collections import deque\n\ndef grado_separacion(grafo: dict, u1: str, u2: str) -> int:\n    if u1 == u2:\n        return 0\n    cola = deque([(u1, 0)])\n    visitados = {u1}\n    while cola:\n        actual, dist = cola.popleft()\n        if actual == u2:\n            return dist\n        for vecino in grafo.get(actual, []):\n            if vecino not in visitados:\n                visitados.add(vecino)\n                cola.append((vecino, dist + 1))\n    return -1\n",
                "tests_code": "red = {'Lucas': ['Sofia'], 'Sofia': ['Lucas', 'Mateo'], 'Mateo': ['Sofia', 'Ana'], 'Ana': ['Mateo'], 'Solitario': []}\nassert grado_separacion(red, 'Lucas', 'Ana') == 3\nassert grado_separacion(red, 'Lucas', 'Solitario') == -1\nprint('✅ Reto 7 superado exitosamente!')\n"
            }
        ]
    }
]

# ── ACTIVIDADES EN FORMATO UN SOLO ARCHIVO (SINGLE-FILE) ──
ACTIVIDADES_SINGLE_FILE = [
    {
        "id": "AC1",
        "titulo": "AC1: Tabla de Medallistas Olímpicos (OOP y Colecciones)",
        "tipo": "actividad",
        "dificultad": 4,
        "descripcion": "Implementar un sistema de seguimiento de medallistas olímpicos usando Programación Orientada a Objetos. Debes completar la lectura de datos, el registro de países con sus puntajes y el ordenamiento de la tabla final.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 1: TABLA DE MEDALLISTAS OLÍMPICOS (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

# Datos de prueba simulando el archivo .dcc
SAMPLE_DATA = """Elin Andersson,Patinaje Artístico,Bronce,Suecia
Lucas García,Atletismo,Oro,España
Maria Rossi,Natación,Plata,Italia
John Smith,Gimnasia,Oro,Estados Unidos
Hans Muller,Esquí,Oro,Alemania
Clara Rossi,Esgrima,Bronce,Italia
Marco Silva,Judo,Oro,Brasil
"""

def get_puntaje(pais) -> int:
    """Retorna el puntaje de un país. Se usa como key de ordenamiento."""
    return pais.puntaje


class Medallista:
    """Representa a un atleta premiado."""
    def __init__(self, nombre: str, deporte: str, medalla: str, nombre_pais: str):
        self.nombre = nombre
        self.deporte = deporte
        self.medalla = medalla
        self.nombre_pais = nombre_pais


class Pais:
    """Registra y acumula medallas y puntaje de un país."""
    def __init__(self, nombre_pais: str):
        self.nombre_pais = nombre_pais
        self.puntaje = 0
        self.oros = 0
        self.platas = 0
        self.bronces = 0

    def agregar_medallista(self, medallista: Medallista):
        """
        Puntajes:
        - Oro: 5 puntos
        - Plata: 3 puntos
        - Bronce: 1 punto
        """
        if medallista.medalla == "Oro":
            self.oros += 1
            self.puntaje += 5
        elif medallista.medalla == "Plata":
            self.platas += 1
            self.puntaje += 3
        elif medallista.medalla == "Bronce":
            self.bronces += 1
            self.puntaje += 1


class TablaPuntajes:
    """Administra la lista de países participantes."""
    def __init__(self):
        self.paises = []

    def agregar_medallista(self, medallista: Medallista):
        """Busca el país del medallista. Si no existe, lo crea y suma la medalla."""
        for pais in self.paises:
            if pais.nombre_pais == medallista.nombre_pais:
                pais.agregar_medallista(medallista)
                return
        nuevo = Pais(medallista.nombre_pais)
        nuevo.agregar_medallista(medallista)
        self.paises.append(nuevo)

    def ordenar_paises(self) -> list[Pais]:
        """Ordena los países de mayor a menor puntaje."""
        return sorted(self.paises, key=get_puntaje, reverse=True)


def cargar_medallistas(texto_datos: str) -> list[Medallista]:
    """Parsea el texto CSV y retorna la lista de objetos Medallista."""
    medallistas = []
    for linea in texto_datos.strip().split("\\n"):
        if linea.strip():
            nombre, deporte, medalla, pais = linea.strip().split(",")
            medallistas.append(Medallista(nombre, deporte, medalla, pais))
    return medallistas


def crear_tabla(medallistas: list[Medallista]) -> TablaPuntajes:
    """Crea la tabla y procesa todos los medallistas."""
    tabla = TablaPuntajes()
    for m in medallistas:
        tabla.agregar_medallista(m)
    return tabla


# --- VERIFICACIÓN Y PRUEBAS ---
if __name__ == "__main__":
    print("--- PROCESANDO ACTIVIDAD 1 ---")
    atletas = cargar_medallistas(SAMPLE_DATA)
    tabla = crear_tabla(atletas)
    ranking = tabla.ordenar_paises()

    for i, p in enumerate(ranking, 1):
        print(f"{i}. {p.nombre_pais}: {p.oros} Oros, {p.platas} Platas, {p.bronces} Bronces (Total: {p.puntaje} pts)")

    # Aserciones
    assert len(atletas) == 7
    assert ranking[0].puntaje >= ranking[-1].puntaje
    print("\\n✅ ¡AC1 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado para AC1
atletas = cargar_medallistas(SAMPLE_DATA)
assert len(atletas) == 7
t = crear_tabla(atletas)
paises = {p.nombre_pais: p for p in t.paises}
assert "Italia" in paises
assert paises["Italia"].platas == 1
assert paises["Italia"].bronces == 1
assert paises["Italia"].puntaje == 4
assert t.ordenar_paises()[0].puntaje >= t.ordenar_paises()[-1].puntaje
print("🎉 AC1 superada con éxito!")
'''
    },

    {
        "id": "AC2",
        "titulo": "AC2: Estadísticas de Premios (NamedTuples & Dicts)",
        "tipo": "actividad",
        "dificultad": 4,
        "descripcion": "Calcular estadísticas históricas de ganadores de premios (Oscars, Grammys, Tonys, Emmys) usando namedtuples, diccionarios y conjuntos para responder consultas con eficiencia.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 2: ESTADÍSTICAS DE PREMIOS (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

from collections import namedtuple, defaultdict

Winner = namedtuple("Winner", ["name", "award_name"])

class AwardStatistics:
    """Clase encargada de calcular estadísticas de premios (Oscars, Grammys, etc.)."""
    def __init__(self):
        # Diccionario persona -> lista de premios ganados
        self.premios_por_persona = defaultdict(list)
        # Diccionario premio -> lista de personas que lo ganaron
        self.ganadores_por_premio = defaultdict(list)

    def add_winner(self, name: str, award_name: str) -> None:
        """Registra un nuevo premio ganado por una persona."""
        self.premios_por_persona[name].append(award_name)
        self.ganadores_por_premio[award_name].append(name)

    def get_top_winner(self) -> tuple[str, int]:
        """Retorna (nombre, total_premios) de la persona con más premios en total."""
        if not self.premios_por_persona:
            return ("", 0)
        mejor = max(self.premios_por_persona.items(), key=lambda item: len(item[1]))
        return (mejor[0], len(mejor[1]))

    def get_top_winner_in_award(self, award_name: str) -> tuple[str, int]:
        """Retorna (nombre, cantidad) de la persona con más premios de un tipo específico."""
        ganadores = self.ganadores_por_premio.get(award_name, [])
        if not ganadores:
            return ("", 0)
        conteo = defaultdict(int)
        for g in ganadores:
            conteo[g] += 1
        mejor = max(conteo.items(), key=lambda item: item[1])
        return (mejor[0], mejor[1])

    def get_all_winners_in_award(self, award_name: str) -> set[str]:
        """Retorna el set de todos los ganadores únicos de un premio."""
        return set(self.ganadores_por_premio.get(award_name, []))

    def get_egot_winners(self) -> set[str]:
        """Retorna los nombres de quienes han ganado un EGOT (Emmy, Grammy, Oscar, Tony)."""
        egot_set = {"Emmy", "Grammy", "Oscar", "Tony"}
        ganadores_egot = set()
        for persona, premios in self.premios_por_persona.items():
            if egot_set.issubset(set(premios)):
                ganadores_egot.add(persona)
        return ganadores_egot


# --- VERIFICACIÓN Y PRUEBAS ---
if __name__ == "__main__":
    stats = AwardStatistics()
    # John Legend es EGOT
    for p in ["Emmy", "Grammy", "Oscar", "Tony", "Grammy"]:
        stats.add_winner("John Legend", p)
    # Adele tiene Oscar y Grammy
    stats.add_winner("Adele", "Oscar")
    stats.add_winner("Adele", "Grammy")

    print("Top Winner Global:", stats.get_top_winner())
    print("Ganadores de EGOT:", stats.get_egot_winners())

    assert stats.get_top_winner() == ("John Legend", 5)
    assert stats.get_egot_winners() == {"John Legend"}
    print("\\n✅ ¡AC2 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC2
stats = AwardStatistics()
stats.add_winner("Rita Moreno", "Emmy")
stats.add_winner("Rita Moreno", "Grammy")
stats.add_winner("Rita Moreno", "Oscar")
stats.add_winner("Rita Moreno", "Tony")
stats.add_winner("Actor A", "Oscar")
assert stats.get_egot_winners() == {"Rita Moreno"}
assert "Actor A" in stats.get_all_winners_in_award("Oscar")
print("🎉 AC2 superada con éxito!")
'''
    },

    {
        "id": "AC3",
        "titulo": "AC3: Simulación Genética (Multiherencia & Mixins)",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Construir una jerarquía de genes, rasgos y dominancia utilizando clases abstractas (ABC), herencia múltiple y llamadas a super() para simular combinaciones biológicas.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 3: SIMULACIÓN GENÉTICA (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

from abc import ABC, abstractmethod

class Gen(ABC):
    """Clase base abstracta de genes."""
    def __init__(self, rasgo: str, alelo: str, es_dominante: bool, **kwargs):
        super().__init__(**kwargs)
        self.rasgo = rasgo
        self.alelo = alelo
        self.es_dominante = es_dominante

    @abstractmethod
    def expresar(self) -> str:
        """Retorna la manifestación física del gen."""
        pass


class GenColorOjos(Gen):
    def __init__(self, alelo: str = "Marron", es_dominante: bool = True, **kwargs):
        super().__init__(rasgo="ColorOjos", alelo=alelo, es_dominante=es_dominante, **kwargs)

    def expresar(self) -> str:
        return f"Ojos {self.alelo}"


class GenColorCabello(Gen):
    def __init__(self, alelo: str = "Negro", es_dominante: bool = True, **kwargs):
        super().__init__(rasgo="ColorCabello", alelo=alelo, es_dominante=es_dominante, **kwargs)

    def expresar(self) -> str:
        return f"Cabello {self.alelo}"


class Individuo(GenColorOjos, GenColorCabello):
    """Individuo que combina múltiples genes mediante herencia múltiple colaborativa."""
    def __init__(self, nombre: str, alelo_ojos: str, alelo_cabello: str):
        super().__init__(alelo=alelo_ojos)
        self.nombre = nombre
        self.alelo_cabello = alelo_cabello

    def describir(self) -> str:
        return f"{self.nombre}: {self.expresar()}, Cabello {self.alelo_cabello}"


if __name__ == "__main__":
    ind = Individuo("Alex", "Azules", "Castano")
    print(ind.describir())
    assert "Azules" in ind.describir()
    print("\\n✅ ¡AC3 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC3
ind = Individuo("Lucas", "Verdes", "Rubio")
desc = ind.describir()
assert "Verdes" in desc and "Rubio" in desc
print("🎉 AC3 superada con éxito!")
'''
    },

    {
        "id": "AC4",
        "titulo": "AC4: Búsqueda en Tableros y Laberintos",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Modelar tableros con obstáculos y encontrar caminos válidos utilizando algoritmos de búsqueda y estructuras de datos eficientes en Python.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 4: BÚSQUEDA EN LABERINTOS (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

from collections import deque

TABLERO = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "E"]
]

class Laberinto:
    def __init__(self, mapa: list[list[str]]):
        self.mapa = mapa
        self.filas = len(mapa)
        self.cols = len(mapa[0])
        self.inicio = self._encontrar("S")
        self.fin = self._encontrar("E")

    def _encontrar(self, char: str) -> tuple[int, int]:
        for r in range(self.filas):
            for c in range(self.cols):
                if self.mapa[r][c] == char:
                    return (r, c)
        return (0, 0)

    def es_valido(self, r: int, c: int) -> bool:
        return 0 <= r < self.filas and 0 <= c < self.cols and self.mapa[r][c] != "#"

    def resolver_bfs(self) -> list[tuple[int, int]]:
        """Retorna el camino más corto desde S hasta E usando BFS."""
        cola = deque([[self.inicio]])
        visitados = {self.inicio}

        while cola:
            camino = cola.popleft()
            r, c = camino[-1]
            if (r, c) == self.fin:
                return camino

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if self.es_valido(nr, nc) and (nr, nc) not in visitados:
                    visitados.add((nr, nc))
                    cola.append(camino + [(nr, nc)])
        return []


if __name__ == "__main__":
    lab = Laberinto(TABLERO)
    camino = lab.resolver_bfs()
    print("Camino encontrado con pasos:", len(camino))
    assert len(camino) > 0
    assert camino[0] == lab.inicio and camino[-1] == lab.fin
    print("\\n✅ ¡AC4 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC4
lab = Laberinto(TABLERO)
camino = lab.resolver_bfs()
assert len(camino) == 9
assert camino[-1] == (4, 4)
print("🎉 AC4 superada con éxito!")
'''
    },

    {
        "id": "AC5",
        "titulo": "AC5: Simulación de Eventos y Manejo Asíncrono",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Crear un motor de eventos concurrentes utilizando programación funcional, generadores y cola de prioridades.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 5: MOTOR DE EVENTOS (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

import heapq

class Evento:
    def __init__(self, tiempo: float, tipo: str, datos: dict = None):
        self.tiempo = tiempo
        self.tipo = tipo
        self.datos = datos or {}

    def __lt__(self, otro):
        return self.tiempo < otro.tiempo


class SimuladorEventos:
    def __init__(self):
        self.cola = []
        self.tiempo_actual = 0.0
        self.manejadores = {}

    def registrar_manejador(self, tipo_evento: str, funcion):
        self.manejadores[tipo_evento] = funcion

    def agendar_evento(self, evento: Evento):
        heapq.heappush(self.cola, evento)

    def ejecutar(self, tiempo_limite: float = 100.0) -> list[str]:
        log = []
        while self.cola and self.cola[0].tiempo <= tiempo_limite:
            ev = heapq.heappop(self.cola)
            self.tiempo_actual = ev.tiempo
            if ev.tipo in self.manejadores:
                resultado = self.manejadores[ev.tipo](ev)
                log.append(f"T={ev.tiempo}: {resultado}")
        return log


if __name__ == "__main__":
    sim = SimuladorEventos()
    sim.registrar_manejador("ALARMA", lambda e: f"Alarma sonando: {e.datos.get('msg')}")
    sim.agendar_evento(Evento(5.0, "ALARMA", {"msg": "Despertar"}))
    sim.agendar_evento(Evento(2.0, "ALARMA", {"msg": "Pre-alarma"}))

    salida = sim.ejecutar()
    for l in salida: print(l)
    assert len(salida) == 2
    assert "Pre-alarma" in salida[0]
    print("\\n✅ ¡AC5 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC5
sim = SimuladorEventos()
sim.registrar_manejador("TEST", lambda e: "OK")
sim.agendar_evento(Evento(1.0, "TEST"))
res = sim.ejecutar()
assert len(res) == 1 and "OK" in res[0]
print("🎉 AC5 superada con éxito!")
'''
    },

    {
        "id": "AC6",
        "titulo": "AC6: Cliente y Servidor de Mensajería (TCP Sockets)",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Implementar un protocolo de comunicación en red sobre TCP/IP con codificación en bytes, intercambio de paquetes estructurados y manejo de conexiones.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 6: PROTOCOLO DE MENSAJERÍA TCP (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

import json

class ProtocoloMensajeria:
    """Empaqueta y desempaqueta mensajes estructurados con cabecera de tamaño fijo (4 bytes)."""

    @staticmethod
    def codificar_mensaje(tipo: str, contenido: dict) -> bytearray:
        """Crea el paquete: 4 bytes (largo del payload) + payload JSON en UTF-8."""
        payload_dict = {"tipo": tipo, "contenido": contenido}
        payload_bytes = json.dumps(payload_dict).encode("utf-8")
        largo_bytes = len(payload_bytes).to_bytes(4, byteorder="big")
        return bytearray(largo_bytes + payload_bytes)

    @staticmethod
    def decodificar_mensaje(paquete: bytearray) -> tuple[str, dict]:
        """Extrae la cabecera, verifica el largo y decodifica el payload."""
        largo = int.from_bytes(paquete[:4], byteorder="big")
        payload_str = paquete[4:4+largo].decode("utf-8")
        datos = json.loads(payload_str)
        return (datos["tipo"], datos["contenido"])


class ServidorEchoSimulado:
    """Simula el procesamiento de un servidor de chat."""
    def __init__(self):
        self.mensajes_recibidos = []

    def recibir_paquete(self, paquete: bytearray) -> bytearray:
        tipo, contenido = ProtocoloMensajeria.decodificar_mensaje(paquete)
        self.mensajes_recibidos.append((tipo, contenido))

        # Respuesta de confirmación
        return ProtocoloMensajeria.codificar_mensaje("RESPUESTA", {"status": "ACK", "echo": contenido})


if __name__ == "__main__":
    servidor = ServidorEchoSimulado()
    pkt = ProtocoloMensajeria.codificar_mensaje("CHAT", {"autor": "Nico", "msg": "Hola a todos!"})
    respuesta_pkt = servidor.recibir_paquete(pkt)
    tipo_r, datos_r = ProtocoloMensajeria.decodificar_mensaje(respuesta_pkt)

    print("Respuesta recibida:", tipo_r, datos_r)
    assert tipo_r == "RESPUESTA"
    assert datos_r["status"] == "ACK"
    print("\\n✅ ¡AC6 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC6
pkt = ProtocoloMensajeria.codificar_mensaje("LOGIN", {"user": "admin"})
tipo, cont = ProtocoloMensajeria.decodificar_mensaje(pkt)
assert tipo == "LOGIN" and cont["user"] == "admin"
print("🎉 AC6 superada con éxito!")
'''
    },

    {
        "id": "AC7",
        "titulo": "AC7: Laberinto y Algoritmos Heurísticos",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Resolver laberintos y generar estadísticas de rendimiento de búsqueda utilizando grafos, colas de prioridad y heurísticas avanzadas.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD 7: BÚSQUEDA HEURÍSTICA Y ESTADÍSTICAS (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

import heapq

def distancia_manhattan(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class BuscadorAEstrella:
    def __init__(self, mapa: list[list[int]]):
        self.mapa = mapa
        self.filas = len(mapa)
        self.cols = len(mapa[0])

    def buscar_camino(self, inicio: tuple[int, int], meta: tuple[int, int]) -> list[tuple[int, int]]:
        # Cola de prioridad: (f_score, costo_g, camino)
        frontera = [(distancia_manhattan(inicio, meta), 0, [inicio])]
        visitados = set()

        while frontera:
            f, g, camino = heapq.heappop(frontera)
            actual = camino[-1]

            if actual == meta:
                return camino

            if actual in visitados:
                continue
            visitados.add(actual)

            r, c = actual
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.filas and 0 <= nc < self.cols and self.mapa[nr][nc] == 0:
                    if (nr, nc) not in visitados:
                        nuevo_g = g + 1
                        nuevo_f = nuevo_g + distancia_manhattan((nr, nc), meta)
                        heapq.heappush(frontera, (nuevo_f, nuevo_g, camino + [(nr, nc)]))
        return []


if __name__ == "__main__":
    tablero = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    buscador = BuscadorAEstrella(tablero)
    ruta = buscador.buscar_camino((0, 0), (4, 4))
    print("Ruta óptima encontrada:", len(ruta), "pasos")
    assert len(ruta) > 0
    assert ruta[0] == (0, 0) and ruta[-1] == (4, 4)
    print("\\n✅ ¡AC7 COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado AC7
tablero = [[0, 0], [0, 0]]
b = BuscadorAEstrella(tablero)
r = b.buscar_camino((0,0), (1,1))
assert len(r) == 3
print("🎉 AC7 superada con éxito!")
'''
    },

    {
        "id": "ACBonus",
        "titulo": "AC Bonus: Wikipedia Queries & Serialización",
        "tipo": "actividad",
        "dificultad": 5,
        "descripcion": "Descarga, análisis, serialización y consultas sobre datos semiestructurados con filtros avanzados y conteo de referencias.",
        "codigo_inicial": '''# ==============================================================================
# ACTIVIDAD BONUS: WIKIPEDIA QUERIES (IIC2233)
# Formato: Un solo archivo autocontenido
# ==============================================================================

import json

SAMPLE_ARTICLES = [
    {"titulo": "Python (lenguaje)", "categoria": "Computación", "vistas": 15000, "palabras": 3200},
    {"titulo": "Ada Lovelace", "categoria": "Biografías", "vistas": 25000, "palabras": 4100},
    {"titulo": "Alan Turing", "categoria": "Biografías", "vistas": 30000, "palabras": 5000},
    {"titulo": "Algoritmo de Dijkstra", "categoria": "Computación", "vistas": 12000, "palabras": 2800},
]

class WikiAnalyzer:
    def __init__(self, articulos: list[dict]):
        self.articulos = articulos

    def filtrar_por_categoria(self, categoria: str) -> list[str]:
        return [a["titulo"] for a in self.articulos if a["categoria"] == categoria]

    def articulo_mas_visto(self) -> str:
        if not self.articulos:
            return ""
        return max(self.articulos, key=lambda a: a["vistas"])["titulo"]

    def palabras_promedio(self) -> float:
        if not self.articulos:
            return 0.0
        return sum(a["palabras"] for a in self.articulos) / len(self.articulos)


if __name__ == "__main__":
    wa = WikiAnalyzer(SAMPLE_ARTICLES)
    print("Artículos de Computación:", wa.filtrar_por_categoria("Computación"))
    print("Más visto:", wa.articulo_mas_visto())
    print("Promedio de palabras:", wa.palabras_promedio())

    assert len(wa.filtrar_por_categoria("Biografías")) == 2
    assert wa.articulo_mas_visto() == "Alan Turing"
    print("\\n✅ ¡AC BONUS COMPLETA Y CORRECTA!")
''',
        "tests_code": '''# Test automatizado ACBonus
wa = WikiAnalyzer(SAMPLE_ARTICLES)
assert wa.articulo_mas_visto() == "Alan Turing"
assert len(wa.filtrar_por_categoria("Computación")) == 2
print("🎉 AC Bonus superada con éxito!")
'''
    }
]

# ── EVALUACIONES ──
EVALUACIONES_DATA = [
    {
        "id": "I1",
        "titulo": "Interrogación 1 (I1)",
        "tipo": "evaluacion",
        "dificultad": 4,
        "descripcion": "Evaluación sumativa que cubre las Semanas 1 a 4: OOP Avanzado, Manejo de Archivos, Estructuras de Datos y Excepciones.",
        "codigo_inicial": '''# --- INTERROGACIÓN 1 ---
# Resuelve las preguntas aquí
'''
    },
    {
        "id": "I2",
        "titulo": "Interrogación 2 (I2)",
        "tipo": "evaluacion",
        "dificultad": 5,
        "descripcion": "Evaluación sumativa que cubre las Semanas 6 a 11: Iteradores, Programación Funcional, Threads, Sockets TCP y Serialización.",
        "codigo_inicial": '''# --- INTERROGACIÓN 2 ---
# Resuelve las preguntas aquí
'''
    },
    {
        "id": "Examen",
        "titulo": "Examen Final",
        "tipo": "evaluacion",
        "dificultad": 5,
        "descripcion": "Evaluación integradora de todos los contenidos del semestre IIC2233.",
        "codigo_inicial": '''# --- EXAMEN FINAL ---
# Resuelve las preguntas aquí
'''
    }
]

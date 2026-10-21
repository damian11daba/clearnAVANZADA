# ClearnP.A — Plataforma de Programación Avanzada

> Plataforma interactiva de ejercicios para el curso **IIC2233 Programación Avanzada** de la UC Chile.  
> Inspirada en [Clearn.cl](https://www.clearn.cl), adaptada para contenidos avanzados en Python.

---

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Iniciar el servidor

```bash
python run.py
```

### 3. Abrir en el navegador

```
http://localhost:5000
```

---

## 📁 Estructura del proyecto

```
clearnP.A/
├── run.py                        ← Punto de entrada
├── requirements.txt              ← Dependencias (Flask, flask-cors)
├── README.md
└── app/
    ├── __init__.py               ← Factory de Flask
    ├── routes.py                 ← API REST + renderizado HTML
    ├── templates/
    │   └── index.html            ← UI completa estilo Clearn (3 paneles)
    ├── static/
    │   ├── css/style.css         ← Estilos (verde, sidebar, editor, terminal)
    │   └── js/app.js             ← Lógica: Monaco Editor + fetch API
    ├── ejercicios/
    │   └── AC1.json              ← Ejercicio AC1 (Medallistas Olímpicos)
    └── sandbox/                  ← Ejecución aislada del código del alumno
```

---

## 🧩 Contenidos incluidos

### 📚 Materias (dificultad gradual)
| Semana | Tema |
|--------|------|
| 1-2 | Introducción y entorno de trabajo |
| 3 | Estructuras de datos (listas, dicts, sets, stacks) |
| 4 | OOP Avanzado (herencia, clases abstractas, mixins) |
| 6 | Excepciones, Iterables e Iteradores |
| 7 | Programación Funcional (map, filter, reduce, lambdas) |
| 9 | Interfaces Gráficas I (PyQt6, signals, slots) |
| 10-11 | Serialización y Networking (JSON, Pickle, Sockets) |
| 14 | Interfaces Gráficas II (modelos/vistas) |
| 15 | Tópicos Avanzados (decoradores, metaclases) |

### 🏋️ Actividades
| ID | Tema |
|----|------|
| AC1 | Tabla de Medallistas (OOP básico) |
| AC2 | Estadísticas de Premios (namedtuples, dicts) |
| AC3 | Genética (herencia, clases abstractas) |
| AC4 | Laberinto (búsqueda en grafos) |
| AC5 | Simulación de Eventos (funcional) |
| AC6 | Cliente-Servidor (sockets TCP) |
| AC7 | Laberinto Avanzado (búsqueda heurística) |
| ACBonus | Wikipedia Queries (serialización) |

### 📝 Evaluaciones
- Interrogación 1: OOP, Estructuras de Datos, Iteradores
- Interrogación 2: Funcional, Networking, GUI
- Examen Final: Todos los contenidos

---

## 🔌 API Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz principal |
| `GET` | `/api/cursos` | Lista de cursos |
| `GET` | `/api/cursos/<id>/secciones` | Secciones del curso |
| `GET` | `/api/ejercicio/<id>` | Datos del ejercicio |
| `POST` | `/api/ejecutar` | Ejecuta código Python (sandbox) |
| `POST` | `/api/test` | Corre tests públicos (pytest) |

---

## 🛡️ Sandbox de ejecución

El código enviado por el usuario se ejecuta de forma **aislada**:
1. Se crea un directorio temporal `app/sandbox/<uuid>/`
2. Se escribe el código como `main.py`
3. Se copian los archivos auxiliares del ejercicio
4. Se ejecuta con `subprocess` con **timeout de 10 segundos**
5. Se retornan stdout/stderr y se **limpia el directorio**

---

## 📦 Basado en el repositorio IIC2233-2026-1

El contenido de ejercicios está basado en el syllabus oficial del curso  
**IIC2233 Programación Avanzada — PUC Chile, 2026-1**.

# ClearnP.A — Plataforma de Programación Avanzada

> Plataforma web interactiva para el curso **IIC2233 Programación Avanzada** (Python) de la **Pontificia Universidad Católica de Chile**.  
> Inspirada en [Clearn.cl](https://www.clearn.cl), diseñada con una **escalera de aprendizaje gradual** para que los estudiantes dominen los conceptos antes de enfrentar las Actividades (AC) de alta complejidad.

---

## 🌐 Acceso Directo (GitHub Pages)

Puedes acceder a la plataforma directamente en tu navegador sin instalar nada:

🔗 **[https://damian11daba.github.io/clearnAVANZADA/](https://damian11daba.github.io/clearnAVANZADA/)**

> ⚡ **Ejecución en el Navegador con Pyodide (WebAssembly):**
> La plataforma ejecuta código Python 3.12 real directamente en tu navegador web. No requiere servidor ni backend para correr pruebas o ejercicios.

---

## 🎯 Enlaces Directos por Sección (Deep Linking)

La plataforma soporta URLs directas para saltar inmediatamente a cualquier semana, lección o actividad:

* **Inicio / Dashboard:** `https://damian11daba.github.io/clearnAVANZADA/#home`
* **Semana 1 (OOP Básico):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-01`
* **Semana 3 (Estructuras de Datos):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-03`
* **Semana 4 (OOP Avanzado):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-04`
* **Semana 6 (Excepciones e Iteradores):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-06`
* **Semana 7 (Programación Funcional):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-07`
* **Semana 9 (GUI & Threads):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-09`
* **Semana 10 y 11 (Networking & Sockets):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-10`
* **Semana 15 (Grafos & Regex):** `https://damian11daba.github.io/clearnAVANZADA/#semana/semana-15`
* **Actividad AC1 (Medallistas):** `https://damian11daba.github.io/clearnAVANZADA/#actividad/AC1`
* **Actividad AC2 (Premios & Namedtuples):** `https://damian11daba.github.io/clearnAVANZADA/#actividad/AC2`
* **Interrogación 1 (I1):** `https://damian11daba.github.io/clearnAVANZADA/#evaluacion/I1`

---

## 🪜 Escalera de Aprendizaje Gradual

Cada semana del curso está estructurada en 3 niveles progresivos:

1. 🟢 **Paso 1: Fundamentos y Conceptos (Contenidos Mínimos):**
   * Lectura interactiva de los apuntes y notebooks oficiales.
   * Botón `▶ Probar snippet` para ejecutar ejemplos teóricos en vivo.
2. 🟡 **Paso 2: Ejercicios de Calentamiento (Dificultad Progresiva):**
   * Desafíos cortos y guiados (Fácil → Medio → Avanzado).
   * Editor de código dividido (split screen) estilo Clearn.
   * Botón `🧪 Evaluar Tests` con verificación automática de aserciones.
3. 🔴 **Paso 3: Actividad Práctica Completa (AC):**
   * El desafío integrador de nivel universitario con múltiples módulos (`main.py`, `entities.py`, `utils/`).
   * Tests exhaustivos y preparación para las evaluaciones.

---

## 💻 Ejecución Local con Servidor Flask (Opcional)

Si prefieres ejecutar la plataforma de forma local en tu computadora:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Iniciar el servidor local
python run.py

# 3. Abrir en el navegador
# http://localhost:5000
```

---

## 📁 Estructura del Repositorio

```
clearnP.A/
├── index.html               ← Página principal (funciona directo en GitHub Pages)
├── run.py                   ← Servidor local Flask
├── requirements.txt         ← Dependencias de Python
├── README.md                ← Documentación y enlaces
│
├── static/                  ← Archivos CSS y JavaScript
│   ├── css/style.css        ← Estilos inspirados en Clearn.cl
│   └── js/app.js            ← Lógica de la app, Pyodide y Deep Linking
│
├── data/
│   └── curso.json           ← Base de datos de contenidos, lecciones, ACs y tests
│
├── scripts/
│   └── build_data.py        ← Compilador de notebooks a curso.json
│
└── app/                     ← Módulo backend Flask (para modo servidor)
    ├── __init__.py
    ├── routes.py
    ├── templates/
    └── static/
```

---

## 🎓 Créditos
* Basado en el material docente del curso **IIC2233 Programación Avanzada** de la Pontificia Universidad Católica de Chile.
* Interfaz y metodología inspiradas en la plataforma **Clearn.cl**.

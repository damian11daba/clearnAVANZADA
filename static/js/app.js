/* ════════════════════════════════════════════════════════════════════
   ClearnP.A — app.js Oficial
   Motor Interactivo WebAssembly (Pyodide) + Deep Linking + Escalera Gradual
════════════════════════════════════════════════════════════════════ */

// Estado global de la aplicación
const App = {
  cursoData: null,
  pyodide: null,
  pyodideCargando: false,
  vistaActual: 'home',
  semanaActual: null,
  leccionActual: null,
  ejercicioActual: null,
  archivosActivos: {},
  archivoActual: 'main.py',
  codigoOriginal: '',
  testsActuales: null,
  tipoActual: 'ejercicio' // 'ejercicio', 'actividad', 'evaluacion'
};

// ── 1. INICIALIZACIÓN ──
document.addEventListener('DOMContentLoaded', async () => {
  // Manejo de teclado en el editor (Tab indentation & Ctrl+Enter)
  configurarEditorTextarea();

  // Iniciar carga de Pyodide en segundo plano
  iniciarPyodide();

  // Cargar datos del curso
  await cargarDatosCurso();

  // Escuchar cambios de Hash en la URL para deep-linking
  window.addEventListener('hashchange', procesarRutaHash);

  // Procesar ruta inicial
  procesarRutaHash();
});

// ── 2. MOTOR PYODIDE (PYTHON EN EL NAVEGADOR) ──
async function iniciarPyodide() {
  const statusEl = document.getElementById('pyodide-status');
  const dotEl = statusEl?.querySelector('.status-dot');
  const textEl = document.getElementById('status-text');

  if (typeof loadPyodide === 'undefined') {
    if (textEl) textEl.textContent = 'Modo Flask';
    return;
  }

  try {
    App.pyodideCargando = true;
    if (textEl) textEl.textContent = 'Cargando Python...';
    
    App.pyodide = await loadPyodide();
    
    App.pyodideCargando = false;
    if (dotEl) dotEl.classList.add('ready');
    if (textEl) textEl.textContent = 'Python 3.12 Listo ✓';
  } catch (err) {
    console.warn('Pyodide no pudo inicializar, usando backend:', err);
    if (textEl) textEl.textContent = 'Modo Servidor';
  }
}

// ── 3. CARGA DE DATOS ──
async function cargarDatosCurso() {
  // Intentar cargar curso.json desde static/data/ o data/
  const rutas = ['data/curso.json', 'static/data/curso.json', '/api/curso'];
  for (const r of rutas) {
    try {
      const res = await fetch(r);
      if (res.ok) {
        App.cursoData = await res.json();
        break;
      }
    } catch (e) {
      // Intentar siguiente
    }
  }

  if (!App.cursoData) {
    console.error('No se pudo cargar el curso.json');
    return;
  }

  renderizarSidebar();
  renderizarHomeGrid();
}

// ── 4. ENRUTAMIENTO Y DEEP LINKING (HASH) ──
function navigateTo(destino, params = {}) {
  let hash = '';
  if (destino === 'home') hash = '#home';
  else if (destino === 'semana') hash = `#semana/${params.semanaId}`;
  else if (destino === 'leccion') hash = `#semana/${params.semanaId}/leccion/${params.leccionId}`;
  else if (destino === 'ejercicio') hash = `#semana/${params.semanaId}/ejercicio/${params.ejercicioId}`;
  else if (destino === 'actividad') hash = `#actividad/${params.actividadId}`;
  else if (destino === 'evaluacion') hash = `#evaluacion/${params.evalId}`;

  window.location.hash = hash;
}

function procesarRutaHash() {
  const hash = window.location.hash.replace(/^#/, '').trim();
  if (!hash || hash === 'home') {
    mostrarVista('home');
    actualizarBreadcrumb('Inicio');
    return;
  }

  const partes = hash.split('/');
  const seccion = partes[0];

  if (seccion === 'semana') {
    const semanaId = partes[1];
    if (partes.length === 2) {
      abrirSemana(semanaId);
    } else if (partes[2] === 'leccion') {
      abrirLeccion(semanaId, partes[3]);
    } else if (partes[2] === 'ejercicio') {
      abrirEjercicioGuiado(semanaId, partes[3]);
    }
  } else if (seccion === 'actividad') {
    abrirActividad(partes[1]);
  } else if (seccion === 'evaluacion') {
    abrirEvaluacion(partes[1]);
  }
}

function mostrarVista(vistaId) {
  document.querySelectorAll('.view').forEach(v => {
    v.classList.remove('active');
    v.classList.add('hidden');
  });

  const target = document.getElementById(`view-${vistaId}`);
  if (target) {
    target.classList.remove('hidden');
    target.classList.add('active');
  }
  App.vistaActual = vistaId;
}

function actualizarBreadcrumb(seccion, item = null) {
  document.getElementById('bc-seccion').textContent = seccion;
  const itemEl = document.getElementById('bc-item');
  const sepEl = document.querySelector('.bc-sep-item');
  if (item) {
    itemEl.textContent = item;
    itemEl.classList.remove('hidden');
    sepEl?.classList.remove('hidden');
  } else {
    itemEl.classList.add('hidden');
    sepEl?.classList.add('hidden');
  }
}

// ── 5. RENDERIZADO DEL SIDEBAR ──
function renderizarSidebar() {
  if (!App.cursoData) return;

  // 1. Materias / Semanas
  const secMaterias = document.getElementById('sec-materias');
  secMaterias.innerHTML = '';
  App.cursoData.semanas?.forEach(s => {
    const li = document.createElement('li');
    li.className = 'sidebar-item';
    li.dataset.id = s.id;
    li.innerHTML = `
      <span class="sidebar-item-label">${s.nombre}</span>
      <span class="dif-pill d${s.dificultad}">Niv ${s.dificultad}</span>
    `;
    li.onclick = () => navigateTo('semana', { semanaId: s.id });
    secMaterias.appendChild(li);
  });

  // 2. Actividades (AC)
  const secAct = document.getElementById('sec-actividades');
  secAct.innerHTML = '';
  App.cursoData.actividades?.forEach(a => {
    const li = document.createElement('li');
    li.className = 'sidebar-item';
    li.dataset.id = a.id;
    li.innerHTML = `
      <span class="sidebar-item-label">${a.titulo.split(':')[0]}</span>
      <span class="dif-pill d${a.dificultad}">Desafío</span>
    `;
    li.onclick = () => navigateTo('actividad', { actividadId: a.id });
    secAct.appendChild(li);
  });

  // 3. Evaluaciones
  const secEval = document.getElementById('sec-evaluaciones');
  secEval.innerHTML = '';
  App.cursoData.evaluaciones?.forEach(e => {
    const li = document.createElement('li');
    li.className = 'sidebar-item';
    li.dataset.id = e.id;
    li.innerHTML = `
      <span class="sidebar-item-label">${e.titulo}</span>
      <span class="dif-pill d${e.dificultad}">Evaluado</span>
    `;
    li.onclick = () => navigateTo('evaluacion', { evalId: e.id });
    secEval.appendChild(li);
  });
}

function filtrarSidebar(texto) {
  const query = texto.toLowerCase();
  document.querySelectorAll('.sidebar-item').forEach(el => {
    const label = el.querySelector('.sidebar-item-label')?.textContent.toLowerCase() || '';
    el.style.display = label.includes(query) ? 'flex' : 'none';
  });
}

function toggleSeccion(id) {
  const ul = document.getElementById(id);
  const arrow = document.getElementById(`arrow-${id}`);
  const isOpen = ul.dataset.open === 'true';
  ul.dataset.open = isOpen ? 'false' : 'true';
  ul.classList.toggle('collapsed', isOpen);
  arrow?.classList.toggle('collapsed', isOpen);
}

// ── 6. VISTA HOME / DASHBOARD ──
function renderizarHomeGrid() {
  const grid = document.getElementById('home-semanas-grid');
  if (!grid || !App.cursoData?.semanas) return;

  grid.innerHTML = '';
  App.cursoData.semanas.forEach(s => {
    const card = document.createElement('div');
    card.className = 'semana-card';
    card.onclick = () => navigateTo('semana', { semanaId: s.id });
    card.innerHTML = `
      <div class="semana-card-top">
        <span class="semana-card-num">${s.id.replace('semana-', 'Semana ')}</span>
        <span class="dif-badge d${s.dificultad}">Nivel ${s.dificultad}</span>
      </div>
      <h3 class="semana-card-title">${s.nombre.replace(/^Semana \d+:\s*/, '')}</h3>
      <p class="semana-card-desc">${s.descripcion}</p>
      <div class="semana-card-footer">
        <span>📖 ${s.lecciones?.length || 0} lecciones · 🟡 ${s.ejercicios_guiados?.length || 0} calentamiento</span>
        <span class="btn-card-go">Explorar →</span>
      </div>
    `;
    grid.appendChild(card);
  });
}

// ── 7. VISTA DETALLADA DE LA SEMANA (LA ESCALERA GRADUAL) ──
function abrirSemana(semanaId) {
  const semana = App.cursoData?.semanas?.find(s => s.id === semanaId);
  if (!semana) return;

  App.semanaActual = semana;
  mostrarVista('semana');
  actualizarBreadcrumb('Materias', semana.nombre);

  // Actualizar sidebar activo
  resaltarSidebar(semanaId);

  // Banner
  const badgeEl = document.getElementById('semana-badge-dif');
  badgeEl.className = `semana-badge-dif dif-badge d${semana.dificultad}`;
  badgeEl.textContent = `Nivel de Dificultad ${semana.dificultad} / 5`;

  document.getElementById('semana-titulo').textContent = semana.nombre;
  document.getElementById('semana-desc').textContent = semana.descripcion;

  // Paso 1: Cuadernos de Teoría
  const listTeoria = document.getElementById('ladder-teoria-list');
  listTeoria.innerHTML = '';
  if (semana.lecciones?.length) {
    semana.lecciones.forEach((l, idx) => {
      const item = document.createElement('div');
      item.className = 'ladder-item';
      item.onclick = () => navigateTo('leccion', { semanaId: semana.id, leccionId: l.id });
      item.innerHTML = `
        <div class="ladder-item-info">
          <h4>📖 1.${idx + 1} ${l.titulo}</h4>
          <p>Apunte interactivo de contenidos mínimos y ejemplos de código</p>
        </div>
        <button class="btn-open-item">Leer y Probar →</button>
      `;
      listTeoria.appendChild(item);
    });
  } else {
    listTeoria.innerHTML = '<p style="padding:10px;color:var(--text-muted)">No hay lecciones registradas para esta semana.</p>';
  }

  // Paso 2: Ejercicios de Calentamiento Guiados
  const listEj = document.getElementById('ladder-ejercicios-list');
  listEj.innerHTML = '';
  if (semana.ejercicios_guiados?.length) {
    semana.ejercicios_guiados.forEach((ej, idx) => {
      const item = document.createElement('div');
      item.className = 'ladder-item';
      item.onclick = () => navigateTo('ejercicio', { semanaId: semana.id, ejercicioId: ej.id });
      item.innerHTML = `
        <div class="ladder-item-info">
          <h4>🟡 Paso 2.${idx + 1}: ${ej.titulo}</h4>
          <p>${ej.objetivo} · Dificultad: <strong>${ej.nivel}</strong></p>
        </div>
        <button class="btn-open-item">Resolver Ejercicio →</button>
      `;
      listEj.appendChild(item);
    });
  } else {
    listEj.innerHTML = '<p style="padding:10px;color:var(--text-muted)">Semana teórica o preparatoria para la AC.</p>';
  }

  // Paso 3: Actividad Práctica (AC)
  const actBox = document.getElementById('ladder-actividad-box');
  actBox.innerHTML = '';
  if (semana.actividad_id) {
    const ac = App.cursoData?.actividades?.find(a => a.id === semana.actividad_id);
    if (ac) {
      const item = document.createElement('div');
      item.className = 'ladder-item';
      item.style.borderLeft = '4px solid var(--accent-red)';
      item.onclick = () => navigateTo('actividad', { actividadId: ac.id });
      item.innerHTML = `
        <div class="ladder-item-info">
          <h4>🔴 Paso 3: ${ac.titulo}</h4>
          <p>${ac.descripcion}</p>
        </div>
        <button class="btn-open-item" style="border-color:var(--accent-red);color:var(--accent-red)">Entrar al Desafío (AC) →</button>
      `;
      actBox.appendChild(item);
    }
  } else {
    actBox.innerHTML = '<p style="padding:10px;color:var(--text-muted)">Esta semana no tiene una Actividad calificada directa asociada (continúa a la siguiente).</p>';
  }
}

function volverASemana() {
  if (App.semanaActual) {
    navigateTo('semana', { semanaId: App.semanaActual.id });
  } else {
    navigateTo('home');
  }
}

// ── 8. VISTA DE LECCIÓN DE TEORÍA ──
function abrirLeccion(semanaId, leccionId) {
  const semana = App.cursoData?.semanas?.find(s => s.id === semanaId);
  if (!semana) return;
  const leccion = semana.lecciones?.find(l => l.id === leccionId);
  if (!leccion) return;

  App.semanaActual = semana;
  App.leccionActual = leccion;

  mostrarVista('leccion');
  actualizarBreadcrumb(semana.nombre, leccion.titulo);
  resaltarSidebar(semanaId);

  document.getElementById('leccion-crumb').textContent = `${semana.nombre} › Lección`;
  document.getElementById('leccion-header-title').textContent = leccion.titulo;

  const container = document.getElementById('leccion-container');
  container.innerHTML = '';

  if (!leccion.bloques || !leccion.bloques.length) {
    container.innerHTML = '<p>Contenido en proceso de digitalización.</p>';
    return;
  }

  leccion.bloques.forEach((b, i) => {
    if (b.tipo === 'teoria') {
      const div = document.createElement('div');
      div.className = 'teoria-block';
      div.innerHTML = (typeof marked !== 'undefined') ? marked.parse(b.contenido) : b.contenido;
      container.appendChild(div);
    } else if (b.tipo === 'codigo') {
      const box = document.createElement('div');
      box.className = 'code-snippet-box';
      const cleanCode = b.contenido.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      box.innerHTML = `
        <div class="code-snippet-header">
          <span>Python 3.12 (Ejemplo Interactivo)</span>
          <button class="btn-snippet-run" onclick="ejecutarSnippetInline(this, ${JSON.stringify(b.contenido)})">▶ Probar snippet</button>
        </div>
        <pre class="code-snippet-body"><code>${cleanCode}</code></pre>
        ${b.output ? `<div class="code-snippet-output"><strong>Salida esperada:</strong>\n${b.output}</div>` : ''}
        <div class="snippet-runtime-output" style="display:none;padding:8px 12px;background:#030712;color:#38bdf8;font-family:var(--font-mono);font-size:0.75rem;border-top:1px solid #1f2937"></div>
      `;
      container.appendChild(box);
    }
  });

  // Resaltar sintaxis de código
  if (typeof hljs !== 'undefined') {
    container.querySelectorAll('pre code').forEach(el => hljs.highlightElement(el));
  }
}

async function ejecutarSnippetInline(btn, codigo) {
  const box = btn.closest('.code-snippet-box');
  const outEl = box.querySelector('.snippet-runtime-output');
  outEl.style.display = 'block';
  outEl.textContent = '⏳ Ejecutando en Python WebAssembly...';

  const res = await correrPython(codigo);
  if (res.exitcode === 0) {
    outEl.style.color = '#34d399';
    outEl.textContent = '✅ Salida:\n' + (res.stdout || '(Ejecutado sin salida por consola)');
  } else {
    outEl.style.color = '#f87171';
    outEl.textContent = '❌ Error:\n' + (res.stderr || 'Error desconocido');
  }
}

function cambiarLeccion(dir) {
  if (!App.semanaActual || !App.leccionActual) return;
  const lecciones = App.semanaActual.lecciones || [];
  const idx = lecciones.findIndex(l => l.id === App.leccionActual.id);
  const targetIdx = idx + dir;

  if (targetIdx >= 0 && targetIdx < lecciones.length) {
    navigateTo('leccion', { semanaId: App.semanaActual.id, leccionId: lecciones[targetIdx].id });
  } else if (targetIdx >= lecciones.length) {
    // Si terminó las lecciones, llevar al calentamiento
    if (App.semanaActual.ejercicios_guiados?.length) {
      navigateTo('ejercicio', { semanaId: App.semanaActual.id, ejercicioId: App.semanaActual.ejercicios_guiados[0].id });
    } else {
      volverASemana();
    }
  } else {
    volverASemana();
  }
}

// ── 9. VISTA SPLIT: EJERCICIO GUIADO (CALENTAMIENTO) ──
function abrirEjercicioGuiado(semanaId, ejercicioId) {
  const semana = App.cursoData?.semanas?.find(s => s.id === semanaId);
  if (!semana) return;
  const ej = semana.ejercicios_guiados?.find(e => e.id === ejercicioId);
  if (!ej) return;

  App.semanaActual = semana;
  App.ejercicioActual = ej;
  App.tipoActual = 'ejercicio';

  mostrarVista('ejercicio');
  actualizarBreadcrumb(semana.nombre, ej.titulo);
  resaltarSidebar(semanaId);

  // Tab bar de ejercicios de la semana
  const tabs = document.getElementById('preguntas-tab-bar');
  tabs.innerHTML = '';
  semana.ejercicios_guiados.forEach((e, idx) => {
    const btn = document.createElement('button');
    btn.className = `tab-pregunta ${e.id === ej.id ? 'active' : ''}`;
    btn.textContent = `Ejercicio ${idx + 1}`;
    btn.onclick = () => navigateTo('ejercicio', { semanaId: semana.id, ejercicioId: e.id });
    tabs.appendChild(btn);
  });

  // Enunciado
  const badgeEl = document.getElementById('enunciado-tipo-badge');
  badgeEl.className = 'enunciado-tipo-badge dif-badge d2';
  badgeEl.textContent = `Calentamiento · ${ej.nivel}`;

  document.getElementById('enunciado-title').textContent = ej.titulo;
  document.getElementById('enunciado-subtitle').textContent = ej.objetivo;

  const bodyEl = document.getElementById('enunciado-body');
  bodyEl.innerHTML = `
    <h3>Descripción del Problema</h3>
    <p>${ej.descripcion}</p>
    <h3>Instrucciones</h3>
    <p>1. Completa el código en el editor de la derecha.<br>
       2. Presiona <strong>▶ Ejecutar Código</strong> para probar tu solución.<br>
       3. Presiona <strong>🧪 Evaluar Tests</strong> para verificar automáticamente si pasa todos los casos de prueba.</p>
  `;

  // Editor
  configurarWorkspaceArchivos({
    'main.py': ej.codigo_inicial
  }, ej.tests_code);
}

// ── 10. VISTA SPLIT: ACTIVIDAD PRÁCTICA (AC) ──
function abrirActividad(actividadId) {
  const ac = App.cursoData?.actividades?.find(a => a.id === actividadId);
  if (!ac) return;

  App.ejercicioActual = ac;
  App.tipoActual = 'actividad';

  mostrarVista('ejercicio');
  actualizarBreadcrumb('Actividades', ac.titulo.split(':')[0]);
  resaltarSidebar(actividadId);

  // Tabs de preguntas / módulos de la AC
  const tabs = document.getElementById('preguntas-tab-bar');
  tabs.innerHTML = '';
  const btn = document.createElement('button');
  btn.className = 'tab-pregunta active';
  btn.textContent = ac.id;
  tabs.appendChild(btn);

  // Enunciado
  const badgeEl = document.getElementById('enunciado-tipo-badge');
  badgeEl.className = 'enunciado-tipo-badge dif-badge d4';
  badgeEl.textContent = `Actividad Práctica Evaluada`;

  document.getElementById('enunciado-title').textContent = ac.titulo;
  document.getElementById('enunciado-subtitle').textContent = 'IIC2233 Programación Avanzada · Desafío Oficial';

  const bodyEl = document.getElementById('enunciado-body');
  bodyEl.innerHTML = `
    <h3>Objetivo de la Actividad</h3>
    <p>${ac.descripcion}</p>
    <h3>Archivos Proporcionados</h3>
    <p>Revisa las pestañas superiores del editor. Puedes explorar los módulos de apoyo (como <code>entities.py</code> o <code>utils/</code>) y completar la solución en el archivo principal.</p>
  `;

  // Configurar archivos en workspace
  const archivos = ac.archivos && Object.keys(ac.archivos).length > 0 
    ? ac.archivos 
    : { 'main.py': ac.codigo_inicial || '# Desarrolla tu solución aquí\n' };

  configurarWorkspaceArchivos(archivos, null);
}

// ── 11. VISTA SPLIT: EVALUACIÓN (INTERROGACIÓN / EXAMEN) ──
function abrirEvaluacion(evalId) {
  const ev = App.cursoData?.evaluaciones?.find(e => e.id === evalId);
  if (!ev) return;

  App.ejercicioActual = ev;
  App.tipoActual = 'evaluacion';

  mostrarVista('ejercicio');
  actualizarBreadcrumb('Evaluaciones', ev.titulo);
  resaltarSidebar(evalId);

  // Tabs de preguntas
  const tabs = document.getElementById('preguntas-tab-bar');
  tabs.innerHTML = '';
  const preguntas = ev.preguntas || [];
  preguntas.forEach((p, idx) => {
    const btn = document.createElement('button');
    btn.className = `tab-pregunta ${idx === 0 ? 'active' : ''}`;
    btn.textContent = `Pregunta ${idx + 1}`;
    btn.onclick = () => {
      document.querySelectorAll('.tab-pregunta').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      cargarPreguntaEvaluacion(p);
    };
    tabs.appendChild(btn);
  });

  if (preguntas.length > 0) {
    cargarPreguntaEvaluacion(preguntas[0]);
  }
}

function cargarPreguntaEvaluacion(p) {
  const badgeEl = document.getElementById('enunciado-tipo-badge');
  badgeEl.className = 'enunciado-tipo-badge dif-badge d5';
  badgeEl.textContent = 'Pregunta de Examen / Interrogación';

  document.getElementById('enunciado-title').textContent = p.titulo;
  document.getElementById('enunciado-subtitle').textContent = 'Puntaje de evaluación escrita/práctica';

  const bodyEl = document.getElementById('enunciado-body');
  bodyEl.innerHTML = `
    <h3>Enunciado</h3>
    <p>${p.descripcion}</p>
  `;

  configurarWorkspaceArchivos({
    'solucion.py': p.codigo_inicial || '# Desarrolla tu respuesta aquí\n'
  }, null);
}

// ── 12. CONFIGURACIÓN DEL WORKSPACE DEL EDITOR ──
function configurarWorkspaceArchivos(archivos, testsCode = null) {
  App.archivosActivos = { ...archivos };
  App.testsActuales = testsCode;

  // Renderizar pestañas de archivos
  const tabsBar = document.getElementById('editor-tabs-bar');
  tabsBar.innerHTML = '';

  const nombres = Object.keys(archivos);
  App.archivoActual = nombres.includes('main.py') ? 'main.py' : nombres[0];

  nombres.forEach(nombre => {
    const tab = document.createElement('div');
    tab.className = `editor-tab ${nombre === App.archivoActual ? 'active' : ''}`;
    tab.textContent = nombre;
    tab.onclick = () => cambiarPestañaArchivo(nombre);
    tabsBar.appendChild(tab);
  });

  // Asignar código al textarea
  const textarea = document.getElementById('code-editor');
  textarea.value = App.archivosActivos[App.archivoActual] || '';
  App.codigoOriginal = textarea.value;

  limpiarConsola();
}

function cambiarPestañaArchivo(nombre) {
  const textarea = document.getElementById('code-editor');
  // Guardar archivo anterior
  if (App.archivoActual) {
    App.archivosActivos[App.archivoActual] = textarea.value;
  }

  App.archivoActual = nombre;
  document.querySelectorAll('.editor-tab').forEach(t => {
    t.classList.toggle('active', t.textContent === nombre);
  });

  textarea.value = App.archivosActivos[nombre] || '';
}

function configurarEditorTextarea() {
  const textarea = document.getElementById('code-editor');
  if (!textarea) return;

  textarea.addEventListener('keydown', (e) => {
    // Tabulación inteligente (4 espacios)
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = textarea.selectionStart;
      const end = textarea.selectionEnd;
      textarea.value = textarea.value.substring(0, start) + '    ' + textarea.value.substring(end);
      textarea.selectionStart = textarea.selectionEnd = start + 4;
    }
    // Ctrl + Enter para ejecutar
    if (e.ctrlKey && e.key === 'Enter') {
      e.preventDefault();
      ejecutarCodigoUsuario();
    }
  });
}

// ── 13. EJECUCIÓN Y EVALUACIÓN DE CÓDIGO ──
async function correrPython(codigo, archivosVirtuales = {}) {
  // 1. Si Pyodide está disponible en WebAssembly:
  if (App.pyodide) {
    let stdout = '';
    let stderr = '';
    
    // Escribir archivos auxiliares en el sistema de archivos virtual de Pyodide
    for (const [fname, cont] of Object.entries(archivosVirtuales)) {
      try {
        const partes = fname.split('/');
        if (partes.length > 1) {
          const dir = partes.slice(0, -1).join('/');
          App.pyodide.FS.mkdirTree(dir);
        }
        App.pyodide.FS.writeFile(fname, cont);
      } catch (e) {
        // Ignorar si ya existe
      }
    }

    App.pyodide.setStdout({ batched: (msg) => stdout += msg + '\n' });
    App.pyodide.setStderr({ batched: (msg) => stderr += msg + '\n' });

    try {
      await App.pyodide.runPythonAsync(codigo);
      return { stdout: stdout.trim(), stderr: stderr.trim(), exitcode: 0 };
    } catch (err) {
      return { stdout: stdout.trim(), stderr: err.message, exitcode: 1 };
    }
  }

  // 2. Si no hay Pyodide, intentar el endpoint de backend Flask
  try {
    const res = await fetch('/api/ejecutar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        codigo: codigo,
        archivos: archivosVirtuales
      })
    });
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    // Sin servidor disponible
  }

  return {
    stdout: '',
    stderr: 'El motor Python está inicializándose en tu navegador. Espera unos segundos y vuelve a presionar Ejecutar.',
    exitcode: 1
  };
}

async function ejecutarCodigoUsuario() {
  const textarea = document.getElementById('code-editor');
  App.archivosActivos[App.archivoActual] = textarea.value;

  const codigo = App.archivosActivos[App.archivoActual];
  const outEl = document.getElementById('console-output');
  const badgeEl = document.getElementById('console-status-badge');

  badgeEl.textContent = 'Ejecutando...';
  badgeEl.style.color = '#f59e0b';
  outEl.className = 'console-output';
  outEl.textContent = '⏳ Ejecutando código en Python...\n';

  const res = await correrPython(codigo, App.archivosActivos);

  if (res.exitcode === 0) {
    badgeEl.textContent = 'Éxito';
    badgeEl.style.color = '#10b981';
    outEl.className = 'console-output success';
    outEl.textContent = res.stdout ? res.stdout : '(El código se ejecutó exitosamente sin salida de texto)';
    if (res.stderr) {
      outEl.textContent += '\n\n⚠️ Advertencias:\n' + res.stderr;
    }
  } else {
    badgeEl.textContent = 'Error';
    badgeEl.style.color = '#ef4444';
    outEl.className = 'console-output error';
    outEl.textContent = (res.stdout ? res.stdout + '\n\n' : '') + '❌ Error durante la ejecución:\n' + res.stderr;
  }
}

async function probarTestsUsuario() {
  const textarea = document.getElementById('code-editor');
  App.archivosActivos[App.archivoActual] = textarea.value;

  const outEl = document.getElementById('console-output');
  const badgeEl = document.getElementById('console-status-badge');

  if (!App.testsActuales) {
    badgeEl.textContent = 'Sin tests';
    badgeEl.style.color = '#38bdf8';
    outEl.className = 'console-output';
    outEl.textContent = 'ℹ️ Esta actividad utiliza los tests públicos de su archivo correspondiente o verificación manual.';
    return;
  }

  badgeEl.textContent = 'Evaluando...';
  badgeEl.style.color = '#f59e0b';
  outEl.className = 'console-output';
  outEl.textContent = '🧪 Ejecutando casos de prueba automáticos...\n';

  // Combinar el código del usuario con los tests
  const codigoCompleto = App.archivosActivos[App.archivoActual] + '\n\n# --- CASOS DE PRUEBA AUTOMÁTICOS ---\n' + App.testsActuales;
  const res = await correrPython(codigoCompleto, App.archivosActivos);

  if (res.exitcode === 0) {
    badgeEl.textContent = 'Aprobado ✓';
    badgeEl.style.color = '#10b981';
    outEl.className = 'console-output success';
    outEl.textContent = '🎉 ¡FELICITACIONES! Tu código pasó todos los tests automáticos.\n\n' + (res.stdout || '');
  } else {
    badgeEl.textContent = 'Falló ✕';
    badgeEl.style.color = '#ef4444';
    outEl.className = 'console-output error';
    outEl.textContent = '❌ Algún test o aserción no pasó:\n\n' + res.stderr + '\n\n💡 Revisa el enunciado y los tipos de datos devueltos.';
  }
}

function reiniciarCodigoUsuario() {
  const textarea = document.getElementById('code-editor');
  textarea.value = App.codigoOriginal;
  App.archivosActivos[App.archivoActual] = App.codigoOriginal;
  limpiarConsola();
}

function limpiarConsola() {
  const outEl = document.getElementById('console-output');
  const badgeEl = document.getElementById('console-status-badge');
  outEl.className = 'console-output';
  outEl.textContent = 'Consola lista. Escribe tu código y presiona Ejecutar.';
  badgeEl.textContent = 'Listo';
  badgeEl.style.color = '#38bdf8';
}

function resaltarSidebar(id) {
  document.querySelectorAll('.sidebar-item').forEach(el => {
    el.classList.toggle('active', el.dataset.id === id);
  });
}

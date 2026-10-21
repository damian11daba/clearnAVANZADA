/**
 * ClearnP.A — Application Logic
 * Vanilla JS (ES2022+), async/await, no frameworks
 */

/* ══════════════════════════════════════════════════
   STATE
══════════════════════════════════════════════════ */
const state = {
  currentEjercicioId: null,
  initialCode: {},       // { filename: code }  — per-file initial code
  fileCode: {},          // { filename: code }  — per-file current edits
  activeFile: 'code.py',
  monacoEditor: null,
  ejercicios: [],
};

/* ══════════════════════════════════════════════════
   DOM SHORTCUTS
══════════════════════════════════════════════════ */
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

const el = {
  questionList:    $('#question-list'),
  sidebarCount:    $('#sidebar-count'),
  breadcrumbCurr:  $('#breadcrumb-current'),
  emptyState:      $('#empty-state'),
  enunciado:       $('#enunciado'),
  ejBadge:         $('#ej-badge'),
  ejTitle:         $('#ej-title'),
  ejObjetivo:      $('#ej-objetivo'),
  ejDescripcion:   $('#ej-descripcion'),
  ejEjemplosSection: $('#ej-ejemplos-section'),
  ejEjemplos:      $('#ej-ejemplos'),
  ejExplicacionSection: $('#ej-explicacion-section'),
  ejExplicacion:   $('#ej-explicacion'),
  editorTabs:      $('#editor-tabs'),
  editorContainer: $('#editor-container'),
  btnEjecutar:     $('#btn-ejecutar'),
  btnLimpiar:      $('#btn-limpiar'),
  btnEntregar:     $('#btn-entregar'),
  btnRevisar:      $('#btn-revisar'),
  editorStatus:    $('#editor-status'),
  resultsPanel:    $('#results-panel'),
  resultsToggle:   $('#results-toggle'),
  resultsBody:     $('#results-body'),
  resultsChevron:  $('#results-chevron'),
  resultsOutput:   $('#results-output'),
};

/* ══════════════════════════════════════════════════
   MONACO EDITOR BOOTSTRAP
══════════════════════════════════════════════════ */
function initMonaco() {
  return new Promise((resolve) => {
    require.config({
      paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs' },
    });

    require(['vs/editor/editor.main'], () => {
      const editor = monaco.editor.create(el.editorContainer, {
        value:             '# Selecciona un ejercicio para comenzar\n',
        language:          'python',
        theme:             'vs-dark',
        fontSize:          14,
        fontFamily:        "'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace",
        fontLigatures:     true,
        lineNumbers:       'on',
        minimap:           { enabled: false },
        scrollBeyondLastLine: false,
        tabSize:           4,
        wordWrap:          'on',
        automaticLayout:   true,
        padding:           { top: 12, bottom: 12 },
        renderLineHighlight: 'line',
        smoothScrolling:   true,
      });

      state.monacoEditor = editor;

      // Ctrl+Enter → ejecutar
      editor.addCommand(
        monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter,
        () => el.btnEjecutar.click()
      );

      // Track edits per-file
      editor.onDidChangeModelContent(() => {
        state.fileCode[state.activeFile] = editor.getValue();
      });

      resolve(editor);
    });
  });
}

/* ══════════════════════════════════════════════════
   SIMPLE MARKDOWN RENDERER
  Converts a subset of Markdown to HTML:
    **bold**, `code`, - list items, \n\n paragraphs
══════════════════════════════════════════════════ */
function renderMarkdown(text) {
  if (!text) return '';

  // Escape HTML first
  const escape = (s) =>
    s.replace(/&/g, '&amp;')
     .replace(/</g, '&lt;')
     .replace(/>/g, '&gt;');

  text = escape(text);

  // Inline code  `code`
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  // Bold  **text**
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  // Italic  *text*
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');

  // Lists: lines starting with "- "
  const lines = text.split('\n');
  const out = [];
  let inList = false;

  for (const line of lines) {
    const listMatch = line.match(/^[-*]\s+(.*)$/);
    if (listMatch) {
      if (!inList) { out.push('<ul>'); inList = true; }
      out.push(`<li>${listMatch[1]}</li>`);
    } else {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(line);
    }
  }
  if (inList) out.push('</ul>');

  // Paragraphs (double newline)
  return out
    .join('\n')
    .split(/\n{2,}/)
    .map((p) => {
      p = p.trim();
      if (!p) return '';
      // Don't wrap block-level elements
      if (/^<(ul|ol|li|h[1-6]|pre|blockquote)/.test(p)) return p;
      return `<p>${p.replace(/\n/g, '<br>')}</p>`;
    })
    .join('\n');
}

/* ══════════════════════════════════════════════════
   BADGE HELPER
══════════════════════════════════════════════════ */
const BADGE_CLASS = {
  actividad:  'badge--actividad',
  materia:    'badge--materia',
  evaluacion: 'badge--evaluacion',
  tarea:      'badge--tarea',
};

function setBadge(tipo = 'actividad') {
  const key = tipo.toLowerCase();
  el.ejBadge.className = `badge ${BADGE_CLASS[key] || 'badge--actividad'}`;
  el.ejBadge.textContent = tipo.charAt(0).toUpperCase() + tipo.slice(1);
}

/* ══════════════════════════════════════════════════
   EXAMPLE BLOCKS (Input / Output)
══════════════════════════════════════════════════ */
function buildExampleBlock(label, content, variant) {
  const block = document.createElement('div');
  block.className = `example-block example-block--${variant}`;

  const header = document.createElement('div');
  header.className = 'example-block__header';

  const lbl = document.createElement('span');
  lbl.className = `example-block__label example-block__label--${variant}`;
  lbl.textContent = label;

  const copyBtn = document.createElement('button');
  copyBtn.className = 'example-block__copy';
  copyBtn.textContent = '📋 Copiar';
  copyBtn.addEventListener('click', () => copyToClipboard(content, copyBtn));

  header.appendChild(lbl);
  header.appendChild(copyBtn);

  const code = document.createElement('pre');
  code.className = 'example-block__code';
  code.textContent = content;

  block.appendChild(header);
  block.appendChild(code);
  return block;
}

async function copyToClipboard(text, btn) {
  try {
    await navigator.clipboard.writeText(text);
    btn.textContent = '✅ Copiado';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 Copiar';
      btn.classList.remove('copied');
    }, 1800);
  } catch {
    // Fallback for older browsers / non-HTTPS
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.cssText = 'position:fixed;opacity:0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    ta.remove();
    btn.textContent = '✅ Copiado';
    setTimeout(() => { btn.textContent = '📋 Copiar'; }, 1800);
  }
}

/* ══════════════════════════════════════════════════
   RENDER EXERCISE
══════════════════════════════════════════════════ */
function renderEjercicio(data) {
  // Header
  setBadge(data.tipo || 'actividad');
  el.ejTitle.textContent       = data.titulo || data.nombre || '(Sin título)';
  el.ejObjetivo.textContent    = data.objetivo || '';
  el.ejDescripcion.innerHTML   = renderMarkdown(data.descripcion || '');
  el.breadcrumbCurr.textContent = data.nombre_corto || data.id;

  // Examples
  el.ejEjemplos.innerHTML = '';
  const ejemplos = data.ejemplos || [];
  if (ejemplos.length > 0) {
    ejemplos.forEach((ej, i) => {
      const wrap = document.createElement('div');
      wrap.style.marginBottom = '1rem';

      if (ej.titulo) {
        const h3 = document.createElement('p');
        h3.style.cssText = 'font-size:.82rem;font-weight:600;margin-bottom:.4rem;color:var(--text-secondary)';
        h3.textContent = `Ejemplo ${i + 1}: ${ej.titulo}`;
        wrap.appendChild(h3);
      }
      if (ej.input  !== undefined) wrap.appendChild(buildExampleBlock('INPUT',  ej.input,  'input'));
      if (ej.output !== undefined) wrap.appendChild(buildExampleBlock('OUTPUT', ej.output, 'output'));

      el.ejEjemplos.appendChild(wrap);
    });
    el.ejEjemplosSection.hidden = false;
  } else {
    el.ejEjemplosSection.hidden = true;
  }

  // Explanation
  if (data.explicacion) {
    el.ejExplicacion.innerHTML  = renderMarkdown(data.explicacion);
    el.ejExplicacionSection.hidden = false;
  } else {
    el.ejExplicacionSection.hidden = true;
  }

  // Show enunciado
  el.emptyState.hidden = true;
  el.enunciado.hidden  = false;

  // Editor: load code files
  const archivos = data.archivos || { 'code.py': '# Escribe tu solución aquí\n' };
  state.initialCode = { ...archivos };
  state.fileCode    = { ...archivos };
  state.activeFile  = Object.keys(archivos)[0];

  renderEditorTabs(Object.keys(archivos));
  loadFileIntoEditor(state.activeFile);

  // Enable buttons
  el.btnEjecutar.disabled = false;
  el.btnLimpiar.disabled  = false;
  el.btnEntregar.disabled = false;
  el.btnRevisar.disabled  = false;

  // Clear terminal
  setTerminalContent('<span class="results-hint">// Ejercicio cargado. Presiona ▶ Ejecutar para ver los resultados.</span>');
}

/* ══════════════════════════════════════════════════
   EDITOR TABS
══════════════════════════════════════════════════ */
function renderEditorTabs(files) {
  el.editorTabs.innerHTML = '';
  files.forEach((file) => {
    const btn = document.createElement('button');
    btn.className  = 'editor-tab' + (file === state.activeFile ? ' editor-tab--active' : '');
    btn.role       = 'tab';
    btn.dataset.file = file;
    btn.setAttribute('aria-selected', file === state.activeFile ? 'true' : 'false');

    const icon = file.endsWith('.py') ? '🐍' : '📦';
    btn.innerHTML = `<span class="tab-icon">${icon}</span> ${file}`;

    btn.addEventListener('click', () => switchTab(file));
    el.editorTabs.appendChild(btn);
  });
}

function switchTab(filename) {
  // Save current editor content to state
  if (state.monacoEditor) {
    state.fileCode[state.activeFile] = state.monacoEditor.getValue();
  }
  state.activeFile = filename;

  // Update tab UI
  $$('.editor-tab', el.editorTabs).forEach((tab) => {
    const active = tab.dataset.file === filename;
    tab.classList.toggle('editor-tab--active', active);
    tab.setAttribute('aria-selected', active ? 'true' : 'false');
  });

  loadFileIntoEditor(filename);
}

function loadFileIntoEditor(filename) {
  if (!state.monacoEditor) return;
  const code = state.fileCode[filename] ?? '';
  state.monacoEditor.setValue(code);

  // Set language based on extension
  const lang = filename.endsWith('.py') ? 'python'
             : filename.endsWith('.js') ? 'javascript'
             : filename.endsWith('.json') ? 'json'
             : 'plaintext';

  const model = state.monacoEditor.getModel();
  if (model) monaco.editor.setModelLanguage(model, lang);

  state.monacoEditor.focus();
}

/* ══════════════════════════════════════════════════
   TERMINAL HELPERS
══════════════════════════════════════════════════ */
function setTerminalContent(html) {
  el.resultsOutput.innerHTML = html;
}

function showLoading() {
  setTerminalContent('<span class="results-info">⏳ Ejecutando…</span>');
  // Expand terminal if collapsed
  if (el.resultsPanel.classList.contains('collapsed')) toggleTerminal();
}

function toggleTerminal() {
  const collapsed = el.resultsPanel.classList.toggle('collapsed');
  el.resultsToggle.setAttribute('aria-expanded', !collapsed);
}

/* ══════════════════════════════════════════════════
   SIDEBAR — load section list
══════════════════════════════════════════════════ */
async function loadSidebar() {
  try {
    const res  = await fetch('/api/cursos/iic2233-2026-1/secciones');
    const data = await res.json();
    const items = data.secciones || data.ejercicios || data || [];

    state.ejercicios = items;
    el.sidebarCount.textContent = items.length;
    el.questionList.innerHTML   = '';

    if (items.length === 0) {
      el.questionList.innerHTML = '<li style="padding:.75rem;color:var(--text-muted);font-size:.82rem">No hay ejercicios disponibles.</li>';
      return;
    }

    items.forEach((item, idx) => {
      const li = buildQuestionItem(item, idx + 1);
      el.questionList.appendChild(li);
    });

  } catch (err) {
    console.error('[ClearnPA] loadSidebar error:', err);
    // Show mock data for development / offline
    loadMockSidebar();
  }
}

function buildQuestionItem(item, num) {
  const li = document.createElement('li');
  li.className = 'question-item';
  li.setAttribute('role', 'option');
  li.setAttribute('tabindex', '0');
  li.dataset.id = item.id ?? num;

  const iconMap = { actividad: '</>', evaluacion: '📝', materia: '📖', tarea: '📋' };
  const icon = iconMap[(item.tipo || '').toLowerCase()] || '</>';

  li.innerHTML = `
    <span class="question-item__num">${num}</span>
    <span class="question-item__icon">${icon}</span>
    <span class="question-item__name" title="${item.nombre || item.titulo || ''}">${item.nombre || item.titulo || `Pregunta ${num}`}</span>
    <span class="question-item__done">✓</span>
  `;

  if (item.completado) li.classList.add('done');

  const activate = () => selectEjercicio(item.id ?? num, li);
  li.addEventListener('click', activate);
  li.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); } });

  return li;
}

/* ── Select exercise ── */
async function selectEjercicio(id, listItem) {
  // Update active state in sidebar
  $$('.question-item').forEach((el) => el.classList.remove('active'));
  if (listItem) listItem.classList.add('active');

  state.currentEjercicioId = id;

  // Show loading placeholder
  el.emptyState.hidden = true;
  el.enunciado.hidden  = false;
  el.ejTitle.textContent = '⏳ Cargando…';
  el.ejObjetivo.textContent = '';
  el.ejDescripcion.innerHTML = '';

  try {
    const res  = await fetch(`/api/ejercicio/${id}`);
    const data = await res.json();
    renderEjercicio(data);
  } catch (err) {
    console.error('[ClearnPA] selectEjercicio error:', err);
    // Use mock data for development / offline
    renderEjercicio(getMockEjercicio(id));
  }
}

/* ══════════════════════════════════════════════════
   EJECUTAR
══════════════════════════════════════════════════ */
async function ejecutar() {
  if (!state.currentEjercicioId) return;

  // Save current file before running
  if (state.monacoEditor) {
    state.fileCode[state.activeFile] = state.monacoEditor.getValue();
  }

  showLoading();
  setEditorStatus('⏳ Ejecutando…', '');

  try {
    const res = await fetch('/api/ejecutar', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        codigo:       state.fileCode,       // send all files
        ejercicio_id: state.currentEjercicioId,
      }),
    });

    const data = await res.json();
    displayResults(data);

  } catch (err) {
    console.error('[ClearnPA] ejecutar error:', err);
    setTerminalContent(`<span class="results-error">❌ Error de red: ${err.message}</span>`);
    setEditorStatus('Error de red', 'err');
  }
}

function displayResults(data) {
  let html = '';

  if (data.stdout) {
    html += `<span class="results-info">▶ STDOUT</span>\n`;
    html += `<span class="results-stdout">${escapeHtml(data.stdout)}</span>\n`;
  }
  if (data.stderr) {
    html += `<span class="results-info">⚠ STDERR</span>\n`;
    html += `<span class="results-stderr">${escapeHtml(data.stderr)}</span>\n`;
  }
  if (data.resultado !== undefined) {
    const ok = data.resultado === 'correcto' || data.resultado === true;
    html += ok
      ? `<span class="results-ok">✅ ¡Correcto!</span>\n`
      : `<span class="results-error">❌ Incorrecto</span>\n`;

    if (data.tests) {
      data.tests.forEach((t) => {
        const icon = t.ok ? '✅' : '❌';
        html += `  ${icon} ${escapeHtml(t.nombre)}\n`;
      });
    }
  }
  if (!html) {
    html = '<span class="results-hint">// Sin salida.</span>';
  }

  setTerminalContent(html);

  const hasError = !!(data.stderr || data.resultado === false || data.resultado === 'incorrecto');
  setEditorStatus(hasError ? '❌ Error' : '✅ OK', hasError ? 'err' : 'ok');

  // Expand terminal
  if (el.resultsPanel.classList.contains('collapsed')) toggleTerminal();
}

function setEditorStatus(text, cls = '') {
  el.editorStatus.textContent = text;
  el.editorStatus.className   = `editor-status ${cls}`;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/* ══════════════════════════════════════════════════
   LIMPIAR
══════════════════════════════════════════════════ */
function limpiar() {
  const initial = state.initialCode[state.activeFile];
  if (initial !== undefined && state.monacoEditor) {
    state.monacoEditor.setValue(initial);
    state.fileCode[state.activeFile] = initial;
    setEditorStatus('↺ Restaurado', '');
    setTimeout(() => setEditorStatus('', ''), 2000);
  }
}

/* ══════════════════════════════════════════════════
   ENTREGAR
══════════════════════════════════════════════════ */
async function entregar() {
  if (!state.currentEjercicioId) return;
  if (!confirm('¿Deseas entregar tu solución? Esta acción no se puede deshacer.')) return;

  if (state.monacoEditor) {
    state.fileCode[state.activeFile] = state.monacoEditor.getValue();
  }

  el.btnEntregar.disabled = true;
  setEditorStatus('📤 Entregando…', '');

  try {
    const res = await fetch('/api/entregar', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        codigo:       state.fileCode,
        ejercicio_id: state.currentEjercicioId,
      }),
    });
    const data = await res.json();

    if (data.ok || data.success) {
      setEditorStatus('✅ Entregado', 'ok');
      setTerminalContent('<span class="results-ok">✅ Solución entregada correctamente.</span>');
      // Mark as done in sidebar
      const activeItem = $('.question-item.active');
      if (activeItem) activeItem.classList.add('done');
    } else {
      setEditorStatus('❌ Error al entregar', 'err');
      setTerminalContent(`<span class="results-error">❌ ${escapeHtml(data.mensaje || data.error || 'Error desconocido')}</span>`);
    }
  } catch (err) {
    setEditorStatus('Error de red', 'err');
    setTerminalContent(`<span class="results-error">❌ Error de red: ${err.message}</span>`);
  } finally {
    el.btnEntregar.disabled = false;
  }
}

/* ══════════════════════════════════════════════════
   MOCK DATA  (offline / development fallback)
══════════════════════════════════════════════════ */
function loadMockSidebar() {
  const mock = [
    { id: 'ac1', nombre: 'AC1 — Herencia y OOP',    tipo: 'actividad'  },
    { id: 'ac2', nombre: 'AC2 — Árboles y Grafos',  tipo: 'actividad'  },
    { id: 'ac3', nombre: 'AC3 — Iteradores',         tipo: 'actividad'  },
    { id: 'ex1', nombre: 'EX1 — Examen Módulo 1',   tipo: 'evaluacion' },
    { id: 'm1',  nombre: 'M1  — Introducción',       tipo: 'materia'    },
  ];
  state.ejercicios = mock;
  el.sidebarCount.textContent = mock.length;
  el.questionList.innerHTML   = '';
  mock.forEach((item, idx) => {
    el.questionList.appendChild(buildQuestionItem(item, idx + 1));
  });
}

function getMockEjercicio(id) {
  return {
    id,
    titulo:      `Ejercicio ${id}`,
    nombre_corto: String(id).toUpperCase(),
    tipo:         'actividad',
    objetivo:     'Aplicar los conceptos de Programación Avanzada vistos en clases.',
    descripcion:  `## Enunciado\n\nCompleta la función **solve()** para que retorne el resultado esperado.\n\n- Lee los datos desde **stdin**.\n- Imprime el resultado en **stdout**.\n\nRecuerda respetar el formato de salida indicado en los ejemplos.`,
    ejemplos: [
      { titulo: 'Caso básico', input: '5\n3', output: '8' },
      { titulo: 'Caso borde',  input: '0\n0', output: '0' },
    ],
    explicacion: 'El programa debe leer dos enteros y devolver su suma. Asegúrate de convertir la entrada con `int()`.',
    archivos: {
      'code.py':     '# Escribe tu solución aquí\n\ndef solve():\n    pass\n\nif __name__ == "__main__":\n    solve()\n',
      'entities.py': '# Clases auxiliares (si las necesitas)\n',
    },
  };
}

/* ══════════════════════════════════════════════════
   EVENT LISTENERS
══════════════════════════════════════════════════ */
function attachListeners() {
  el.btnEjecutar.addEventListener('click', ejecutar);
  el.btnLimpiar.addEventListener('click',  limpiar);
  el.btnEntregar.addEventListener('click', entregar);

  el.btnRevisar.addEventListener('click', () => {
    alert('📋 Revisando entrega… (funcionalidad conectada al backend)');
  });

  // Terminal toggle
  el.resultsToggle.addEventListener('click', toggleTerminal);
  el.resultsToggle.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleTerminal(); }
  });
}

/* ══════════════════════════════════════════════════
   INIT
══════════════════════════════════════════════════ */
async function init() {
  attachListeners();

  // Disable action buttons until an exercise is selected
  el.btnEjecutar.disabled = true;
  el.btnLimpiar.disabled  = true;
  el.btnEntregar.disabled = true;

  // Boot Monaco & load sidebar in parallel
  await Promise.all([
    initMonaco(),
    loadSidebar(),
  ]);

  console.log('[ClearnPA] ✅ Aplicación lista');
}

// Wait for DOM
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

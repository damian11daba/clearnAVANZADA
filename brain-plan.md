# Plan de rediseño ClearnP.A v2.0

## Estructura de rutas
- / → landing page con el curso
- /semana/<id> → vista de semana con sus lecciones
- /semana/<id>/leccion/<nb_id> → lección interactiva del notebook
- /actividad/<id> → vista de actividad con preguntas
- /actividad/<id>/pregunta/<n> → pregunta específica
- /evaluacion/<id>/pregunta/<n> → evaluación/interrogación

## Flujo de dificultad por semana
1. Leer teoría (notebook convertido a HTML interactivo)
2. Ejercicios de práctica simples (autogenerados del notebook)  
3. Actividad completa (AC del Syllabus)
4. Evaluación (Interrogación/Examen)

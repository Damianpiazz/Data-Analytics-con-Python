# ADR-005: Notebook único generado programáticamente

**Estado:** Aceptada

## Contexto

El proyecto necesita un notebook Jupyter que recorra todo el pipeline para presentación final. Inicialmente se generaron 4 notebooks separados (uno por etapa del curso), pero esto fragmentaba el flujo de análisis y dificultaba la presentación como informe único.

## Decisión

Generamos **un solo notebook** (`analisis_comercial.ipynb`) mediante un script Python que usa `nbformat`, en lugar de crearlo manualmente en la interfaz de Jupyter.

```
notebooks/
  analisis_comercial.ipynb   # Notebook final (generado)
```

El script generador (`generate_unified.py`) se elimina después de generar el notebook; no se versiona como parte del proyecto porque el notebook es el artefacto final.

## Alternativas consideradas

1. **4 notebooks separados**: Rechazado porque obliga al usuario a abrir y ejecutar 4 archivos en orden, y el tono académico ("Etapa 1", "Actividades") no es profesional.
2. **Notebook manual en Jupyter**: Rechazado porque es propenso a errores de formato, celdas fuera de orden, y difícil de regenerar si algo cambia.
3. **Dashboard con Panel/Dash**: Rechazado porque requiere servidores corriendo y no es tan accesible como un notebook.

## Consecuencias

**Positivas:**
- El notebook es reproducible: se regenera completo si el pipeline cambia.
- Formato consistente (markdown profesional, código correcto, imports exactos).
- Un solo archivo para compartir y ejecutar.
- Se puede ejecutar de punta a punta sin intervención del usuario.

**Negativas:**
- El script generador debe mantenerse sincronizado con la API real de `src/`.
- El notebook generado es JSON; los diffs en git son difíciles de leer (aunque mejor que notebooks manuales que guardan outputs binarios).
- Si se quiere modificar el notebook, hay que modificar el generador y regenerar.

## Cumplimiento

- El notebook debe ejecutarse sin errores `python -m jupyter nbconvert --to notebook --execute`.
- El notebook debe importar desde `src/`, no tener código duplicado.
- El tono del notebook debe ser profesional, no académico.

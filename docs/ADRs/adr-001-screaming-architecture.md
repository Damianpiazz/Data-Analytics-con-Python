# ADR-001: Estructura Screaming Architecture

**Estado:** Aceptada

## Contexto

El proyecto necesita organizar módulos de Python para carga, limpieza, transformación, análisis estadístico, visualización y utilidades. La estructura debe ser mantenible, escalable y fácil de navegar para un equipo de datos.

Las opciones típicas son:

- **Por capa técnica**: modelos/ → servicios/ → controllers/ → views/
- **Por dominio**: data/ → analysis/ → visualization/ → utils/

## Decisión

Usamos **Screaming Architecture** (también llamada _package by feature_ o _package by domain_) donde la estructura del proyecto refleja los dominios del negocio de datos:

```
src/
  data/           # Pipeline ETL
    loader.py
    cleaner.py
    transformer.py
    exporter.py
  analysis/       # Análisis estadístico
    descriptive.py
    correlations.py
    aggregations.py
  visualization/  # Visualización
    plots.py
    interactive.py
    styles.py
  utils/          # Utilidades
    helpers.py
    validators.py
```

Cada directorio raíz (`data/`, `analysis/`, etc.) contiene un `__init__.py` que expone la API pública del módulo.

## Alternativas consideradas

1. **Estructura plana**: Todos los `.py` en `src/`. Rechazada porque escala mal; 10+ archivos en un directorio son difíciles de navegar.
2. **Por tipo de archivo**: `src/models/`, `src/services/`. Rechazada porque mezcla dominios no relacionados (un "service" de limpieza vs uno de visualización no comparten nada).
3. **Monolito en un archivo**: Un solo `pipeline.py`. Rechazada porque viola el principio de responsabilidad única y hace imposible el testeo unitario.

## Consecuencias

**Positivas:**
- Navegación intuitiva: sabés dónde buscar según lo que querés hacer.
- Cada módulo tiene un `__init__.py` que controla su API pública.
- Fácil añadir nuevos dominios (ej: `src/ml/` para modelos predictivos).
- Los tests siguen la misma estructura (`tests/test_cleaner.py`, `tests/test_analysis.py`).

**Negativas:**
- Puede haber dependencias circulares si dos dominios se necesitan mutuamente (se resuelve con inyección desde el orquestador, nunca desde el import).
- No es la estructura estándar de Django/Rails, pero este proyecto no es una web app.

## Cumplimiento

- Cualquier archivo nuevo debe ir en el subdirectorio correspondiente a su dominio.
- No se permite importar desde `src/analysis/` hacia `src/data/` (solo al revés).
- Revisar en code review que los imports respeten la dirección de dependencias.

# ADR-007: Logging estructurado para trazabilidad

**Estado:** Aceptada

## Contexto

El pipeline ejecuta múltiples operaciones (carga, limpieza, transformación, exportación) que pueden fallar o producir resultados inesperados. Sin logging, diagnosticar problemas requiere ejecutar paso a paso manualmente.

## Decisión

Implementamos logging estructurado con el módulo `logging` de la stdlib, sin depender de librerías externas como `loguru` o `structlog`:

```python
# config/logging_config.py
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(REPORTS_DIR / "pipeline.log"),
        ],
    )
```

Cada módulo obtiene su propio logger:

```python
logger = get_module_logger(__name__)
logger.info("clean_precio: %d valores convertidos", n)
```

El formato incluye timestamp, nivel, nombre del módulo y mensaje.

## Alternativas consideradas

1. **print()**: Rechazado porque no discrimina niveles (info vs error), no tiene formato consistente y no se puede silenciar.
2. **loguru**: Rechazado porque agrega una dependencia externa para un caso de uso que la stdlib cubre bien.
3. **Sin logging**: Rechazado porque dificulta el debugging y la auditoría del pipeline.

## Consecuencias

**Positivas:**
- Trazabilidad completa de cada operación con timestamp y módulo.
- Dos salidas simultáneas: consola (interactivo) y archivo (auditoría).
- Se puede cambiar el nivel a DEBUG para debugging sin modificar código.

**Negativas:**
- El archivo `pipeline.log` se acumula; hay que rotarlo o limpiarlo periódicamente.
- El logging agrega overhead de E/S, insignificante para el tamaño actual.

## Cumplimiento

- Todo módulo del pipeline debe obtener su logger via `get_module_logger(__name__)`.
- No usar `print()` en código de producción en `src/`.
- Los mensajes de logging deben ser informativos e incluir métricas cuando corresponda (cantidad de filas, valores transformados, etc.).

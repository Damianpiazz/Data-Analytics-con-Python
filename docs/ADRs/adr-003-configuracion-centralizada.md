# ADR-003: Configuración centralizada con Path constants

**Estado:** Aceptada

## Contexto

El pipeline necesita rutas a archivos CSV, nombres de columnas y directorios de salida. Sin centralización, estos valores se repiten como strings hardcodeados en múltiples módulos, lo que genera inconsistencia y errores difíciles de rastrear.

## Decisión

Crear `config/settings.py` como fuente única de verdad para:

- **Rutas absolutas**: derivadas de `Path(__file__).resolve().parent.parent`, sin strings relativos frágiles.
- **Nombres de columnas**: constantes como `COL_PRECIO`, `COL_VENTA_TOTAL` para evitar errores por typos.
- **Archivos de salida**: rutas predefinidas para datos procesados y el dataset final.

```python
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
VENTAS_FILE = RAW_DATA_DIR / "ventas.csv"
COL_PRECIO = "precio"
```

Además, `config/logging_config.py` centraliza la configuración de logging para que todos los módulos tengan formato consistente.

## Alternativas consideradas

1. **Variables de entorno**: `.env` + `python-dotenv`. Rechazada porque agrega una dependencia externa y no hay secretos que proteger en este proyecto.
2. **Archivo YAML/JSON de configuración**: Rechazado porque agrega otro archivo y un paso de parseo; Python puro es más directo.
3. **Strings hardcodeados en cada módulo**: Rechazado por violar DRY y ser propenso a errores.

## Consecuencias

**Positivas:**
- Cambiar una ruta o nombre de columna se hace en un solo lugar.
- Los tests pueden sobrescribir rutas fácilmente.
- No hay strings mágicos dispersos en el código.

**Negativas:**
- `settings.py` se importa al inicio del módulo, no es dinámico (no se puede cambiar en caliente). No es un problema real para este proyecto.
- Cualquier módulo nuevo debe importar `settings.py`; hay que recordarlo.

## Cumplimiento

- Ningún string de ruta o nombre de columna debe aparecer directamente en los módulos del pipeline; deben importarse desde `config.settings`.
- Cualquier nueva ruta o constante debe agregarse a `settings.py` antes de ser usada.

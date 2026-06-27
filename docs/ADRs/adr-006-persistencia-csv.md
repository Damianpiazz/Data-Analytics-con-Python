# ADR-006: Persistencia en CSV plano

**Estado:** Aceptada

## Contexto

El pipeline necesita almacenar los datos procesados para su consumo en notebooks, herramientas de visualización externas o modelos posteriores. La elección del formato de persistencia impacta en portabilidad, rendimiento y facilidad de uso.

## Decisión

Usamos **CSV plano** con codificación UTF-8 BOM (`utf-8-sig`) como formato de persistencia:

```python
df.to_csv(path, index=False, encoding="utf-8-sig")
```

Los archivos se guardan en `data/processed/` con nombres descriptivos:

```
data/processed/
  ventas_processed.csv
  marketing_processed.csv
  clientes_processed.csv
  dataset_final.csv        # Dataset consolidado
```

## Alternativas consideradas

1. **Parquet**: Formato columnar binario, más eficiente en espacio y velocidad. Rechazado porque no es legible directamente por Excel, Power BI o la mayoría de las herramientas de negocio.
2. **SQLite**: Base de datos embebida. Rechazada porque agrega dependencia de SQL y complejidad para un dataset de ~3000 filas.
3. **Pickle**: Formato serializado de Python. Rechazado porque no es portable a otras herramientas ni legible por humanos.
4. **Excel (xlsx)**: Rechazado porque es más lento de escribir/leer, tiene límites de filas y no es amigable con control de versiones.

## Consecuencias

**Positivas:**
- Los CSVs se abren en cualquier herramienta (Excel, Google Sheets, Power BI, Tableau).
- Son legibles por humanos y se pueden versionar en git (con git-lfs para archivos grandes).
- La exportación es una línea de código.
- UTF-8 BOM asegura que Excel interprete correctamente los caracteres en español (ñ, tildes).

**Negativas:**
- Sin esquema: el tipo de datos se pierde al guardar (hay que re-especificar al leer). Se mitiga con `settings.py` que define las columnas esperadas.
- Ocupa más espacio que formatos binarios (~1MB para dataset final). Irrelevante para el tamaño actual.
- Sin compresión nativa (se puede comprimir externamente si es necesario).

## Cumplimiento

- Todos los archivos de salida se guardan en `data/processed/`.
- Usar siempre `encoding="utf-8-sig"` para compatibilidad con Excel.
- No versionar CSVs generados en git (agregar `data/processed/*.csv` a `.gitignore`).

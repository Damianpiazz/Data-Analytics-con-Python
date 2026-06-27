# ADR-002: Pipeline ETL con funciones puras

**Estado:** Aceptada

## Contexto

El pipeline ETL (carga → limpia → transforma → exporta) necesita ejecutarse de forma confiable y componible. Cada etapa debe poder ejecutarse por separado para debugging, tests o notebooks parciales.

## Decisión

Cada etapa del pipeline es una **función pura** que recibe un DataFrame y devuelve un DataFrame (o un dict de ellos), sin efectos secundarios más allá del logging interno:

```python
def clean_precio(df: pd.DataFrame, column: str | None = None) -> pd.DataFrame:
    df = df.copy()  # Nunca muta el original
    # ... transformaciones ...
    return df
```

No hay clases, no hay estado compartido, no hay mutación de los datos originales. Todas las funciones internamente hacen `df.copy()` antes de modificar.

## Alternativas consideradas

1. **Clase Pipeline** con métodos encadenables: `Pipeline().load().clean().transform().export()`. Rechazada porque agrega complejidad innecesaria para un flujo lineal.
2. **Estado mutable global**: Una variable `datos` que cada etapa modifica. Rechazada porque hace imposible el testeo y el debugging.
3. **Decoradores para registro automático**: Tentador, pero oscurece el flujo y dificulta el debugging.

## Consecuencias

**Positivas:**
- Cada función es testeable de forma aislada.
- Se pueden componer en cualquier orden.
- No hay efectos secundarios ocultos.
- Fácil agregar nuevos pasos sin modificar los existentes.

**Negativas:**
- Cada `copy()` tiene un costo en memoria con datasets grandes (>1M filas). No es problema para el tamaño actual (~3K filas).
- El orquestador (notebook o script) es responsable de encadenar las llamadas; no hay una clase que lo haga automáticamente.

## Cumplimiento

- Toda función del pipeline debe tener tipo de retorno explícito (`-> pd.DataFrame`).
- Ninguna función debe modificar el DataFrame de entrada sin copiar.
- No se permiten clases en `src/data/` salvo que el requerimiento lo justifique explícitamente.

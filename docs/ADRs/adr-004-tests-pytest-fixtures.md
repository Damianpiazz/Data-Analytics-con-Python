# ADR-004: Tests con pytest y fixtures compartidas

**Estado:** Aceptada

## Contexto

El proyecto necesita verificar que las funciones de limpieza y análisis producen resultados correctos. Sin tests automatizados, cada cambio requiere verificación manual, lo que es lento y propenso a errores.

## Decisión

Usamos **pytest** como framework de testing con:

- **Fixtures compartidas** en `tests/conftest.py` con DataFrames pequeños de ejemplo (4-5 filas) para evitar depender de los CSVs reales.
- **Tests agrupados por funcionalidad** en `test_cleaner.py` y `test_analysis.py`.
- **Aserciones explícitas** con `pytest.approx()` para valores float.
- Uso de `pd.testing.assert_frame_equal()` para comparar DataFrames completos.

```python
@pytest.fixture
def sample_ventas():
    return pd.DataFrame({
        "precio": ["$100.00", "$200.50", "$100.00", "$50.00"],
        "cantidad": [2, 1, 3, 5],
    })

def test_clean_precio(sample_ventas):
    resultado = clean_precio(sample_ventas.copy())
    assert resultado["precio"].iloc[0] == 100.00
```

## Alternativas consideradas

1. **unittest** (stdlib): Rechazado porque requiere más boilerplate (clases, `self.assert*`) y no tiene fixtures tan flexibles.
2. **Tests contra datos reales**: Rechazado porque los CSVs pueden cambiar y haría los tests lentos y frágiles.
3. **Sin tests**: Rechazado por obvias razones de calidad.

## Consecuencias

**Positivas:**
- 38 tests corriendo en <1 segundo.
- Las fixtures aíslan los tests de los datos reales.
- Fácil agregar nuevos tests para funciones nuevas.
- Detección temprana de regresiones (ya pasó al alinear tests con la API real).

**Negativas:**
- Las fixtures deben mantenerse sincronizadas si la estructura de datos cambia.
- Los tests con valores float requieren `pytest.approx()` para evitar falsos positivos por precisión numérica.

## Cumplimiento

- Toda función pública en `src/` debe tener al menos un test.
- Los tests nunca deben depender de archivos en `data/raw/`.
- Ejecutar `python -m pytest tests/ -v` antes de cada commit.

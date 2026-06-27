"""Tests para el módulo de limpieza de datos (src/data/cleaner.py).

Verifica que las funciones de limpieza transformen correctamente
los datos sucios en datos listos para análisis.
"""

import pandas as pd
import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Tests para clean_precio
# ---------------------------------------------------------------------------

def test_clean_precio(sample_ventas):
    """clean_precio debe convertir strings como '$100.00' a float 100.0."""
    from src.data.cleaner import clean_precio

    resultado = clean_precio(sample_ventas.copy(), "precio")

    assert resultado["precio"].dtype == float or np.issubdtype(resultado["precio"].dtype, np.number)
    assert resultado["precio"].iloc[0] == 100.00
    assert resultado["precio"].iloc[1] == 200.50
    assert resultado["precio"].iloc[3] == 50.00


def test_clean_precio_sin_simbolo():
    """clean_precio debe funcionar también con números sin símbolo de moneda."""
    from src.data.cleaner import clean_precio

    df = pd.DataFrame({"precio": ["100", "200.5", "50"]})
    resultado = clean_precio(df, "precio")

    assert resultado["precio"].iloc[0] == 100.0
    assert resultado["precio"].iloc[1] == 200.5


def test_clean_precio_columna_inexistente():
    """clean_precio debe devolver el DataFrame sin cambios si la columna no existe."""
    from src.data.cleaner import clean_precio

    df = pd.DataFrame({"otra_col": [1, 2]})
    resultado = clean_precio(df, "precio")
    pd.testing.assert_frame_equal(resultado, df)


# ---------------------------------------------------------------------------
# Tests para remove_duplicates
# ---------------------------------------------------------------------------

def test_remove_duplicates(sample_ventas):
    """remove_duplicates debe eliminar filas duplicadas."""
    from src.data.cleaner import remove_duplicates

    df_duplicado = pd.concat([sample_ventas, sample_ventas.iloc[[0]]], ignore_index=True)
    assert len(df_duplicado) == len(sample_ventas) + 1

    resultado = remove_duplicates(df_duplicado)
    assert len(resultado) == len(sample_ventas)


def test_remove_duplicates_sin_duplicados(sample_ventas):
    """remove_duplicates no debe eliminar filas si no hay duplicados."""
    from src.data.cleaner import remove_duplicates

    resultado = remove_duplicates(sample_ventas.copy())
    assert len(resultado) == len(sample_ventas)


def test_remove_duplicates_subset():
    """remove_duplicates debe soportar el parámetro subset para considerar solo ciertas columnas."""
    from src.data.cleaner import remove_duplicates

    df = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "producto": ["A", "A", "B", "A"],
        "precio": [100.0, 100.0, 200.0, 100.0],
    })
    # Duplicado en 'producto' y 'precio' pero no en 'id'
    resultado = remove_duplicates(df, subset=["producto", "precio"])
    assert len(resultado) == 2  # A/100 y B/200


# ---------------------------------------------------------------------------
# Tests para handle_nulls
# ---------------------------------------------------------------------------

def test_handle_nulls_drop():
    """handle_nulls con strategy='drop' debe eliminar filas con nulos."""
    from src.data.cleaner import handle_nulls

    df = pd.DataFrame({
        "a": [1, 2, np.nan, 4],
        "b": [10, np.nan, 30, 40],
    })
    resultado = handle_nulls(df, strategy="drop")
    # Filas 0 (a=1,b=10) y 3 (a=4,b=40) no tienen nulos → 2 filas
    assert len(resultado) == 2


def test_handle_nulls_fill_mean():
    """handle_nulls con strategy='fill_mean' debe rellenar nulos con la media."""
    from src.data.cleaner import handle_nulls

    df = pd.DataFrame({
        "precio": [100.0, 200.0, np.nan, 400.0],
    })
    resultado = handle_nulls(df, strategy="fill_mean")
    # Media de [100, 200, 400] = 700/3 ≈ 233.33
    assert resultado["precio"].iloc[2] == pytest.approx(233.3333, rel=1e-3)


def test_handle_nulls_fill_median():
    """handle_nulls con strategy='fill_median' debe rellenar nulos con la mediana."""
    from src.data.cleaner import handle_nulls

    df = pd.DataFrame({
        "precio": [100.0, 200.0, np.nan, 400.0],
    })
    resultado = handle_nulls(df, strategy="fill_median")
    # Mediana de [100, 200, 400] = 200 (ordenado: 100, 200, 400)
    assert resultado["precio"].iloc[2] == 200.0


def test_handle_nulls_fill_value():
    """handle_nulls con strategy='fill_value' debe usar el valor provisto."""
    from src.data.cleaner import handle_nulls

    df = pd.DataFrame({
        "precio": [100.0, np.nan, 300.0],
    })
    resultado = handle_nulls(df, strategy="fill_value", fill_value=0)
    assert resultado["precio"].iloc[1] == 0.0


def test_handle_nulls_strategy_invalida():
    """handle_nulls debe lanzar ValueError si la strategy no es válida."""
    from src.data.cleaner import handle_nulls

    df = pd.DataFrame({"a": [1, np.nan]})
    with pytest.raises(ValueError):
        handle_nulls(df, strategy="invalida")

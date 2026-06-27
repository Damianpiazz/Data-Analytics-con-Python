"""Validación de calidad de datos.

Proporciona funciones para verificar nulos, duplicados, tipos
esperados y un reporte consolidado de calidad sobre un DataFrame.
"""

import pandas as pd
import numpy as np
from config.logging_config import get_module_logger

logger = get_module_logger(__name__)


def validate_no_nulls(df: pd.DataFrame) -> bool:
    """Verifica que el DataFrame no contenga valores nulos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a inspeccionar.

    Returns
    -------
    bool
        ``True`` si no hay ningún valor nulo, ``False`` en caso contrario.
    """
    total_nulls = df.isna().sum().sum()
    ok = total_nulls == 0
    if not ok:
        logger.warning("validate_no_nulls: se encontraron %d valores nulos", total_nulls)
    return ok


def validate_no_duplicates(df: pd.DataFrame) -> bool:
    """Verifica que el DataFrame no contenga filas duplicadas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a inspeccionar.

    Returns
    -------
    bool
        ``True`` si no hay duplicados, ``False`` en caso contrario.
    """
    dups = df.duplicated().sum()
    ok = dups == 0
    if not ok:
        logger.warning("validate_no_duplicates: se encontraron %d filas duplicadas", dups)
    return ok


def validate_types(df: pd.DataFrame, schema: dict) -> list[str]:
    """Valida que las columnas tengan los tipos de dato esperados.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a validar.
    schema : dict
        Diccionario ``{nombre_columna: tipo_esperado}``.
        Los tipos pueden ser strings como ``"float64"``, ``"int64"``,
        ``"object"``, ``"datetime64[ns]"``, o tipos de numpy/pandas.

    Returns
    -------
    list[str]
        Lista de mensajes de error. Vacía si todo está bien.
    """
    errores = []
    for col, dtype_esperado in schema.items():
        if col not in df.columns:
            errores.append(f"Columna '{col}' no encontrada en el DataFrame")
            continue
        dtype_real = df[col].dtype
        if dtype_real != dtype_esperado:
            errores.append(
                f"Columna '{col}': se esperaba {dtype_esperado}, se obtuvo {dtype_real}"
            )
    if errores:
        logger.warning("validate_types: %d errores de tipo encontrados", len(errores))
    else:
        logger.info("validate_types: todos los tipos coinciden con el esquema")
    return errores


def report_quality(df: pd.DataFrame, name: str = "") -> dict:
    """Genera un reporte de calidad completo del DataFrame.

    Incluye porcentaje de nulos por columna, cantidad de duplicados,
    tipos de dato y rango de valores para columnas numéricas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a analizar.
    name : str
        Nombre opcional del dataset para el log.

    Returns
    -------
    dict
        Diccionario con las métricas de calidad:

        - ``"nombre"``: nombre del dataset
        - ``"filas"``: cantidad de filas
        - ``"columnas"``: cantidad de columnas
        - ``"nulos_totales"``: total de valores nulos
        - ``"nulos_por_columna"``: dict ``{col: % nulos}``
        - ``"duplicados"``: cantidad de filas duplicadas
        - ``"tipos"``: dict ``{col: str(dtype)}``
        - ``"rangos"``: dict ``{col: {"min": ..., "max": ..., "media": ...}}``
          solo para columnas numéricas.
    """
    tag = f"[{name}]" if name else ""

    nulos_totales = int(df.isna().sum().sum())
    nulos_por_columna = {
        col: round(float(df[col].isna().mean() * 100), 2)
        for col in df.columns
    }
    duplicados = int(df.duplicated().sum())
    tipos = {col: str(df[col].dtype) for col in df.columns}

    rangos = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        rangos[col] = {
            "min": float(df[col].min()) if not df[col].isna().all() else None,
            "max": float(df[col].max()) if not df[col].isna().all() else None,
            "media": round(float(df[col].mean()), 2) if not df[col].isna().all() else None,
        }

    reporte = {
        "nombre": name,
        "filas": len(df),
        "columnas": len(df.columns),
        "nulos_totales": nulos_totales,
        "nulos_por_columna": nulos_por_columna,
        "duplicados": duplicados,
        "tipos": tipos,
        "rangos": rangos,
    }

    logger.info(
        "%s Calidad: %d filas, %d columnas, %d nulos, %d duplicados",
        tag,
        reporte["filas"],
        reporte["columnas"],
        nulos_totales,
        duplicados,
    )
    return reporte

"""Funciones de estadística descriptiva para DataFrames de pandas.

Proporciona herramientas para calcular medidas de tendencia central,
dispersión, resúmenes estadísticos mejorados y detección de outliers.
"""

import pandas as pd
import numpy as np


def tendencia_central(df: pd.DataFrame, columns: list = None) -> dict:
    """Calcula media, mediana y moda para las columnas numéricas especificadas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos a analizar.
    columns : list, optional
        Lista de columnas numéricas a evaluar. Si es None, usa todas las
        columnas numéricas del DataFrame.

    Returns
    -------
    dict
        Diccionario con la forma {'columna': {'media': ..., 'mediana': ..., 'moda': ...}}.
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    resultado = {}
    for col in columns:
        if col not in df.columns:
            continue
        serie = df[col].dropna()
        if serie.empty:
            continue

        # Cálculo de moda: puede haber múltiples; tomamos el primer valor
        moda_vals = serie.mode()
        moda = moda_vals.iloc[0] if not moda_vals.empty else np.nan

        resultado[col] = {
            "media": round(serie.mean(), 4),
            "mediana": round(serie.median(), 4),
            "moda": round(moda, 4) if isinstance(moda, (int, float)) else moda,
        }

    return resultado


def dispersion(df: pd.DataFrame, columns: list = None) -> dict:
    """Calcula varianza, desvío estándar, rango y rango intercuartil (IQR).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos a analizar.
    columns : list, optional
        Lista de columnas numéricas. Si es None, usa todas las numéricas.

    Returns
    -------
    dict
        Diccionario con la forma {'columna': {'varianza': ..., 'std': ..., ...}}.
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    resultado = {}
    for col in columns:
        if col not in df.columns:
            continue
        serie = df[col].dropna()
        if serie.empty:
            continue

        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)

        resultado[col] = {
            "varianza": round(serie.var(), 4),
            "std": round(serie.std(), 4),
            "rango": round(serie.max() - serie.min(), 4),
            "min": round(serie.min(), 4),
            "max": round(serie.max(), 4),
            "q25": round(q1, 4),
            "q75": round(q3, 4),
            "iqr": round(q3 - q1, 4),
        }

    return resultado


def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna un DataFrame con estadísticas descriptivas mejoradas.

    Incluye las métricas de df.describe() más IQR y rango.
    Útil para tener una visión rápida y completa de la distribución
    de cada variable numérica.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a analizar.

    Returns
    -------
    pd.DataFrame
        DataFrame con filas: conteo, media, std, min, 25%, 50%, 75%,
        max, IQR, rango.
    """
    desc = df.describe(include=[np.number])

    # Agregar IQR y rango
    for col in desc.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        desc.loc["iqr", col] = q3 - q1
        desc.loc["rango", col] = df[col].max() - df[col].min()

    return desc


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Detecta outliers usando el método del rango intercuartil (IQR).

    Un valor se considera outlier si está por debajo de Q1 - 1.5*IQR
    o por encima de Q3 + 1.5*IQR.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    column : str
        Nombre de la columna numérica a evaluar.

    Returns
    -------
    pd.DataFrame
        Copia del DataFrame original con una columna adicional 'is_outlier'
        (booleano) que indica si cada fila es outlier en la columna dada.
    """
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame.")

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"La columna '{column}' debe ser numérica.")

    resultado = df.copy()
    q1 = resultado[column].quantile(0.25)
    q3 = resultado[column].quantile(0.75)
    iqr = q3 - q1

    cota_inferior = q1 - 1.5 * iqr
    cota_superior = q3 + 1.5 * iqr

    resultado["is_outlier"] = (resultado[column] < cota_inferior) | (
        resultado[column] > cota_superior
    )

    return resultado

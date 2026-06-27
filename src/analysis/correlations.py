"""Funciones para análisis de correlaciones entre variables numéricas.

Soporta los métodos de Pearson, Spearman y Kendall, y ofrece
utilidades para encontrar las correlaciones más relevantes.
"""

import pandas as pd
import numpy as np


def correlation_matrix(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """Calcula la matriz de correlación para las columnas numéricas del DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    method : str, optional
        Método de correlación: 'pearson' (default), 'spearman' o 'kendall'.

    Returns
    -------
    pd.DataFrame
        Matriz de correlación cuadrada.
    """
    if method not in ("pearson", "spearman", "kendall"):
        raise ValueError(f"Método '{method}' no soportado. Usá pearson, spearman o kendall.")

    return df.select_dtypes(include=[np.number]).corr(method=method)


def analyze_correlations(df: pd.DataFrame, threshold: float = 0.5) -> dict:
    """Encuentra pares de variables con correlación fuerte.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    threshold : float, optional
        Umbral mínimo de |correlación| para considerar un par como fuerte.
        Por defecto 0.5.

    Returns
    -------
    dict
        Diccionario con dos listas:
        - 'fuertes_positivas': pares con correlación > threshold
        - 'fuertes_negativas': pares con correlación < -threshold
        Cada elemento es (var1, var2, valor_correlacion).
    """
    corr = correlation_matrix(df)
    fuertes_positivas = []
    fuertes_negativas = []

    # Recorremos solo el triángulo superior para evitar duplicados
    for i in range(len(corr.columns)):
        for j in range(i + 1, len(corr.columns)):
            valor = corr.iloc[i, j]
            if pd.isna(valor):
                continue
            if valor > threshold:
                fuertes_positivas.append((corr.columns[i], corr.columns[j], round(valor, 4)))
            elif valor < -threshold:
                fuertes_negativas.append((corr.columns[i], corr.columns[j], round(valor, 4)))

    return {
        "fuertes_positivas": sorted(fuertes_positivas, key=lambda x: abs(x[2]), reverse=True),
        "fuertes_negativas": sorted(fuertes_negativas, key=lambda x: abs(x[2]), reverse=True),
    }


def top_correlations(corr_matrix: pd.DataFrame, n: int = 5) -> list:
    """Devuelve las n correlaciones más fuertes en valor absoluto.

    Excluye la diagonal (correlación de una variable consigo misma).

    Parameters
    ----------
    corr_matrix : pd.DataFrame
        Matriz de correlación cuadrada.
    n : int, optional
        Cantidad de pares a devolver. Por defecto 5.

    Returns
    -------
    list
        Lista de tuplas (var1, var2, valor), ordenadas de mayor a menor
        según |valor|.
    """
    pares = []

    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            valor = corr_matrix.iloc[i, j]
            if pd.isna(valor):
                continue
            pares.append((corr_matrix.columns[i], corr_matrix.columns[j], round(valor, 4)))

    # Ordenar por valor absoluto descendente
    pares.sort(key=lambda x: abs(x[2]), reverse=True)

    return pares[:n]

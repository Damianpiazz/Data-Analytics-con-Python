"""Limpieza de datos para los tres datasets del pipeline.

Cada función está pensada para ser componible dentro de ``clean_all``,
que ejecuta el pipeline completo de limpieza y loggea cada paso.
"""

import pandas as pd
import numpy as np
from config.logging_config import get_module_logger
from config.settings import COL_PRECIO, COL_COSTO

logger = get_module_logger(__name__)


def clean_precio(df: pd.DataFrame, column: str | None = None) -> pd.DataFrame:
    """Limpia la columna de precio: elimina el signo ``$`` y convierte a float.

    Los valores vacíos o que no puedan convertirse quedan como ``NaN``.
    La transformación se hace sobre una copia para no mutar el original.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna de precio.
    column : str, optional
        Nombre de la columna a limpiar. Si es ``None``, usa ``COL_PRECIO``.

    Returns
    -------
    pd.DataFrame
        Copia con la columna en tipo ``float64``.
    """
    col = column if column is not None else COL_PRECIO
    df = df.copy()
    if col not in df.columns:
        logger.warning("Columna '%s' no encontrada, se omite clean_precio", col)
        return df

    antes = df[col].isna().sum()
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r"[$ ]", "", regex=True)
        .replace("", np.nan)
        .astype(float)
    )
    despues = df[col].isna().sum()
    logger.info(
        "clean_precio: %d valores no numéricos convertidos a NaN (total NaN: %d)",
        despues - antes,
        despues,
    )
    return df


def clean_costo(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte la columna ``costo`` a ``float`` eliminando ceros adelantados.

    Valores como ``"05.07"`` se convierten a ``5.07``.
    Los vacíos o no numéricos pasan a ``NaN``.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna ``costo``.

    Returns
    -------
    pd.DataFrame
        Copia con ``costo`` en ``float64``.
    """
    df = df.copy()
    if COL_COSTO not in df.columns:
        logger.warning("Columna '%s' no encontrada, se omite clean_costo", COL_COSTO)
        return df

    antes = df[COL_COSTO].isna().sum()
    df[COL_COSTO] = pd.to_numeric(df[COL_COSTO], errors="coerce")
    despues = df[COL_COSTO].isna().sum()
    logger.info(
        "clean_costo: %d valores no numéricos convertidos a NaN (total NaN: %d)",
        despues - antes,
        despues,
    )
    return df


def remove_duplicates(df: pd.DataFrame, subset: list[str] | None = None) -> pd.DataFrame:
    """Elimina filas duplicadas del DataFrame y loggea cuántas sacó.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    subset : list[str] | None
        Columnas a considerar para detectar duplicados.
        Si es ``None`` usa todas las columnas.

    Returns
    -------
    pd.DataFrame
        DataFrame sin duplicados (se conserva la primera ocurrencia).
    """
    antes = len(df)
    df = df.drop_duplicates(subset=subset, keep="first")
    despues = len(df)
    quitadas = antes - despues
    if quitadas > 0:
        logger.info(
            "remove_duplicates: %d filas duplicadas eliminadas (quedan %d)",
            quitadas,
            despues,
        )
    else:
        logger.info("remove_duplicates: no se encontraron duplicados")
    return df


def handle_nulls(df: pd.DataFrame, strategy: str = "drop", fill_value: float | None = None) -> pd.DataFrame:
    """Maneja valores nulos según la estrategia indicada.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    strategy : str
        Estrategia a aplicar:

        - ``"drop"``: elimina filas con cualquier valor nulo.
        - ``"fill_mean"``: imputa columnas numéricas con su media.
        - ``"fill_median"``: imputa columnas numéricas con su mediana.
        - ``"fill_value"``: imputa con el valor proporcionado en ``fill_value``.
    fill_value : float, optional
        Valor a usar cuando strategy es ``"fill_value"``.

    Returns
    -------
    pd.DataFrame
        DataFrame sin nulos según la estrategia elegida.

    Raises
    ------
    ValueError
        Si ``strategy`` no es válida o falta ``fill_value`` cuando se requiere.
    """
    antes = df.isna().sum().sum()
    if antes == 0:
        logger.info("handle_nulls: no hay valores nulos, no se hace nada")
        return df

    if strategy == "drop":
        df = df.dropna()
        quitadas = antes - df.isna().sum().sum()
        logger.info(
            "handle_nulls (drop): se eliminaron %d filas con nulos",
            quitadas,
        )

    elif strategy in ("fill_mean", "fill_median"):
        num_cols = df.select_dtypes(include=["float64", "int64"]).columns
        for col in num_cols:
            valor = df[col].mean() if strategy == "fill_mean" else df[col].median()
            df[col] = df[col].fillna(valor)
        logger.info(
            "handle_nulls (%s): se imputaron %d valores nulos",
            strategy, antes,
        )

    elif strategy == "fill_value":
        if fill_value is None:
            raise ValueError("Debe proporcionar 'fill_value' cuando strategy='fill_value'.")
        df = df.fillna(fill_value)
        logger.info(
            "handle_nulls (fill_value): se imputaron %d valores nulos con %s",
            antes, fill_value,
        )

    else:
        raise ValueError(f"Estrategia desconocida: '{strategy}'.")

    return df


def clean_all(df: pd.DataFrame, dataset_name: str = "") -> pd.DataFrame:
    """Ejecuta el pipeline completo de limpieza sobre un DataFrame.

    El orden de las operaciones es:

    1. Eliminar duplicados.
    2. Limpiar columna ``precio`` (si existe).
    3. Limpiar columna ``costo`` (si existe).
    4. Eliminar filas con valores nulos restantes.

    Cada paso se loggea con el nombre del dataset para trazabilidad.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a limpiar.
    dataset_name : str
        Nombre descriptivo (``"ventas"``, ``"marketing"``, etc.)
        para los mensajes de log.

    Returns
    -------
    pd.DataFrame
        DataFrame limpio.
    """
    tag = f"[{dataset_name}]" if dataset_name else ""
    logger.info("%s Inicia limpieza: %d filas", tag, len(df))

    df = remove_duplicates(df)
    df = clean_precio(df)
    df = clean_costo(df)
    df = handle_nulls(df, strategy="drop")

    logger.info("%s Limpieza completada: %d filas finales", tag, len(df))
    return df

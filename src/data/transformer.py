"""Transformaciones para enriquecer y combinar los datasets.

Incluye creación de columnas derivadas, filtros y merges
entre ventas, marketing y clientes.
"""

import pandas as pd
from config.logging_config import get_module_logger
from config.settings import (
    COL_PRECIO,
    COL_CANTIDAD,
    COL_VENTA_TOTAL,
    COL_PRODUCTO,
    COL_FECHA,
)

logger = get_module_logger(__name__)


def add_venta_total(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega la columna ``venta_total = precio * cantidad``.

    Si alguna de las dos columnas es ``NaN``, el resultado también
    será ``NaN`` (comportamiento natural de pandas).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con las columnas ``precio`` y ``cantidad``.

    Returns
    -------
    pd.DataFrame
        Copia con la nueva columna ``venta_total``.
    """
    df = df.copy()
    df[COL_VENTA_TOTAL] = df[COL_PRECIO] * df[COL_CANTIDAD]
    logger.info(
        "add_venta_total: columna '%s' agregada (precio * cantidad)", COL_VENTA_TOTAL
    )
    return df


def filter_high_performance(
    df: pd.DataFrame, threshold: float = 500.0
) -> pd.DataFrame:
    """Filtra filas donde ``venta_total`` supere un umbral.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con la columna ``venta_total``.
    threshold : float
        Valor mínimo de ``venta_total`` para conservar la fila.

    Returns
    -------
    pd.DataFrame
        Filas con ``venta_total > threshold``.
    """
    antes = len(df)
    df = df.loc[df[COL_VENTA_TOTAL] > threshold].copy()
    despues = len(df)
    logger.info(
        "filter_high_performance: %d filas con venta_total > %.2f (descartadas %d)",
        despues,
        threshold,
        antes - despues,
    )
    return df


def merge_ventas_marketing(
    ventas: pd.DataFrame,
    marketing: pd.DataFrame,
    how: str = "left",
) -> pd.DataFrame:
    """Fusiona ventas con marketing usando la columna ``producto`` como clave.

    Parameters
    ----------
    ventas : pd.DataFrame
        DataFrame de ventas.
    marketing : pd.DataFrame
        DataFrame de marketing.
    how : str
        Tipo de merge: ``"left"``, ``"inner"``, ``"outer"``, etc.

    Returns
    -------
    pd.DataFrame
        Resultado del merge.
    """
    logger.info(
        "merge_ventas_marketing: %d ventas x %d marketing (how=%s)",
        len(ventas),
        len(marketing),
        how,
    )
    df = ventas.merge(marketing, on=COL_PRODUCTO, how=how, suffixes=("", "_mkt"))
    logger.info("Merge completado: %d filas", len(df))
    return df


def merge_with_clientes(
    ventas: pd.DataFrame,
    clientes: pd.DataFrame,
    how: str = "left",
) -> pd.DataFrame:
    """Fusiona ventas con clientes.

    Como no hay una clave directa entre ambos datasets, este merge
    se realiza por índice (join positional). Si en el futuro se agrega
    una columna compartida, se puede cambiar a merge por columna.

    Parameters
    ----------
    ventas : pd.DataFrame
        DataFrame de ventas (o el combinado ventas-marketing).
    clientes : pd.DataFrame
        DataFrame de clientes.
    how : str
        Tipo de join.

    Returns
    -------
    pd.DataFrame
        Resultado del merge.
    """
    logger.info(
        "merge_with_clientes: %d ventas x %d clientes (how=%s, join por índice)",
        len(ventas),
        len(clientes),
        how,
    )
    df = ventas.join(clientes, how=how, lsuffix="_venta", rsuffix="_cli")
    logger.info("Merge completado: %d filas", len(df))
    return df


def create_date_features(
    df: pd.DataFrame,
    date_col: str = COL_FECHA,
) -> pd.DataFrame:
    """Extrae características temporales de una columna datetime.

    Agrega las columnas:

    - ``mes`` (int, 1-12)
    - ``dia_semana`` (int, 0=lunes, 6=domingo)
    - ``trimestre`` (int, 1-4)

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con una columna datetime.
    date_col : str
        Nombre de la columna de fecha.

    Returns
    -------
    pd.DataFrame
        Copia con las nuevas columnas derivadas.
    """
    df = df.copy()
    if date_col not in df.columns:
        logger.warning("Columna '%s' no encontrada, se omite create_date_features", date_col)
        return df

    df["mes"] = df[date_col].dt.month
    df["dia_semana"] = df[date_col].dt.dayofweek
    df["trimestre"] = df[date_col].dt.quarter
    logger.info(
        "create_date_features: columnas 'mes', 'dia_semana', 'trimestre' creadas desde '%s'",
        date_col,
    )
    return df

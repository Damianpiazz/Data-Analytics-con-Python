"""Funciones de agregación y tabulación para DataFrames de ventas.

Incluye agrupaciones por categoría, producto, mes y la creación
de tablas dinámicas para análisis multidimensional.
"""

import pandas as pd


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Agrupa ventas por categoría y calcula métricas agregadas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de ventas. Debe tener las columnas 'categoria',
        'venta_total' y 'cantidad'.

    Returns
    -------
    pd.DataFrame
        DataFrame con columnas: categoria, venta_total_sum, cantidad_sum,
        num_transacciones, ordenado por venta_total_sum descendente.
    """
    required = {"categoria", "venta_total"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Faltan columnas requeridas: {missing}")

    agg = df.groupby("categoria").agg(
        venta_total_sum=("venta_total", "sum"),
        cantidad_sum=("cantidad", "sum") if "cantidad" in df.columns else ("venta_total", "count"),
        num_transacciones=("venta_total", "count"),
    ).reset_index()

    # Si cantidad no existe, renombramos para consistencia
    if "cantidad" not in df.columns:
        agg.rename(columns={"cantidad_sum": "cantidad_sum"}, inplace=True)
        # Como usamos count sobre venta_total, mejor dejamos num_transacciones

    agg = agg.sort_values("venta_total_sum", ascending=False).reset_index(drop=True)
    return agg


def sales_by_product(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top N productos por venta_total.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de ventas. Debe tener las columnas 'producto' y 'venta_total'.
    top_n : int, optional
        Cantidad de productos a mostrar. Por defecto 10.

    Returns
    -------
    pd.DataFrame
        DataFrame con producto, venta_total_sum, cantidad_sum,
        num_transacciones, ordenado descendente.
    """
    if "producto" not in df.columns:
        raise KeyError("El DataFrame debe tener una columna 'producto'.")

    if "venta_total" not in df.columns:
        raise KeyError("El DataFrame debe tener una columna 'venta_total'.")

    agg = df.groupby("producto").agg(
        venta_total_sum=("venta_total", "sum"),
        cantidad_sum=("cantidad", "sum") if "cantidad" in df.columns else ("venta_total", "count"),
        num_transacciones=("venta_total", "count"),
    ).reset_index()

    agg = agg.sort_values("venta_total_sum", ascending=False).head(top_n).reset_index(drop=True)
    return agg


def monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula ventas mensuales a partir de la columna 'fecha_venta'.

    Crea la columna 'mes' a partir de fecha_venta si no existe,
    y agrupa por mes.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de ventas. Debe tener 'fecha_venta' (datetime) y 'venta_total'.

    Returns
    -------
    pd.DataFrame
        DataFrame con columnas mes, venta_total_sum, cantidad_sum,
        num_transacciones, ordenado cronológicamente.
    """
    if "fecha_venta" not in df.columns:
        raise KeyError("El DataFrame debe tener una columna 'fecha_venta'.")

    df_copy = df.copy()
    df_copy["mes"] = df_copy["fecha_venta"].dt.to_period("M").astype(str)

    agg = df_copy.groupby("mes").agg(
        venta_total_sum=("venta_total", "sum"),
        cantidad_sum=("cantidad", "sum") if "cantidad" in df.columns else ("venta_total", "count"),
        num_transacciones=("venta_total", "count"),
    ).reset_index()

    agg = agg.sort_values("mes").reset_index(drop=True)
    return agg


def pivot_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Crea una tabla dinámica de ventas.

    Parámetros fijos:
    - Filas: producto
    - Columnas: categoria
    - Valores: venta_total (suma)

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de ventas con 'producto', 'categoria' y 'venta_total'.

    Returns
    -------
    pd.DataFrame
        Tabla dinámica con productos como filas y categorías como columnas.
    """
    required = {"producto", "categoria", "venta_total"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Faltan columnas requeridas: {missing}")

    pivot = df.pivot_table(
        index="producto",
        columns="categoria",
        values="venta_total",
        aggfunc="sum",
        fill_value=0,
    )

    # Agregar columna de total por producto
    pivot["total"] = pivot.sum(axis=1)
    pivot = pivot.sort_values("total", ascending=False)

    return pivot


def summary_by_channel(df: pd.DataFrame) -> pd.DataFrame:
    """Resumen de ventas por canal de marketing.

    Si el DataFrame incluye datos de campañas de marketing con columna
    'canal', agrupa y resume.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que debe tener la columna 'canal' (merge de ventas + marketing).

    Returns
    -------
    pd.DataFrame
        DataFrame con canal, venta_total_sum, cantidad_sum, num_transacciones,
        ordenado por venta_total_sum descendente.

    Raises
    ------
    KeyError
        Si no existe la columna 'canal'.
    """
    if "canal" not in df.columns:
        raise KeyError(
            "El DataFrame debe tener una columna 'canal'. "
            "Hacé un merge de ventas con la tabla de marketing primero."
        )

    agg = df.groupby("canal").agg(
        venta_total_sum=("venta_total", "sum"),
        cantidad_sum=("cantidad", "sum") if "cantidad" in df.columns else ("venta_total", "count"),
        num_transacciones=("venta_total", "count"),
        costo_total=("costo", "sum") if "costo" in df.columns else ("venta_total", "count"),
    ).reset_index()

    if "costo" in df.columns:
        # Calcular retorno por canal si tenemos costo
        agg["roi"] = ((agg["venta_total_sum"] - agg["costo_total"]) / agg["costo_total"] * 100).round(2)

    agg = agg.sort_values("venta_total_sum", ascending=False).reset_index(drop=True)
    return agg

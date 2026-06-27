"""Funciones de gráficos estáticos con matplotlib y seaborn.

Cada función recibe datos y parámetros de personalización, y devuelve
el objeto Figure de matplotlib para mostrar, guardar o modificar.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.visualization.styles import set_style, COLORS

# Aplicar estilo al importar el módulo
set_style()


def line_plot(data, x, y, title="", xlabel="", ylabel="", figsize=(10, 6)):
    """Gráfico de líneas — ideal para ventas y métricas en el tiempo.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Nombres de las columnas para los ejes X e Y.
    title, xlabel, ylabel : str
        Título y etiquetas de ejes.
    figsize : tuple
        Dimensiones de la figura (ancho, alto).

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=data, x=x, y=y, ax=ax, marker="o", linewidth=2, color=COLORS[0])
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    plt.tight_layout()
    return fig


def bar_plot(data, x, y, title="", xlabel="", ylabel="", color=COLORS[0], figsize=(10, 6)):
    """Gráfico de barras — ideal para comparar categorías.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Nombres de las columnas para los ejes.
    title, xlabel, ylabel : str
        Título y etiquetas.
    color : str
        Color de las barras (se ignora si se usa palette).
    figsize : tuple
        Dimensiones de la figura.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(data=data, x=x, y=y, ax=ax, palette="viridis", hue=x, legend=False)
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    return fig


def scatter_plot(data, x, y, hue=None, title="", xlabel="", ylabel="", figsize=(10, 6)):
    """Gráfico de dispersión — ideal para explorar correlaciones.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Columnas para los ejes.
    hue : str, optional
        Columna para colorear puntos por categoría.
    title, xlabel, ylabel : str
        Título y etiquetas.
    figsize : tuple
        Dimensiones de la figura.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(data=data, x=x, y=y, hue=hue, ax=ax, s=80, alpha=0.7)
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    plt.tight_layout()
    return fig


def box_plot(data, x, y, title="", xlabel="", ylabel="", figsize=(10, 6)):
    """Box plot — ideal para visualizar distribuciones y outliers.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Columna categórica (x) y numérica (y).
    title, xlabel, ylabel : str
        Título y etiquetas.
    figsize : tuple
        Dimensiones de la figura.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.boxplot(data=data, x=x, y=y, ax=ax, palette="viridis", hue=x, legend=False)
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    plt.tight_layout()
    return fig


def histogram(data, column, bins=30, title="", xlabel="", figsize=(10, 6)):
    """Histograma con curva KDE — ideal para distribuciones de una variable.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    column : str
        Columna numérica a analizar.
    bins : int
        Cantidad de bins del histograma.
    title, xlabel : str
        Título y etiqueta del eje X.
    figsize : tuple
        Dimensiones de la figura.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(data=data, x=column, bins=bins, kde=True, ax=ax, color=COLORS[0])
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel or column)
    ax.set_ylabel("Frecuencia")
    plt.tight_layout()
    return fig


def heatmap(corr_matrix, title="Matriz de Correlación", figsize=(8, 6)):
    """Heatmap de una matriz de correlación.

    Parameters
    ----------
    corr_matrix : pd.DataFrame
        Matriz de correlación cuadrada.
    title : str
        Título del gráfico.
    figsize : tuple
        Dimensiones de la figura.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        corr_matrix, annot=True, cmap="RdBu_r", center=0,
        fmt=".2f", linewidths=0.5, ax=ax, vmin=-1, vmax=1,
    )
    ax.set_title(title, fontweight="bold")
    plt.tight_layout()
    return fig


def pairplot(data, columns=None, hue=None):
    """Pairplot de Seaborn para explorar relaciones entre múltiples variables.

    A diferencia de las demás funciones, ésta devuelve un sns.PairGrid
    (no una Figure de matplotlib estándar).

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    columns : list, optional
        Columnas numéricas a incluir. Si es None, usa todas las numéricas.
    hue : str, optional
        Columna categórica para colorear.

    Returns
    -------
    sns.PairGrid
    """
    return sns.pairplot(
        data=data, vars=columns, hue=hue,
        palette="viridis", diag_kind="kde",
    )


def save_figure(fig, filename: str, dpi=150):
    """Guarda una figura en el directorio reports/figures/.

    Crea el directorio si no existe.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figura a guardar.
    filename : str
        Nombre del archivo (ej: 'ventas_mensuales.png').
    dpi : int
        Resolución en DPI. Por defecto 150.

    Returns
    -------
    pathlib.Path
        Ruta completa del archivo guardado.
    """
    from pathlib import Path
    import os

    figures_dir = (
        Path(__file__).resolve().parent.parent.parent / "reports" / "figures"
    )
    os.makedirs(figures_dir, exist_ok=True)

    path = figures_dir / filename
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Figura guardada: {path}")
    return path

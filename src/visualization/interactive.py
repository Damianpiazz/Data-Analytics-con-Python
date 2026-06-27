"""Gráficos interactivos con Plotly.

Cada función devuelve un objeto plotly.graph_objects.Figure que se
puede mostrar en Jupyter, guardar como HTML o incrustar en dashboards.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from src.visualization.styles import COLORS


def interactive_line(data, x, y, title="", color=None):
    """Gráfico de líneas interactivo.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Columnas para los ejes.
    title : str
        Título del gráfico.
    color : str, optional
        Columna para agrupar (múltiples líneas).

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = px.line(
        data, x=x, y=y, color=color, title=title,
        markers=True, template="plotly_white",
    )
    fig.update_layout(hovermode="x unified")
    return fig


def interactive_scatter(data, x, y, color=None, size=None, title=""):
    """Scatter plot interactivo.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Columnas para los ejes.
    color : str, optional
        Columna para colorear puntos.
    size : str, optional
        Columna para definir el tamaño de los puntos.
    title : str
        Título del gráfico.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = px.scatter(
        data, x=x, y=y, color=color, size=size,
        title=title, template="plotly_white",
        hover_data=[data.index],
    )
    return fig


def interactive_bar(data, x, y, title="", color=None):
    """Gráfico de barras interactivo.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x, y : str
        Columnas para los ejes.
    title : str
        Título del gráfico.
    color : str, optional
        Columna para agrupar barras.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = px.bar(
        data, x=x, y=y, color=color, title=title,
        template="plotly_white", barmode="group",
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig


def interactive_histogram(data, x, title="", nbins=30):
    """Histograma interactivo con box plot marginal.

    Parameters
    ----------
    data : pd.DataFrame
        Datos a graficar.
    x : str
        Columna numérica a analizar.
    title : str
        Título del gráfico.
    nbins : int
        Cantidad de bins.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = px.histogram(
        data, x=x, nbins=nbins, title=title,
        template="plotly_white", marginal="box",
    )
    return fig


def create_dashboard(data_ventas, data_categorias, data_mensual):
    """Crea un dashboard combinando múltiples gráficos en una página.

    Usa make_subplots para organizar 4 visualizaciones en una grilla 2x2:
    - Ventas mensuales (líneas)
    - Ventas por categoría (barras)
    - Distribución de precios (histograma)
    - Top productos (barras)

    Parameters
    ----------
    data_ventas : pd.DataFrame
        DataFrame de ventas completo (para histograma de precios).
    data_categorias : pd.DataFrame
        DataFrame agregado por categoría (columnas: categoria, venta_total_sum).
    data_mensual : pd.DataFrame
        DataFrame con ventas mensuales (columnas: mes, venta_total_sum).

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Ventas Mensuales",
            "Ventas por Categoría",
            "Distribución de Precios",
            "Top Productos",
        ),
        specs=[
            [{"type": "scatter"}, {"type": "bar"}],
            [{"type": "histogram"}, {"type": "bar"}],
        ],
    )

    # 1. Ventas mensuales (líneas)
    fig.add_trace(
        go.Scatter(
            x=data_mensual["mes"],
            y=data_mensual["venta_total_sum"],
            mode="lines+markers",
            name="Ventas Mensuales",
            line=dict(color=COLORS[0], width=3),
        ),
        row=1, col=1,
    )

    # 2. Ventas por categoría (barras)
    fig.add_trace(
        go.Bar(
            x=data_categorias["categoria"],
            y=data_categorias["venta_total_sum"],
            name="Por Categoría",
            marker_color=COLORS[1],
        ),
        row=1, col=2,
    )

    # 3. Distribución de precios (histograma)
    fig.add_trace(
        go.Histogram(
            x=data_ventas["precio"],
            nbinsx=30,
            name="Precios",
            marker_color=COLORS[2],
            opacity=0.75,
        ),
        row=2, col=1,
    )

    # 4. Top productos (barras)
    top_productos = (
        data_ventas.groupby("producto")["venta_total"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig.add_trace(
        go.Bar(
            x=top_productos["producto"],
            y=top_productos["venta_total"],
            name="Top Productos",
            marker_color=COLORS[3],
        ),
        row=2, col=2,
    )

    fig.update_layout(
        title_text="Dashboard de Ventas",
        template="plotly_white",
        height=800,
        showlegend=True,
    )

    return fig

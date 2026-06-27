# Módulo de visualización de datos
# Exporta las funciones principales de estilos y gráficos
from src.visualization.styles import set_style, COLORS, COLORS_CATEGORIAS
from src.visualization.plots import (
    line_plot,
    bar_plot,
    scatter_plot,
    box_plot,
    histogram,
    heatmap,
    pairplot,
    save_figure,
)
from src.visualization.interactive import (
    interactive_line,
    interactive_scatter,
    interactive_bar,
    interactive_histogram,
    create_dashboard,
)

__all__ = [
    "set_style",
    "COLORS",
    "COLORS_CATEGORIAS",
    "line_plot",
    "bar_plot",
    "scatter_plot",
    "box_plot",
    "histogram",
    "heatmap",
    "pairplot",
    "save_figure",
    "interactive_line",
    "interactive_scatter",
    "interactive_bar",
    "interactive_histogram",
    "create_dashboard",
]

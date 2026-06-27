"""Estilos, paletas y configuración global para gráficos.

Define una paleta de colores moderna y la función set_style()
para aplicar una apariencia consistente a todas las visualizaciones.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Paleta de colores personalizada — moderna, accesible y profesional
COLORS = [
    "#2E86AB",  # Azul profundo
    "#A23B72",  # Magenta
    "#F18F01",  # Naranja
    "#C73E1D",  # Rojo ladrillo
    "#3B1F2B",  # Vino tinto
    "#44BBA4",  # Verde agua
    "#E94F37",  # Rojo coral
]

COLORS_CATEGORIAS = {
    "Electrónica": "#2E86AB",
    "Electrodomésticos": "#A23B72",
    "Decoración": "#F18F01",
}


def set_style():
    """Configura el estilo global de matplotlib y seaborn.

    Aplica:
    - Fondo con grilla blanca (seaborn)
    - Paleta de colores personalizada
    - Tamaño de figura, fuente y DPI predeterminados
    """
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except OSError:
        # Fallback si el estilo no está disponible
        plt.style.use("ggplot")

    sns.set_palette(COLORS)

    plt.rcParams.update({
        "figure.figsize": (10, 6),
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "figure.dpi": 120,
    })

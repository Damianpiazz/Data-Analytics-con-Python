# Módulo de análisis estadístico
# Exporta las funciones principales para facilitar el acceso
from src.analysis.descriptive import tendencia_central, dispersion, summary_stats, detect_outliers_iqr
from src.analysis.correlations import correlation_matrix, analyze_correlations, top_correlations
from src.analysis.aggregations import (
    sales_by_category,
    sales_by_product,
    monthly_sales,
    pivot_sales,
    summary_by_channel,
)

__all__ = [
    "tendencia_central",
    "dispersion",
    "summary_stats",
    "detect_outliers_iqr",
    "correlation_matrix",
    "analyze_correlations",
    "top_correlations",
    "sales_by_category",
    "sales_by_product",
    "monthly_sales",
    "pivot_sales",
    "summary_by_channel",
]

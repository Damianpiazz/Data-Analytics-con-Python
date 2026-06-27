"""Módulo de carga, limpieza, transformación y exportación de datos."""

from src.data.loader import load_ventas, load_marketing, load_clientes, load_all_datasets
from src.data.cleaner import (
    clean_precio,
    clean_costo,
    remove_duplicates,
    handle_nulls,
    clean_all,
)
from src.data.transformer import (
    add_venta_total,
    filter_high_performance,
    merge_ventas_marketing,
    merge_with_clientes,
    create_date_features,
)
from src.data.exporter import save_processed, export_final

__all__ = [
    # loader
    "load_ventas",
    "load_marketing",
    "load_clientes",
    "load_all_datasets",
    # cleaner
    "clean_precio",
    "clean_costo",
    "remove_duplicates",
    "handle_nulls",
    "clean_all",
    # transformer
    "add_venta_total",
    "filter_high_performance",
    "merge_ventas_marketing",
    "merge_with_clientes",
    "create_date_features",
    # exporter
    "save_processed",
    "export_final",
]

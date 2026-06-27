"""Fixtures compartidas para todos los tests del proyecto.

Define DataFrames de ejemplo reutilizables en las baterías de tests
de limpieza, análisis y visualización.
"""

import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_ventas():
    """DataFrame de ventas pequeño con datos sucios (precios como string).

    Útil para tests del módulo cleaner.
    """
    return pd.DataFrame({
        "id_venta": [1, 2, 3, 4],
        "producto": ["Producto A", "Producto B", "Producto A", "Producto C"],
        "precio": ["$100.00", "$200.50", "$100.00", "$50.00"],
        "cantidad": [2, 1, 3, 5],
        "fecha_venta": pd.to_datetime(
            ["01/01/2024", "02/01/2024", "03/01/2024", "04/01/2024"]
        ),
        "categoria": ["Electrónica", "Decoración", "Electrónica", "Electrodomésticos"],
    })


@pytest.fixture
def sample_ventas_clean():
    """DataFrame de ventas ya limpias para tests de análisis.

    Incluye venta_total calculada y tipos de datos correctos.
    """
    return pd.DataFrame({
        "producto": ["A", "B", "C", "A"],
        "categoria": ["X", "Y", "X", "X"],
        "precio": [100.0, 200.0, 50.0, 100.0],
        "cantidad": [2, 1, 5, 3],
        "venta_total": [200.0, 200.0, 250.0, 300.0],
        "fecha_venta": pd.to_datetime(
            ["01/01/2024", "02/01/2024", "03/01/2024", "04/01/2024"]
        ),
    })


@pytest.fixture
def sample_marketing():
    """DataFrame de marketing pequeño para tests de aggregations."""
    return pd.DataFrame({
        "id_campanha": [101, 102, 103],
        "producto": ["A", "B", "C"],
        "canal": ["Redes Sociales", "Email", "Redes Sociales"],
        "costo": [500.0, 300.0, 200.0],
        "fecha_inicio": pd.to_datetime(["01/01/2024", "15/01/2024", "01/02/2024"]),
        "fecha_fin": pd.to_datetime(["15/01/2024", "01/02/2024", "15/02/2024"]),
    })

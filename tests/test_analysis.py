"""Tests para el módulo de análisis estadístico (src/analysis/).

Cubre funciones de estadística descriptiva, correlaciones y agregaciones.
"""

import pandas as pd
import numpy as np
import pytest


# ===========================================================================
# Tests de descriptive.py
# ===========================================================================

class TestTendenciaCentral:
    """Tests para tendencia_central()."""

    def test_tendencia_central_basico(self, sample_ventas_clean):
        """Debe calcular media, mediana y moda para columnas numéricas."""
        from src.analysis.descriptive import tendencia_central

        resultado = tendencia_central(sample_ventas_clean)

        assert "precio" in resultado
        assert "media" in resultado["precio"]
        assert "mediana" in resultado["precio"]
        assert "moda" in resultado["precio"]

        # precio: [100, 200, 50, 100] → media=112.5, mediana=100, moda=100
        assert resultado["precio"]["media"] == 112.5
        assert resultado["precio"]["mediana"] == 100.0
        assert resultado["precio"]["moda"] == 100.0

    def test_tendencia_central_columnas_especificas(self, sample_ventas_clean):
        """Debe trabajar solo con las columnas indicadas."""
        from src.analysis.descriptive import tendencia_central

        resultado = tendencia_central(sample_ventas_clean, columns=["precio"])
        assert list(resultado.keys()) == ["precio"]

    def test_tendencia_central_sin_columnas(self):
        """Si el DataFrame no tiene columnas numéricas, debe devolver dict vacío."""
        from src.analysis.descriptive import tendencia_central

        df = pd.DataFrame({"a": ["x", "y"], "b": ["m", "n"]})
        resultado = tendencia_central(df)
        assert resultado == {}

    def test_tendencia_central_con_nulls(self):
        """Debe ignorar valores nulos en los cálculos."""
        from src.analysis.descriptive import tendencia_central

        df = pd.DataFrame({"precio": [100.0, np.nan, 200.0, 100.0]})
        resultado = tendencia_central(df)
        assert resultado["precio"]["media"] == pytest.approx(133.3333, rel=1e-3)


class TestDispersion:
    """Tests para dispersion()."""

    def test_dispersion_basico(self, sample_ventas_clean):
        """Debe calcular varianza, std, rango e IQR."""
        from src.analysis.descriptive import dispersion

        resultado = dispersion(sample_ventas_clean)

        assert "precio" in resultado
        assert "varianza" in resultado["precio"]
        assert "std" in resultado["precio"]
        assert "rango" in resultado["precio"]
        assert "iqr" in resultado["precio"]

        # precio: [100, 200, 50, 100] → min=50, max=200, rango=150
        assert resultado["precio"]["min"] == 50.0
        assert resultado["precio"]["max"] == 200.0
        assert resultado["precio"]["rango"] == 150.0


class TestSummaryStats:
    """Tests para summary_stats()."""

    def test_summary_stats_incluye_iqr_rango(self, sample_ventas_clean):
        """El DataFrame devuelto debe incluir filas iqr y rango."""
        from src.analysis.descriptive import summary_stats

        resultado = summary_stats(sample_ventas_clean)

        assert "iqr" in resultado.index
        assert "rango" in resultado.index

    def test_summary_stats_solo_numericas(self):
        """Solo debe incluir columnas numéricas."""
        from src.analysis.descriptive import summary_stats

        df = pd.DataFrame({
            "a": [1, 2, 3],
            "b": ["x", "y", "z"],
        })
        resultado = summary_stats(df)
        assert "a" in resultado.columns
        assert "b" not in resultado.columns


class TestDetectOutliersIQR:
    """Tests para detect_outliers_iqr()."""

    def test_detecta_outliers(self):
        """Debe marcar correctamente valores extremos."""
        from src.analysis.descriptive import detect_outliers_iqr

        df = pd.DataFrame({"valor": [10, 12, 11, 13, 100, 9, 200]})
        resultado = detect_outliers_iqr(df, "valor")

        assert "is_outlier" in resultado.columns
        # Con pandas quantile (linear interpolation):
        # Q1=10.5, Q3=56.5, IQR=46, límites: [-58.5, 125.5]
        # Solo 200 (>125.5) es outlier; 100 está dentro del rango
        assert not resultado.loc[4, "is_outlier"]  # 100 → dentro del límite
        assert resultado.loc[6, "is_outlier"]       # 200 → outlier
        assert not resultado.loc[0, "is_outlier"]  # 10 → dentro

    def test_columna_inexistente(self):
        """Debe lanzar ValueError si la columna no existe."""
        from src.analysis.descriptive import detect_outliers_iqr

        df = pd.DataFrame({"a": [1, 2, 3]})
        with pytest.raises(ValueError):
            detect_outliers_iqr(df, "b")

    def test_columna_no_numerica(self):
        """Debe lanzar TypeError si la columna no es numérica."""
        from src.analysis.descriptive import detect_outliers_iqr

        df = pd.DataFrame({"a": ["x", "y", "z"]})
        with pytest.raises(TypeError):
            detect_outliers_iqr(df, "a")


# ===========================================================================
# Tests de correlations.py
# ===========================================================================

class TestCorrelationMatrix:
    """Tests para correlation_matrix()."""

    def test_correlation_matrix_forma(self, sample_ventas_clean):
        """La matriz debe ser cuadrada y simétrica."""
        from src.analysis.correlations import correlation_matrix

        corr = correlation_matrix(sample_ventas_clean)
        assert corr.shape[0] == corr.shape[1]
        assert corr.shape[0] >= 1

    def test_correlation_matrix_methodo_invalido(self, sample_ventas_clean):
        """Debe lanzar ValueError con método no soportado."""
        from src.analysis.correlations import correlation_matrix

        with pytest.raises(ValueError):
            correlation_matrix(sample_ventas_clean, method="magico")

    def test_correlation_matrix_solo_numericas(self):
        """Solo debe incluir columnas numéricas."""
        from src.analysis.correlations import correlation_matrix

        df = pd.DataFrame({
            "a": [1.0, 2.0, 3.0],
            "b": [4.0, 5.0, 6.0],
            "c": ["x", "y", "z"],
        })
        corr = correlation_matrix(df)
        assert list(corr.columns) == ["a", "b"]


class TestAnalyzeCorrelations:
    """Tests para analyze_correlations()."""

    def test_analyze_correlations_estructura(self, sample_ventas_clean):
        """Debe devolver dict con fuertes_positivas y fuertes_negativas."""
        from src.analysis.correlations import analyze_correlations

        resultado = analyze_correlations(sample_ventas_clean, threshold=0.0)
        assert "fuertes_positivas" in resultado
        assert "fuertes_negativas" in resultado

    def test_analyze_correlations_threshold_alto(self):
        """Con threshold=0.99 encuentra los pares perfectamente correlacionados."""
        from src.analysis.correlations import analyze_correlations

        df = pd.DataFrame({
            "a": [1.0, 2.0, 3.0],
            "b": [4.0, 5.0, 6.0],
            "c": [7.0, 8.0, 9.0],
        })
        resultado = analyze_correlations(df, threshold=0.99)
        # a/b/c están perfectamente correlacionados (r=1.0) → los 3 pares
        assert len(resultado["fuertes_positivas"]) == 3
        assert len(resultado["fuertes_negativas"]) == 0


class TestTopCorrelations:
    """Tests para top_correlations()."""

    def test_top_correlations_cantidad(self, sample_ventas_clean):
        """Debe devolver exactamente n pares (o menos si no hay suficientes)."""
        from src.analysis.correlations import correlation_matrix, top_correlations

        corr = correlation_matrix(sample_ventas_clean)
        pares = top_correlations(corr, n=3)
        assert len(pares) <= 3
        assert all(len(p) == 3 for p in pares)

    def test_top_correlations_excluye_diagonal(self):
        """No debe incluir la diagonal (correlación de una variable consigo misma)."""
        from src.analysis.correlations import correlation_matrix, top_correlations

        df = pd.DataFrame({
            "a": [1.0, 2.0, 3.0],
            "b": [4.0, 5.0, 6.0],
        })
        corr = correlation_matrix(df)
        pares = top_correlations(corr, n=5)
        for v1, v2, _ in pares:
            assert v1 != v2


# ===========================================================================
# Tests de aggregations.py
# ===========================================================================

class TestSalesByCategory:
    """Tests para sales_by_category()."""

    def test_sales_by_category_resultado(self, sample_ventas_clean):
        """Debe agrupar por categoría y sumar venta_total."""
        from src.analysis.aggregations import sales_by_category

        resultado = sales_by_category(sample_ventas_clean)

        assert "categoria" in resultado.columns
        assert "venta_total_sum" in resultado.columns
        assert "num_transacciones" in resultado.columns

        # Categoría X: productos A, C, A → total = 200 + 250 + 300 = 750
        fila_x = resultado[resultado["categoria"] == "X"]
        assert fila_x["venta_total_sum"].iloc[0] == 750.0

    def test_sales_by_category_faltante(self):
        """Debe lanzar KeyError si falta una columna requerida."""
        from src.analysis.aggregations import sales_by_category

        df = pd.DataFrame({"otra": [1, 2]})
        with pytest.raises(KeyError):
            sales_by_category(df)


class TestSalesByProduct:
    """Tests para sales_by_product()."""

    def test_sales_by_product_top(self, sample_ventas_clean):
        """Debe devolver el top N productos ordenados."""
        from src.analysis.aggregations import sales_by_product

        resultado = sales_by_product(sample_ventas_clean, top_n=2)

        assert len(resultado) == 2
        # A: 500, C: 250, B: 200 → top 2 son A y C
        assert resultado["producto"].iloc[0] == "A"

    def test_sales_by_product_sin_columna(self):
        """Debe lanzar KeyError si falta producto o venta_total."""
        from src.analysis.aggregations import sales_by_product

        df = pd.DataFrame({"x": [1]})
        with pytest.raises(KeyError):
            sales_by_product(df)


class TestMonthlySales:
    """Tests para monthly_sales()."""

    def test_monthly_sales_agrupa_por_mes(self, sample_ventas_clean):
        """Debe agrupar correctamente por mes."""
        from src.analysis.aggregations import monthly_sales

        resultado = monthly_sales(sample_ventas_clean)

        assert "mes" in resultado.columns
        assert "venta_total_sum" in resultado.columns
        # El fixture tiene datos en 4 meses distintos (ene-abr 2024)
        assert len(resultado) == 4
        assert "2024-01" in resultado["mes"].values
        assert "2024-04" in resultado["mes"].values

    def test_monthly_sales_sin_fecha(self):
        """Debe lanzar KeyError si falta fecha_venta."""
        from src.analysis.aggregations import monthly_sales

        df = pd.DataFrame({"x": [1]})
        with pytest.raises(KeyError):
            monthly_sales(df)


class TestPivotSales:
    """Tests para pivot_sales()."""

    def test_pivot_sales_forma(self, sample_ventas_clean):
        """Debe crear una tabla dinámica con productos como filas."""
        from src.analysis.aggregations import pivot_sales

        pivot = pivot_sales(sample_ventas_clean)

        assert "total" in pivot.columns
        assert pivot.index.name == "producto"

    def test_pivot_sales_faltante(self):
        """Debe lanzar KeyError si falta una columna."""
        from src.analysis.aggregations import pivot_sales

        df = pd.DataFrame({"x": [1]})
        with pytest.raises(KeyError):
            pivot_sales(df)


class TestSummaryByChannel:
    """Tests para summary_by_channel()."""

    def test_summary_by_channel_con_canal(self, sample_ventas_clean):
        """Debe agrupar por canal si la columna existe."""
        from src.analysis.aggregations import summary_by_channel

        df = sample_ventas_clean.copy()
        df["canal"] = ["Redes Sociales", "Email", "Redes Sociales", "Email"]
        df["costo"] = [100.0, 50.0, 150.0, 80.0]

        resultado = summary_by_channel(df)

        assert "canal" in resultado.columns
        assert "roi" in resultado.columns or "roi" in resultado.columns
        assert len(resultado) == 2  # Dos canales

    def test_summary_by_channel_sin_canal(self, sample_ventas_clean):
        """Debe lanzar KeyError si no existe la columna canal."""
        from src.analysis.aggregations import summary_by_channel

        with pytest.raises(KeyError):
            summary_by_channel(sample_ventas_clean)

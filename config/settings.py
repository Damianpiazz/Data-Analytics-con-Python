"""Configuración central del proyecto.

Define rutas absolutas y constantes de columnas para evitar
strings hardcodeados en el resto del pipeline.
"""

from pathlib import Path

# ── Rutas base ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
INTERIM_DATA_DIR = DATA_DIR / "interim"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
DASHBOARD_DIR = REPORTS_DIR / "dashboard"

# ── Archivos raw ────────────────────────────────────────────────────────────
VENTAS_FILE = RAW_DATA_DIR / "ventas.csv"
MARKETING_FILE = RAW_DATA_DIR / "marketing.csv"
CLIENTES_FILE = RAW_DATA_DIR / "clientes.csv"

# ── Archivos procesados ─────────────────────────────────────────────────────
VENTAS_PROCESSED = PROCESSED_DATA_DIR / "ventas_processed.csv"
MARKETING_PROCESSED = PROCESSED_DATA_DIR / "marketing_processed.csv"
CLIENTES_PROCESSED = PROCESSED_DATA_DIR / "clientes_processed.csv"
FINAL_DATASET = PROCESSED_DATA_DIR / "dataset_final.csv"

# ── Columnas: ventas ────────────────────────────────────────────────────────
COL_VENTA_ID = "id_venta"
COL_PRODUCTO = "producto"
COL_PRECIO = "precio"
COL_CANTIDAD = "cantidad"
COL_FECHA = "fecha_venta"
COL_CATEGORIA = "categoria"
COL_VENTA_TOTAL = "venta_total"

# ── Columnas: marketing ─────────────────────────────────────────────────────
COL_CAMPAIGN_ID = "id_campanha"
COL_CANAL = "canal"
COL_COSTO = "costo"
COL_FECHA_INICIO = "fecha_inicio"
COL_FECHA_FIN = "fecha_fin"

# ── Columnas: clientes ──────────────────────────────────────────────────────
COL_CLIENTE_ID = "id_cliente"
COL_INGRESOS = "ingresos"
COL_CIUDAD = "ciudad"
COL_EDAD = "edad"

"""Carga de datasets raw desde archivos CSV.

Cada función acepta una ruta opcional para facilitar tests
y usa las rutas de ``config.settings`` por defecto.
"""

import pandas as pd
from config.logging_config import get_module_logger
from config.settings import (
    VENTAS_FILE,
    MARKETING_FILE,
    CLIENTES_FILE,
    COL_FECHA,
    COL_FECHA_INICIO,
    COL_FECHA_FIN,
)

logger = get_module_logger(__name__)


def load_ventas(path: str | None = None) -> pd.DataFrame:
    """Carga el archivo de ventas y parsea ``fecha_venta`` como datetime.

    Parameters
    ----------
    path : str | None
        Ruta al CSV. Si es ``None`` se usa ``settings.VENTAS_FILE``.

    Returns
    -------
    pd.DataFrame
        Datos de ventas con la columna ``fecha_venta`` en tipo datetime.
    """
    path = path or VENTAS_FILE
    logger.info("Cargando ventas desde %s", path)
    df = pd.read_csv(path, encoding="utf-8")
    df[COL_FECHA] = pd.to_datetime(df[COL_FECHA], format="%d/%m/%Y", dayfirst=True)
    logger.info("Ventas cargadas: %d filas x %d columnas", df.shape[0], df.shape[1])
    return df


def load_marketing(path: str | None = None) -> pd.DataFrame:
    """Carga el archivo de marketing y parsea fechas como datetime.

    Parameters
    ----------
    path : str | None
        Ruta al CSV. Si es ``None`` se usa ``settings.MARKETING_FILE``.

    Returns
    -------
    pd.DataFrame
        Datos de marketing con ``fecha_inicio`` y ``fecha_fin`` en datetime.
    """
    path = path or MARKETING_FILE
    logger.info("Cargando marketing desde %s", path)
    df = pd.read_csv(path, encoding="utf-8")
    df[COL_FECHA_INICIO] = pd.to_datetime(
        df[COL_FECHA_INICIO], format="%d/%m/%Y", dayfirst=True
    )
    df[COL_FECHA_FIN] = pd.to_datetime(
        df[COL_FECHA_FIN], format="%d/%m/%Y", dayfirst=True
    )
    logger.info("Marketing cargado: %d filas x %d columnas", df.shape[0], df.shape[1])
    return df


def load_clientes(path: str | None = None) -> pd.DataFrame:
    """Carga el archivo de clientes (no necesita parseo especial).

    Parameters
    ----------
    path : str | None
        Ruta al CSV. Si es ``None`` se usa ``settings.CLIENTES_FILE``.

    Returns
    -------
    pd.DataFrame
        Datos de clientes.
    """
    path = path or CLIENTES_FILE
    logger.info("Cargando clientes desde %s", path)
    df = pd.read_csv(path, encoding="utf-8")
    logger.info("Clientes cargados: %d filas x %d columnas", df.shape[0], df.shape[1])
    return df


def load_all_datasets() -> dict[str, pd.DataFrame]:
    """Carga los tres datasets raw en un solo paso.

    Returns
    -------
    dict[str, pd.DataFrame]
        Diccionario con las claves ``'ventas'``, ``'marketing'`` y ``'clientes'``.
    """
    logger.info("=== Cargando todos los datasets ===")
    return {
        "ventas": load_ventas(),
        "marketing": load_marketing(),
        "clientes": load_clientes(),
    }

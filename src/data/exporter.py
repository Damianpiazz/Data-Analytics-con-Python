"""Exportación de DataFrames a CSV.

Las funciones garantizan que el directorio de destino existe
antes de escribir y devuelven la ruta absoluta del archivo generado.
"""

import pandas as pd
from pathlib import Path
from config.logging_config import get_module_logger

logger = get_module_logger(__name__)


def save_processed(df: pd.DataFrame, path: Path, index: bool = False) -> str:
    """Guarda un DataFrame como CSV en la ruta indicada.

    Crea el directorio padre si no existe. Loggea la operación
    y devuelve la ruta absoluta del archivo generado.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a guardar.
    path : Path
        Ruta de salida (archivo .csv).
    index : bool
        Si es ``True`` incluye el índice de pandas como columna.

    Returns
    -------
    str
        Ruta absoluta del archivo guardado.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index, encoding="utf-8-sig")
    logger.info("Guardado: %s (%d filas)", path, len(df))
    return str(path.resolve())


def export_final(df: pd.DataFrame, path: Path) -> str:
    """Exporta el dataset final listo para presentación/análisis.

    Es un wrapper sobre ``save_processed`` con index=False por defecto.
    Se usa para el dataset consolidado final del pipeline.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset final.
    path : Path
        Ruta de salida.

    Returns
    -------
    str
        Ruta absoluta del archivo guardado.
    """
    logger.info("Exportando dataset final a %s", path)
    return save_processed(df, path, index=False)

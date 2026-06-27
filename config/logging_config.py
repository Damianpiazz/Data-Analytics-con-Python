"""Configuración de logging del proyecto.

Escribe en consola y en un archivo rotativo dentro de reports/.
Todos los módulos del pipeline deben obtener su logger via
`logging.getLogger(__name__)`.
"""

import logging
import sys
from pathlib import Path
from config.settings import REPORTS_DIR


def setup_logging(
    level: int = logging.INFO,
    log_file: str | None = None,
) -> logging.Logger:
    """Configura el logging raíz del proyecto.

    Parameters
    ----------
    level : int
        Nivel mínimo de logging (default: logging.INFO).
    log_file : str | None
        Nombre del archivo de log. Si es None se usa ``pipeline.log``.

    Returns
    -------
    logging.Logger
        Logger raíz ya configurado.
    """
    if log_file is None:
        log_file = "pipeline.log"

    log_path = REPORTS_DIR / log_file
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Formato: 2024-01-15 14:30:00,123 - modulo - LEVEL - Mensaje
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Handler: archivo (sobrescribe en cada ejecución)
    file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # Handler: consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Evitar duplicar handlers si se llama más de una vez
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

    return root_logger


def get_module_logger(name: str) -> logging.Logger:
    """Devuelve un logger para un módulo específico.

    Parameters
    ----------
    name : str
        Nombre del módulo (generalmente ``__name__``).

    Returns
    -------
    logging.Logger
    """
    return logging.getLogger(name)

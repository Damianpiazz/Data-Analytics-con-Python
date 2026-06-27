"""Utilidades varias para el pipeline y notebooks.

Incluye creación segura de directorios, un decorador ``timer``
para medir tiempos de ejecución y ``print_section`` para
separar visualmente secciones en notebooks o consola.
"""

import os
import time
import functools
from pathlib import Path
from config.logging_config import get_module_logger

logger = get_module_logger(__name__)


def ensure_dir(path: str | Path) -> Path:
    """Crea un directorio y todos sus padres si no existen.

    Parameters
    ----------
    path : str | Path
        Ruta del directorio a crear.

    Returns
    -------
    Path
        Objeto Path del directorio (existente o recién creado).
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    logger.debug("Directorio asegurado: %s", path)
    return path


def timer(func):
    """Decorador que mide y loggea el tiempo de ejecución de una función.

    Uso::

        @timer
        def mi_funcion():
            ...

    Parameters
    ----------
    func : callable
        Función a decorar.

    Returns
    -------
    callable
        Función envuelta que imprime el tiempo transcurrido.
    """

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(
            "[TIMER] %s ejecutada en %.4f segundos", func.__name__, elapsed
        )
        return value

    return wrapper_timer


def print_section(title: str, width: int = 70, char: str = "=") -> None:
    """Imprime un título de sección con bordes para separar visualmente.

    Útil en notebooks o salida de consola para agrupar pasos del pipeline.

    Parameters
    ----------
    title : str
        Título de la sección.
    width : int
        Ancho total de la línea (default: 70).
    char : str
        Carácter para el borde (default: ``"="``).
    """
    border = char * width
    padded = f" {title} ".center(width, char)
    print(f"\n{border}\n{padded}\n{border}\n")

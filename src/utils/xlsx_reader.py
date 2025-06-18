"""Модуль для чтения Excel-файла с транзакциями."""

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def load_transactions(file_path: str = "data/operations.xlsx") -> pd.DataFrame:
    """Загружает Excel-файл в DataFrame и обрабатывает названия столбцов."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    logger.info("Loading transactions from Excel file...")
    df = pd.read_excel(path)
    return df

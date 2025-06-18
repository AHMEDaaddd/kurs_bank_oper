"""Модуль генерации отчётов по транзакциям: по категориям, дням недели и типу дня."""

import logging

import pandas as pd

from src.utils.xlsx_reader import load_transactions

logger = logging.getLogger(__name__)


def spending_by_category() -> pd.DataFrame:
    """Возвращает сумму трат по категориям из таблицы операций."""
    logger.info("Генерация отчета: траты по категориям")
    df = load_transactions()
    df = df[df["Сумма операции"] < 0]
    result = df.groupby("Категория")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_weekday() -> pd.DataFrame:
    """Возвращает сумму трат по дням недели из таблицы операций."""
    logger.info("Генерация отчета: траты по дням недели")
    df = load_transactions()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["День недели"] = df["Дата операции"].dt.day_name()
    result = df.groupby("День недели")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_workday() -> pd.DataFrame:
    """Возвращает сумму трат по рабочим и выходным дням."""
    logger.info("Генерация отчета: траты по рабочим/выходным дням")
    df = load_transactions()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["Тип дня"] = df["Дата операции"].dt.weekday.apply(lambda x: "Рабочий" if x < 5 else "Выходной")
    result = df.groupby("Тип дня")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")

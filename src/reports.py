"""Модуль генерации отчётов по транзакциям: по категориям, дням недели и типу дня."""

import logging
from typing import Optional

import pandas as pd

from src.utils.xlsx_reader import load_transactions

logger = logging.getLogger(__name__)


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Возвращает сумму трат по переданной категории.

    Если указана дата — фильтрует операции в рамках месяца до этой даты.
    """
    logger.info("Генерация отчета: траты по категории '%s'", category)

    df = transactions.copy()
    df = df[df["Сумма операции"] < 0]
    df = df[df["Категория"] == category]

    if date:
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
        end_date = pd.to_datetime(date, dayfirst=True)
        start_date = end_date.replace(day=1)
        df = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]

    result = df.groupby("Категория")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_weekday(transactions: pd.DataFrame) -> pd.DataFrame:
    """Возвращает сумму трат по дням недели (понедельник, вторник и т.д.)."""
    logger.info("Генерация отчета: траты по дням недели")

    df = transactions.copy()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["День недели"] = df["Дата операции"].dt.day_name()

    result = df.groupby("День недели")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_workday(transactions: pd.DataFrame) -> pd.DataFrame:
    """Возвращает сумму трат по типу дня: Рабочий или Выходной."""
    logger.info("Генерация отчета: траты по рабочим/выходным дням")

    df = transactions.copy()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["Тип дня"] = df["Дата операции"].dt.weekday.apply(lambda x: "Рабочий" if x < 5 else "Выходной")

    result = df.groupby("Тип дня")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")

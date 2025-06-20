"""Модуль генерации отчётов по транзакциям: по категориям, дням недели и типу дня."""

import logging
from datetime import datetime
from typing import Optional

import pandas as pd
from pandas.tseries.offsets import DateOffset

from src.utils.report_saver import save_report
from src.utils.xlsx_reader import load_transactions

logger = logging.getLogger(__name__)


@save_report()  # или @save_report("my_filename.json") для именованного файла
def spending_by_category(
    transactions: pd.DataFrame | None = None, category: str | None = None, date: str | None = None
) -> pd.DataFrame:
    """
    Возвращает сумму трат по категориям за последние 3 месяца до указанной даты.

    Если дата не передана, используется текущая.
    """
    logger.info("Генерация отчета: траты по категориям (за последние 3 месяца)")
    df = transactions if transactions is not None else load_transactions()
    df = df[df["Сумма операции"] < 0].copy()
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)

    if date:
        end_date = pd.to_datetime(date, dayfirst=True)
    else:
        end_date = pd.Timestamp.now()

    start_date = end_date - DateOffset(months=3)
    df_filtered = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]

    if category:
        df_filtered = df_filtered[df_filtered["Категория"] == category]

    result = df_filtered.groupby("Категория")["Сумма операции"].sum().sort_values()
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

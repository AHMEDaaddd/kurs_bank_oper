"""Модуль с функциями для отображения JSON-ответов на главной странице."""

import logging
from datetime import datetime

import pandas as pd

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)


def get_greeting(date_time: str) -> str:
    """Возвращает приветствие в зависимости от времени суток."""
    hour = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").hour
    if 5 <= hour < 12:
        return "Доброе утро"# Это вспомогательные функции для отображения
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    return "Доброй ночи"


def get_cards_summary(df: pd.DataFrame) -> list:
    """Возвращает список карт, трат и кешбэка по каждой из них."""
    result = []
    grouped = df.groupby("Номер карты")
    for card, group in grouped:
        spent = group["Сумма платежа"].sum()
        cashback = spent * 0.01
        result.append({"last_digits": str(card)[-4:], "total_spent": round(spent, 2), "cashback": round(cashback, 2)})
    return result


def get_top_transactions(df: pd.DataFrame, top_n: int = 5) -> list:
    """Возвращает топ-N транзакций по сумме платежа."""
    df_sorted = df.sort_values(by="Сумма платежа", ascending=False).head(top_n)
    return [
        {
            "date": pd.to_datetime(row["Дата операции"], dayfirst=True).strftime("%d.%m.%Y"),
            "amount": round(row["Сумма платежа"], 2),
            "category": row["Категория"],
            "description": row["Описание"],
        }
        for _, row in df_sorted.iterrows()
    ]

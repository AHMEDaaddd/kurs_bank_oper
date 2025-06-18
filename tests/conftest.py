"""Фикстуры для модульных тестов."""

from io import StringIO

import pandas as pd
import pytest


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Возвращает пример DataFrame с транзакциями для тестов."""
    data = StringIO(
        """Дата операции,Категория,Сумма платежа,Описание
2021-12-01,Продукты,-500,Покупка в магазине
2021-12-10,Транспорт,-150,Метро
2021-12-17,Кафе,-800,Ужин в ресторане
2021-11-25,Подарки,-2000,Подарок другу"""
    )
    df = pd.read_csv(data, parse_dates=["Дата операции"])

    return df

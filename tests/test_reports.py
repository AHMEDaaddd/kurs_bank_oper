from typing import Any

import pandas as pd
from pandas import DataFrame

from src.reports import spending_by_category, spending_by_weekday, spending_by_workday


def test_spending_by_category(sample_df: DataFrame) -> None:
    result = spending_by_category(sample_df, "Продукты")
    assert isinstance(result, pd.DataFrame)
    assert not result.empty


def test_spending_by_weekday(sample_df: DataFrame) -> None:
    result = spending_by_weekday(sample_df)
    assert isinstance(result, pd.DataFrame)
    assert result["Сумма операции"].sum() < 0


def test_spending_by_workday(sample_df: DataFrame) -> None:
    result = spending_by_workday(sample_df)
    assert "Рабочий" in result.index or "Выходной" in result.index
    assert result["Сумма операции"].sum() < 0

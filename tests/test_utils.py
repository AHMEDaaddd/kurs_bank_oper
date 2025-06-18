from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd
import pytest
from pandas import DataFrame

from src.user_settings import get_user_settings
from src.utils.api_client import get_currency_rates
from src.utils.views_helpers import get_top_transactions
from src.utils.xlsx_reader import load_transactions


def test_load_transactions() -> None:
    df = load_transactions("data/operations.xlsx")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


@patch("src.utils.xlsx_reader.load_transactions")
def test_get_top_transactions_logic(mock_df: Any, sample_df: DataFrame) -> None:
    mock_df.return_value = sample_df.to_dict(orient="records")
    df = pd.DataFrame(sample_df.to_dict(orient="records"))
    result = get_top_transactions(df)
    assert isinstance(result, list)
    assert all("description" in tx for tx in result)


@patch("requests.get")
def test_get_currency_rates(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"rates": {"USD": 90.5, "EUR": 98.1}, "base": "RUB"}
    mock_get.return_value.status_code = 200
    result = get_currency_rates()
    assert any(x["currency"] == "USD" for x in result)


@patch("builtins.open", new_callable=mock_open, read_data='{"currency": "RUB"}')
def test_get_user_settings_file(mock_file: Any) -> None:
    settings = get_user_settings()
    assert isinstance(settings, dict)
    assert settings.get("currency") == "RUB"

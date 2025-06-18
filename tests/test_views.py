import json
from typing import Any
from unittest.mock import patch

from pandas import DataFrame

from src.views import get_greeting, main_view


def test_get_greeting() -> None:
    assert get_greeting("2025-05-28 08:00:00") == "Доброе утро"
    assert get_greeting("2025-05-28 14:00:00") == "Добрый день"
    assert get_greeting("2025-05-28 20:00:00") == "Добрый вечер"
    assert get_greeting("2025-05-28 02:00:00") == "Доброй ночи"


@patch("src.utils.xlsx_reader.load_transactions")
def test_main_view_returns_data(mock_get_df: Any, sample_df: DataFrame) -> None:
    mock_get_df.return_value = sample_df.to_dict(orient="records")
    result = json.loads(main_view("2021-12-17 01:02:03"))
    assert "top_transactions" in result
    assert isinstance(result["top_transactions"], list)

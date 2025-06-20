from typing import Any, Dict, List

import pytest

from src.services import filter_by_currency, find_by_description


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"Сумма операции": 100, "Валюта": "RUB", "Описание": "Оплата", "Категория": "Магазин"},
        {"Сумма операции": 200, "Валюта": "USD", "Описание": "Покупка", "Категория": "Супермаркет"},
        {"Сумма операции": 300, "Валюта": "EUR", "Описание": "оплата услуг", "Категория": "Онлайн"},
    ]


@pytest.mark.parametrize(
    "currency,expected_count",
    [
        ("RUB", 1),
        ("usd", 1),
        ("EUR", 1),
        ("GBP", 0),
    ],
)
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency: str, expected_count: int) -> None:
    result = filter_by_currency(sample_transactions, currency)
    assert isinstance(result, str)
    assert result.count("{") == expected_count


def test_find_by_description_exact(sample_transactions: List[Dict[str, Any]]) -> None:
    result = find_by_description(sample_transactions, "Оплата")
    assert "Оплата" in result


def test_find_by_description_partial(sample_transactions: List[Dict[str, Any]]) -> None:
    result = find_by_description(sample_transactions, "оплата")
    assert "оплата" in result or "Оплата" in result

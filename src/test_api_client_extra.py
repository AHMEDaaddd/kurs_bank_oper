from unittest.mock import MagicMock, patch

from src.utils.api_client import get_currency_rates, get_stock_prices


@patch("requests.get")
def test_get_currency_rates_failure(mock_get: MagicMock) -> None:
    mock_get.return_value.raise_for_status.side_effect = Exception("API error")
    result = get_currency_rates()
    assert isinstance(result, list)
    assert result[0]["rate"] == 0.0


def test_get_stock_prices_result() -> None:
    result = get_stock_prices()
    assert isinstance(result, list)

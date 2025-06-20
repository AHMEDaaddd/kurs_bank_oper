import json
from typing import Any, Dict, List, cast

from src.main import main_view
from src.reports import spending_by_category
from src.services import simple_search
from src.utils.xlsx_reader import load_transactions


def test_main_view_result() -> None:
    result = json.loads(main_view("2021-12-17 01:02:03"))
    assert isinstance(result, dict)
    assert "greeting" in result


def test_simple_search_integration() -> None:
    transactions = cast(List[Dict[str, Any]], load_transactions().to_dict(orient="records"))
    result = simple_search("оплата", transactions)
    assert isinstance(result, str)


def test_spending_by_category_integration() -> None:
    df = load_transactions()
    result = spending_by_category(df, "Продукты")
    assert hasattr(result, "index")

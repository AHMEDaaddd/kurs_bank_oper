"""Точка входа в приложение. Демонстрирует работу веб-страницы, сервиса и отчёта."""

from typing import Any, cast

from src.reports import spending_by_category
from src.services import simple_search
from src.utils.xlsx_reader import load_transactions
from src.views import main_view

# Загружаем данные
transactions = cast(list[dict[str, Any]], load_transactions().to_dict(orient="records"))

if __name__ == "__main__":
    print("Веб-страница:")
    print(main_view("2021-12-17 01:02:03"))

    print("\nСервис (поиск по описанию):")
    print(simple_search("оплата", transactions))

    print("\nОтчёт (траты по категориям):")
    df = load_transactions()  # уже есть вызов
    print(spending_by_category(df, "Продукты"))

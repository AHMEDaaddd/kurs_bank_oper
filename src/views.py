"""Модуль обработки веб-страницы: собирает JSON-ответ с транзакциями, курсами валют и акциями."""

import json

import pandas as pd

from src.utils.api_client import get_currency_rates, get_stock_prices
from src.utils.views_helpers import get_cards_summary, get_greeting, get_top_transactions, logger
from src.utils.xlsx_reader import load_transactions


def main_view(date_time: str) -> str:
    """Формирует JSON-ответ с данными: приветствие, карты, топ транзакций, валюты и акции."""
    logger.info("Loading transactions...")
    df = load_transactions()
    df = df[pd.to_datetime(df["Дата операции"], dayfirst=True) <= pd.to_datetime(date_time)]

    logger.info("Generating greeting...")
    greeting = get_greeting(date_time)

    logger.info("Generating cards summary...")
    cards = get_cards_summary(df)

    logger.info("Getting top transactions...")
    top = get_top_transactions(df)

    logger.info("Fetching currency rates and stock prices...")
    currencies = get_currency_rates()
    stocks = get_stock_prices()

    response = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top,
        "currency_rates": currencies,
        "stock_prices": stocks,
    }

    return json.dumps(response, ensure_ascii=False, indent=2)

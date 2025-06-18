from src.services import search_phone_numbers, search_private_transfers, simple_search


def test_simple_search() -> None:
    data = [{"Описание": "Ozon", "Категория": "Онлайн-магазины"}]
    result = simple_search("ozon", data)
    assert "Ozon" in result


def test_search_phone_numbers() -> None:
    data = [{"Описание": "Позвони +7 999 123-45-67"}]
    result = search_phone_numbers(data)
    assert "+7" in result


def test_search_private_transfers() -> None:
    data = [{"Категория": "Переводы", "Описание": "Владимир И."}]
    result = search_private_transfers(data)
    assert "Владимир" in result

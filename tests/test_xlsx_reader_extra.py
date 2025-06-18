import pytest

from src.utils.xlsx_reader import load_transactions


def test_load_transactions_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        load_transactions("data/missing.xlsx")

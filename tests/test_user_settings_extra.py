import pytest

from src.user_settings import get_user_settings


def test_get_user_settings_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        get_user_settings("nonexistent.json")

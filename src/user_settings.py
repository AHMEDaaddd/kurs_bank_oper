"""Модуль для загрузки пользовательских настроек из JSON."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)


def get_user_settings(path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
    """Загружает пользовательские настройки из JSON-файла."""
    if path is None:
        # Путь по умолчанию — корень проекта, рядом с pyproject.toml
        path = Path(__file__).resolve().parent.parent / "user_settings.json"
    else:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Файл настроек не найден: {path}")

    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return dict(data)

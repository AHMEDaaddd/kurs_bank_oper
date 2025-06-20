"""Модуль-декоратор для сохранения отчётов в JSON-файл."""
import json
import os
from datetime import datetime
from functools import wraps
from typing import Callable, Optional
from typing import Any

def save_report(file_name: Optional[str] = None) -> Callable:
    """Декоратор для сохранения результата функции в JSON-файл.

    Можно указать имя файла, либо использовать автоимя по умолчанию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            default_file_name = file_name or f"report_{func.__name__}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            output_path = os.path.join("spending_by_category_output.json") if not file_name else default_file_name

            try:
                result_dict = result.to_dict() if hasattr(result, "to_dict") else result
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result_dict, f, indent=4, ensure_ascii=False)
            except Exception as e:
                print(f"Ошибка при сохранении отчета: {e}")
            return result

        return wrapper

    return decorator

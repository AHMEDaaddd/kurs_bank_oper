# 📊 Анализ банковских транзакций

Этот проект позволяет анализировать банковские операции из Excel-файла. Реализованы три основные задачи:

- 🌐 Веб-страница (main_view): отображает топ транзакций с начала месяца до заданной даты.
- ⚙️ Сервис (simple_search): поиск операций по описанию.
- 📈 Отчёт (spending_by_category): анализ трат по категориям.

## 🚀 Как запустить

```bash
poetry install
poetry run python src/main.py
```

## ✅ Проверки качества кода

```bash
poetry run flake8 src
poetry run black --check src
poetry run isort --check src
poetry run mypy src
poetry run pytest
```

## 📂 Структура проекта

```
├── data/                    # Файлы операций (.xlsx)
├── src/
│   ├── main.py             # Точка входа
│   ├── views.py            # Веб-страница
│   ├── services.py         # Сервисы
│   ├── reports.py          # Отчёты
│   └── utils/              # Вспомогательные модули
├── tests/                  # Pytest-тесты
├── .env_template           # Шаблон переменных окружения
├── pyproject.toml          # Настройки Poetry и зависимостей
```

## 🔐 Переменные окружения

См. файл `.env_template`.

## 🧪 Тесты

```bash
poetry run pytest
```

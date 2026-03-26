import pytest
from unittest.mock import MagicMock
import requests


@pytest.fixture
def sample_transactions():
    return [
        {
            "Дата операции": "2021-12-10",
            "Сумма операции": 120,
            "Описание": "МТС +7 921 11-22-33",
            "Категория": "Связь",
        },
        {
            "Дата операции": "2021-12-11",
            "Сумма операции": 180,
            "Описание": "Перевод Иван И.",
            "Категория": "Переводы",
        },
    ]


@pytest.fixture
def mock_get(monkeypatch):
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"RUB": 100}}

    # патчим requests.get сразу на фиктивный ответ
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock_response)

    return mock_response
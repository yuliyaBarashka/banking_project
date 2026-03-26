from unittest.mock import patch
from src.api import get_currency_rates

"src.api.requests.get"


def test_currency(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {"RUB": 100}
    }

    result = get_currency_rates(["USD"])
    assert result[0]["rate"] == 100

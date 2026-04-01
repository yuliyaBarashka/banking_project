from unittest.mock import patch

from src.api import get_currency_rates, get_stock_prices


@patch("src.api.requests.get")
def test_get_currency_rates_success(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {"RUB": 100}
    }

    result = get_currency_rates(["USD"])

    assert result == [{"currency": "USD", "rate": 100}]


@patch("src.api.requests.get")
def test_get_currency_rates_multiple(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {"RUB": 90}
    }

    result = get_currency_rates(["USD", "EUR"])

    assert len(result) == 2
    assert result[0]["rate"] == 90
    assert result[1]["rate"] == 90


@patch("src.api.requests.get")
def test_get_currency_rates_exception(mock_get):
    mock_get.side_effect = Exception("API error")

    result = get_currency_rates(["USD"])

    assert result == [{"currency": "USD", "rate": None}]


@patch("src.api.requests.get")
def test_get_currency_rates_no_rub(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {}
    }

    result = get_currency_rates(["USD"])

    assert result[0]["rate"] is None


def test_get_currency_rates_empty():
    result = get_currency_rates([])

    assert result == []


def test_get_stock_prices():
    result = get_stock_prices(["AAPL", "GOOGL"])

    assert len(result) == 2
    assert result[0]["price"] == 100.0


def test_get_stock_prices_empty():
    result = get_stock_prices([])

    assert result == []

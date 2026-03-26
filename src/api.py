import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_currency_rates(currencies):
    result = []

    for cur in currencies:
        try:
            r = requests.get(f"https://api.exchangerate.host/latest?base={cur}")
            data = r.json()
            result.append({
                "currency": cur,
                "rate": round(data["rates"]["RUB"], 2)
            })
        except Exception:
            result.append({"currency": cur, "rate": None})

    return result


def get_stock_prices(stocks):
    result = []

    for stock in stocks:
        # заглушка (без платного API)
        result.append({
            "stock": stock,
            "price": 100.0
        })

    return result

import json
import logging
from datetime import datetime

from src.api import get_currency_rates, get_stock_prices
from src.utils import get_date_range, load_transactions, prepare_dataframe

logger = logging.getLogger(__name__)


def get_greeting(hour: int) -> str:
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    return "Доброй ночи"


def main_page(date_str: str) -> str:
    """Главная страница"""
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    df = load_transactions("data/operations.xlsx")
    df = prepare_dataframe(df)

    start, end = get_date_range(date)
    df = df[(df["Дата операции"] >= start) & (df["Дата операции"] <= end)]

    # карты
    cards = (
        df.groupby("Номер карты")["Сумма платежа"]
        .sum()
        .reset_index()
    )

    cards_data = [
        {
            "last_digits": str(row["Номер карты"])[-4:],
            "total_spent": round(row["Сумма платежа"], 2),
            "cashback": round(row["Сумма платежа"] / 100, 2),
        }
        for _, row in cards.iterrows()
    ]

    # топ транзакции
    top = df.sort_values(by="Сумма платежа", ascending=False).head(5)

    top_transactions = [
        {
            "date": row["Дата операции"].strftime("%d.%m.%Y"),
            "amount": row["Сумма платежа"],
            "category": row["Категория"],
            "description": row["Описание"],
        }
        for _, row in top.iterrows()
    ]

    currencies = ["USD", "EUR"]
    stocks = ["AAPL", "AMZN", "GOOGL"]

    result = {
        "greeting": get_greeting(date.hour),
        "cards": cards_data,
        "top_transactions": top_transactions,
        "currency_rates": get_currency_rates(currencies),
        "stock_prices": get_stock_prices(stocks),
    }

    return json.dumps(result, ensure_ascii=False, indent=2)

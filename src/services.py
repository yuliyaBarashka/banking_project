import json
import re
import logging

logger = logging.getLogger(__name__)


def investment_bank(month, transactions, limit):
    total = 0

    for t in transactions:
        if t["Дата операции"].startswith(month):
            amount = t["Сумма операции"]
            rounded = ((amount // limit) + 1) * limit
            total += rounded - amount

    return total


def search(query, transactions):
    result = [
        t for t in transactions
        if query.lower() in t["Описание"].lower()
        or query.lower() in t["Категория"].lower()
    ]
    return json.dumps(result, ensure_ascii=False)


def search_phone_numbers(transactions):
    pattern = r"\+7\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{2}"
    result = [t for t in transactions if re.search(pattern, t["Описание"])]
    return json.dumps(result, ensure_ascii=False)


def search_transfers(transactions):
    pattern = r"[А-Я][а-я]+ [А-Я]\."
    result = [
        t for t in transactions
        if t["Категория"] == "Переводы" and re.search(pattern, t["Описание"])
    ]
    return json.dumps(result, ensure_ascii=False)

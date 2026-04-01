import json
import logging
from datetime import datetime, timedelta

import pandas as pd

logger = logging.getLogger(__name__)


def save_report(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            name = filename or f"{func.__name__}.json"
            result.to_json(name, force_ascii=False)
            return result
        return wrapper
    return decorator


def spending_by_category(df: pd.DataFrame, category: str, days: int = 0) -> str:
    df = df[df["Категория"] == category].copy()

    if days:
        cutoff = datetime.now() - timedelta(days=days)
        df = df[df["Дата операции"] >= cutoff]

    total = float(df["Сумма платежа"].sum())

    result = {
        "category": category,
        "total_spent": round(total, 2),
        "transactions_count": int(len(df)),
    }

    return json.dumps(result, ensure_ascii=False, indent=2)

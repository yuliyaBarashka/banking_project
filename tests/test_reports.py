import json

import pandas as pd

from src.reports import save_report, spending_by_category


def test_spending_by_category():
    data = {
        "Категория": ["Еда", "Еда", "Транспорт"],
        "Сумма платежа": [100, 200, 50],
    }

    df = pd.DataFrame(data)

    result = spending_by_category(df, "Еда")

    parsed = json.loads(result)

    assert parsed["category"] == "Еда"
    assert parsed["total_spent"] == 300
    assert parsed["transactions_count"] == 2


def test_spending_by_category_empty():
    data = {
        "Категория": ["Еда"],
        "Сумма платежа": [100],
    }

    df = pd.DataFrame(data)

    result = spending_by_category(df, "Развлечения")

    parsed = json.loads(result)

    assert parsed["total_spent"] == 0
    assert parsed["transactions_count"] == 0


def test_save_report(tmp_path):
    file = tmp_path / "report.json"

    @save_report(filename=str(file))
    def dummy():
        return pd.DataFrame({"a": [1, 2]})

    dummy()

    assert file.exists()

from datetime import datetime
from unittest.mock import patch

import pandas as pd

from src.utils import get_date_range, load_transactions, prepare_dataframe


def test_prepare_dataframe():
    data = {
        "Дата операции": ["01.01.2024", "02.01.2024"]
    }

    df = pd.DataFrame(data)

    result = prepare_dataframe(df)

    assert pd.api.types.is_datetime64_any_dtype(result["Дата операции"])


def test_get_date_range():
    date = datetime(2024, 5, 15)

    start, end = get_date_range(date)

    assert start == datetime(2024, 5, 1)
    assert end == date


@patch("src.utils.pd.read_excel")
def test_load_transactions_success(mock_read):
    mock_df = pd.DataFrame({"a": [1, 2]})
    mock_read.return_value = mock_df

    result = load_transactions("fake_path.xlsx")

    assert not result.empty


@patch("src.utils.pd.read_excel")
def test_load_transactions_error(mock_read):
    mock_read.side_effect = Exception("Ошибка")

    result = load_transactions("fake_path.xlsx")

    assert result.empty

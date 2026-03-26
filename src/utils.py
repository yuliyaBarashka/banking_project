import pandas as pd
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def load_transactions(path: str) -> pd.DataFrame:
    """Загрузка транзакций"""
    try:
        df = pd.read_excel(path)
        logger.info("Файл успешно загружен")
        return df
    except Exception as e:
        logger.error(f"Ошибка загрузки: {e}")
        return pd.DataFrame()


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Подготовка датафрейма"""
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    return df


def get_date_range(date: datetime):
    """Диапазон с начала месяца"""
    start = date.replace(day=1)
    return start, date

import pandas as pd
from datetime import datetime, timedelta
import logging

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

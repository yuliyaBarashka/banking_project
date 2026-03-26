from src.services import search, search_phone_numbers, search_transfers


def test_search(sample_transactions):
    result = search("МТС", sample_transactions)
    assert "МТС" in result


def test_phone_search(sample_transactions):
    result = search_phone_numbers(sample_transactions)
    assert "+7" in result


def test_transfer_search(sample_transactions):
    result = search_transfers(sample_transactions)
    assert "Переводы" in result

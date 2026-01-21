import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(1000, 2000, 1500)


def test_transfer_then_interest():
    from_balance, to_balance = transfer(10000, 5000, 2000)
    updated_balance = calculate_interest(from_balance, 5, 1)
    assert round(updated_balance, 2) == 8400.00

# test_unit.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


def test_deposit_valid():
    assert deposit(1000, 500) == 1500


def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)


def test_withdraw_valid():
    assert withdraw(1000, 300) == 700


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 800)


def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(500, -50)


def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00


def test_calculate_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 1)


def test_check_loan_eligibility_true():
    assert check_loan_eligibility(6000, 750) is True


def test_check_loan_eligibility_false():
    assert check_loan_eligibility(3000, 650) is False

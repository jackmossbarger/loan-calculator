# test_app.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import app_test
# from app import app, Loan

# initialze variables to be used in test
loan_amount = 100000
years = 30
interest = 0.06
monthly_payment = 599.55

# unit tests
def test_calculate_monthly_interest_rate():
    assert calculate_monthly_interest_rate(interest) == 0.005

def test_calculate_number_of_payments():
    assert calculate_number_of_payments(years) == 360

def test_calculate_monthly_payment():
    assert round(calculate_monthly_payment(loan_amount, interest, years), 2) == monthly_payment

# functional test
def test_calculate_loan_payment_plan():
    expected_output = f"Loan amount: ${loan_amount:.2f}\nInterest rate: {interest*100:.2f}%\nYears: {years}\nMonthly payment: ${monthly_payment:.2f}\nTotal payment: ${monthly_payment*360:.2f}\n"
    assert calculate_loan_payment_plan(loan_amount, interest, years) == expected_output
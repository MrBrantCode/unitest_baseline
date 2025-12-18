"""
QUESTION:
Write a Python function named `compare_banks(principal, withdrawal_rate)` that determines which of three banks (A, B, and C) would give the highest value at the end of 5 years, given the principal amount and withdrawal rate. The banks have the following interest rates and compounding periods:
- Bank A: 4% annual interest rate, compounded quarterly
- Bank B: 3.6% annual interest rate, compounded monthly
- Bank C: Varying annual interest rate starting at 3.8%, compounded annually, increasing by 0.05% each year
The function should simulate the interest accumulation and withdrawals over 5 years, with a withdrawal of a certain percentage of the principal amount at the end of each year from the bank with the highest balance.
"""

def compare_banks(principal, withdrawal_rate):
    def calculate_balance(principal, rate, compound_times, years, withdrawal_rate):
        balance = principal
        for year in range(years):
            for period in range(compound_times):
                balance *= 1 + rate / compound_times / 100
            balance -= principal * withdrawal_rate
        return balance

    def calculate_annually_increasing_balance(principal, initial_rate, rate_increase, years, withdrawal_rate):
        balance = principal
        rate = initial_rate
        for year in range(years):
            balance *= 1 + rate / 100
            balance -= principal * withdrawal_rate
            rate += rate_increase
        return balance

    bank_a_balance = calculate_balance(principal, 4, 4, 5, withdrawal_rate)
    bank_b_balance = calculate_balance(principal, 3.6, 12, 5, withdrawal_rate)
    bank_c_balance = calculate_annually_increasing_balance(principal, 3.8, 0.05, 5, withdrawal_rate)

    if bank_a_balance >= bank_b_balance and bank_a_balance >= bank_c_balance:
        return 'Bank A'
    elif bank_b_balance >= bank_c_balance:
        return 'Bank B'
    else:
        return 'Bank C'
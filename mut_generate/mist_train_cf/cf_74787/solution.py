"""
QUESTION:
Write a function `accumulated_funds` that calculates the accumulated sum of funds over a given number of years, considering an initial base sum, fluctuating annual interest rates, and periodic annual deposits. The function should take in the initial sum, a list of annual interest rates, the annual deposit amount, and an optional parameter for the number of years (defaulting to 5). It should return the accumulated sum after the specified number of years.
"""

def accumulated_funds(initial_sum, interest_rates, period_deposit, years=5):
    sum = initial_sum
    for i in range(years):
        sum = sum + sum * interest_rates[i] + period_deposit
    return sum
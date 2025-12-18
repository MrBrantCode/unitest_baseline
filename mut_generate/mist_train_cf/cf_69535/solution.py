"""
QUESTION:
Write a function `calculate_total_amount` that takes three arguments: the initial deposit amount (`principal`), the number of years (`years`), and a list of annual interest rates (`interest_rates`). The function should calculate the total amount in the account after `years` years, assuming the interest rates are compounded annually and expressed as percentages. The function should return the total amount. The input `interest_rates` list will have the same length as `years`.
"""

def calculate_total_amount(principal, years, interest_rates):
    for i in range(years):
        principal *= 1 + (interest_rates[i] / 100)

    return principal
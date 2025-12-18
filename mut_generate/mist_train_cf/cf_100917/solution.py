"""
QUESTION:
Write a function called `savings_amount` that calculates the total amount of money saved over a certain period of time. The function should take in three parameters: `monthly_savings`, the fixed amount saved each month; `years`, the number of years to save; and `interest_rate`, the annual interest rate. The function should return the total savings, calculated using compound interest, at the end of the given period.
"""

def savings_amount(monthly_savings, years, interest_rate):
    total_savings = 0
    months = years * 12
    for month in range(1, months + 1):
        total_savings += monthly_savings
        total_savings = total_savings * (1 + (interest_rate/12))
    return total_savings
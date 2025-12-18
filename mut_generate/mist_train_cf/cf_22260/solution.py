"""
QUESTION:
Write a function `compound_interest(principal, rate, periods)` that calculates the compound interest given the principal amount, annual interest rate, and the number of compounding periods per year. The function should return the compound interest amount.
"""

def compound_interest(principal, rate, periods):
    """
    Calculate the compound interest given the principal amount, 
    annual interest rate, and the number of compounding periods per year.

    Args:
        principal (float): The principal amount.
        rate (float): The annual interest rate.
        periods (int): The number of compounding periods per year.

    Returns:
        float: The compound interest amount.
    """
    amount = principal * (1 + rate / periods) ** periods
    interest = amount - principal
    return interest
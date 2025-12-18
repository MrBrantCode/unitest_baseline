"""
QUESTION:
Write a Python function `savings_amount` that calculates the total savings over a certain period of time if a fixed amount is saved each month with compound interest. The function should take three parameters: `monthly_savings` (the fixed amount saved each month), `years` (the number of years to save), and `interest_rate` (the annual interest rate). The function should return the total savings at the end of the period, using the compound interest formula.
"""

def savings_amount(monthly_savings, years, interest_rate):
    """
    Calculate the total savings over a certain period of time if a fixed amount is saved each month with compound interest.

    Args:
        monthly_savings (float): The fixed amount saved each month.
        years (int): The number of years to save.
        interest_rate (float): The annual interest rate.

    Returns:
        float: The total savings at the end of the period.
    """
    def compound_interest(principal, rate, time):
        return principal * (1 + rate) ** time

    total_savings = 0
    months = years * 12
    for month in range(1, months + 1):
        total_savings += monthly_savings
        total_savings = compound_interest(total_savings, interest_rate/12, 1)
    return total_savings
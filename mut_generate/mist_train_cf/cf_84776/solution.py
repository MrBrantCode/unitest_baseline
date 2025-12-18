"""
QUESTION:
Write a function `calculate_compound_interest` to calculate the total value of an investment after a certain period of time with compound interest. The function should take four parameters: the principal amount, the annual interest rate (in decimal form), the number of times interest is compounded per year, and the time the money is invested for in years. The function should return the total value of the investment after the given time period.
"""

def calculate_compound_interest(principal, annual_interest_rate, compounding_periods_per_year, investment_time_in_years):
    """
    Calculate the total value of an investment after a certain period of time with compound interest.

    Parameters:
    principal (float): The principal amount.
    annual_interest_rate (float): The annual interest rate in decimal form.
    compounding_periods_per_year (int): The number of times interest is compounded per year.
    investment_time_in_years (int): The time the money is invested for in years.

    Returns:
    float: The total value of the investment after the given time period.
    """
    return principal * (1 + annual_interest_rate/compounding_periods_per_year)**(compounding_periods_per_year*investment_time_in_years)
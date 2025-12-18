"""
QUESTION:
Write a function `calculate_retirement_investment` that calculates the total investment value after a certain number of years. The function takes four parameters: `principal` (initial investment amount), `annual_contribution` (annual contribution amount), `rate` (annual interest rate in decimal), and `years` (number of years). The function should return the total investment value, rounded to two decimal places, after the specified number of years with annual compound interest and annual contributions.
"""

def calculate_retirement_investment(principal, annual_contribution, rate, years):
    """
    Calculate the total investment value after a certain number of years.
    
    Args:
    principal (float): Initial investment amount
    annual_contribution (float): Annual contribution amount
    rate (float): Annual interest rate in decimal
    years (int): Number of years
    
    Returns:
    float: Total investment value after the specified number of years
    """
    investment_value = principal
    for _ in range(years):
        investment_value += annual_contribution
        investment_value *= (1 + rate)
    return round(investment_value, 2)
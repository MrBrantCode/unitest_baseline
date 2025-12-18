"""
QUESTION:
Calculate the total income earned and total tax deducted over a specified period of years given a starting salary, annual increase, annual deduction for taxes, and time period in years. The function should take four parameters: starting_salary, annual_increase, annual_deduction, and time_in_years, and return the total income earned and total tax deducted over the specified period.
"""

def total_income_and_tax(starting_salary, annual_increase, annual_deduction, time_in_years):
    """
    Calculate the total income earned and total tax deducted over a specified period of years.

    Args:
        starting_salary (float): The initial salary.
        annual_increase (float): The annual percentage increase in salary.
        annual_deduction (float): The annual percentage deduction for taxes.
        time_in_years (int): The time period in years.

    Returns:
        tuple: A tuple containing the total income earned and total tax deducted.
    """
    total_income = 0
    total_tax_deducted = 0

    for i in range(1, time_in_years + 1):
        annual_income = starting_salary * (1 - annual_deduction / 100) * ((1 + annual_increase / 100) ** i)
        total_income += annual_income
        total_tax_deducted += annual_income * annual_deduction / 100

    return total_income, total_tax_deducted
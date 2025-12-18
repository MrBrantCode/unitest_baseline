"""
QUESTION:
Write a function called `calculate_compound_interest` to calculate the final amount after a certain number of years, considering the compound interest with inflation. The function should take in the principal amount, annual interest rate, inflation rate, number of times the interest is compounded per year, and the number of years. The interest rates and inflation rate should be passed as decimals. The function should return the final amount after the given number of years, rounded to two decimal places.
"""

def calculate_compound_interest(principal, annual_interest_rate, inflation_rate, compounds_per_year, years):
    """
    Calculate the final amount after a certain number of years, 
    considering the compound interest with inflation.

    Args:
        principal (float): The principal amount (initial investment)
        annual_interest_rate (float): The annual interest rate (as a decimal)
        inflation_rate (float): The inflation rate (as a decimal)
        compounds_per_year (int): The number of times the interest is compounded per year
        years (int): The number of years

    Returns:
        float: The final amount after the given number of years, rounded to two decimal places
    """
    return round(principal * (1 + (annual_interest_rate - inflation_rate)/compounds_per_year) ** (compounds_per_year*years), 2)
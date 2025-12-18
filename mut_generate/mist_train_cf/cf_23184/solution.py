"""
QUESTION:
Calculate the compound interest for multiple time periods with variable interest rates. Implement a function `calculate_compound_interest(principal, interest_rates, time, compounded_per_year)` where `principal` is the initial investment amount, `interest_rates` is a list of annual interest rates as decimals, `time` is the number of years the money is invested, and `compounded_per_year` is the number of times interest is compounded per year. The function should return a list of future values for each year and the total amount after the specified time period.
"""

def calculate_compound_interest(principal, interest_rates, time, compounded_per_year):
    """
    Calculate the compound interest for multiple time periods with variable interest rates.

    Args:
    principal (float): The initial investment amount.
    interest_rates (list): A list of annual interest rates as decimals.
    time (int): The number of years the money is invested.
    compounded_per_year (int): The number of times interest is compounded per year.

    Returns:
    list: A list of future values for each year and the total amount after the specified time period.
    """
    future_values = []
    for i in range(time):
        rate = interest_rates[i]
        future_value = principal * (1 + rate/compounded_per_year)**(compounded_per_year * (i+1))
        future_values.append(future_value)
    return future_values, sum(future_values)
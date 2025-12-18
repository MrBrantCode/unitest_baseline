"""
QUESTION:
Create a function named `calculate_fx_forward_rate` that takes the spot exchange rate, domestic interest rate, foreign interest rate, and time to maturity as input and returns the forward exchange rate. Assume the interest rates are annualized and the time to maturity is in years. Do not round the result.
"""

def calculate_fx_forward_rate(spot_exchange_rate, domestic_interest_rate, foreign_interest_rate, time_to_maturity):
    """
    Calculate the forward exchange rate using the given spot exchange rate, domestic interest rate, 
    foreign interest rate, and time to maturity.

    Args:
    spot_exchange_rate (float): The current spot exchange rate.
    domestic_interest_rate (float): The annualized domestic interest rate.
    foreign_interest_rate (float): The annualized foreign interest rate.
    time_to_maturity (float): The time to maturity in years.

    Returns:
    float: The forward exchange rate.
    """
    forward_exchange_rate = spot_exchange_rate * ((1 + domestic_interest_rate) / (1 + foreign_interest_rate)) ** time_to_maturity
    return forward_exchange_rate
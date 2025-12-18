"""
QUESTION:
Write a function `calculate_risk_neutral_expectation` that takes as input the current option price, delta, and gamma, and a percentage change in the spot price, and returns the risk-neutral expectation of the option price after the spot price change, assuming no change in volatility or time decay. The function should account for the convexity of options prices due to gamma.
"""

def calculate_risk_neutral_expectation(current_option_price, delta, gamma, percentage_change_in_spot_price):
    """
    Calculate the risk-neutral expectation of the option price after a percentage change in the spot price.

    Parameters:
    current_option_price (float): The current price of the option.
    delta (float): The delta of the option, representing the expected change in option price for a 1% change in the underlying asset price.
    gamma (float): The gamma of the option, representing the rate of change of the delta.
    percentage_change_in_spot_price (float): The percentage change in the spot price.

    Returns:
    float: The risk-neutral expectation of the option price after the spot price change.
    """
    change_in_spot_price = percentage_change_in_spot_price / 100
    return current_option_price + (delta * change_in_spot_price) + 0.5 * gamma * (change_in_spot_price ** 2)
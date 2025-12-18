"""
QUESTION:
Write a function called `max_call_fly_price` that calculates the maximum amount you would be willing to pay for a European call fly given three strike prices, assuming no fees and a 0% interest rate, and regardless of the underlying distribution. The function should take three integer parameters: the price of the lower strike call option, the price of the at-the-money call option, and the price of the higher strike call option.
"""

def max_call_fly_price(lower_strike_price, at_the_money_price, higher_strike_price):
    """
    Calculate the maximum amount you would be willing to pay for a European call fly.
    
    Parameters:
    lower_strike_price (int): The price of the lower strike call option.
    at_the_money_price (int): The price of the at-the-money call option.
    higher_strike_price (int): The price of the higher strike call option.
    
    Returns:
    int: The maximum amount you would be willing to pay for a European call fly.
    """
    return higher_strike_price - lower_strike_price
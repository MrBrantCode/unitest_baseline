"""
QUESTION:
Create a function called `calculate_skew` that calculates the implied volatility skew for options with different strike prices but the same expiry. The function should take in two parameters: `strike_prices` and `implied_volatilities`, which are lists of floats representing the strike prices and corresponding implied volatilities of the options. The function should return a float representing the implied volatility skew.
"""

def calculate_skew(strike_prices, implied_volatilities):
    """
    Calculate the implied volatility skew for options with different strike prices but the same expiry.

    Args:
    strike_prices (list of floats): List of strike prices of the options.
    implied_volatilities (list of floats): List of corresponding implied volatilities of the options.

    Returns:
    float: The implied volatility skew.
    """
    # Calculate the at-the-money volatility (assuming the ATM strike price is the mean of the strike prices)
    atm_strike_price = sum(strike_prices) / len(strike_prices)
    atm_volatility = implied_volatilities[strike_prices.index(min(strike_prices, key=lambda x:abs(x-atm_strike_price)))]

    # Calculate the average volatility of out-of-the-money options
    otm_volatilities = [iv for sp, iv in zip(strike_prices, implied_volatilities) if sp > atm_strike_price]
    avg_otm_volatility = sum(otm_volatilities) / len(otm_volatilities)

    # Calculate the average volatility of in-the-money options
    itm_volatilities = [iv for sp, iv in zip(strike_prices, implied_volatilities) if sp < atm_strike_price]
    avg_itm_volatility = sum(itm_volatilities) / len(itm_volatilities)

    # Calculate the skew
    skew = (avg_otm_volatility - avg_itm_volatility) / atm_volatility

    return skew
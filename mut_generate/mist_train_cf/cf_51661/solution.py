"""
QUESTION:
Derive the price of an SPY option from the price of an equivalent SPX option, assuming the main difference lies in the contract value. Write a function named `spy_option_price` that takes the price of an SPX option as input and returns a rough estimate of the price of the corresponding SPY option.
"""

def spy_option_price(spx_option_price):
    """
    Derives the price of an SPY option from the price of an equivalent SPX option.

    Args:
    spx_option_price (float): The price of the SPX option.

    Returns:
    float: A rough estimate of the price of the corresponding SPY option.
    """
    # Divide the price of the SPX option by 10 to derive the price of the SPY option
    return spx_option_price / 10
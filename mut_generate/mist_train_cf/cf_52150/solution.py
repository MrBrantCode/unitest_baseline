"""
QUESTION:
Compute the mid IV in a model-agnostic fashion given the bid IV and ask IV for the same option (same underlying asset, strike price, and expiration date), without considering arbitrage-freeness.
"""

def compute_mid_iv(bid_iv, ask_iv):
    """
    Compute the mid IV in a model-agnostic fashion given the bid IV and ask IV for the same option.

    Args:
    bid_iv (float): The implied volatility of the bid price.
    ask_iv (float): The implied volatility of the ask price.

    Returns:
    float: The mid IV.
    """
    return (bid_iv + ask_iv) / 2
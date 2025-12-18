"""
QUESTION:
Write a function named `calculate_swaption_strike` that takes a callable bond's call price as input and returns the strike price of the swaption used to decompose the callable bond into a long vanilla bond and a short receiver swaption.
"""

def calculate_swaption_strike(call_price):
    """
    Calculate the strike price of the swaption used to decompose a callable bond into a long vanilla bond and a short receiver swaption.

    Args:
    call_price (float): The call price of the callable bond.

    Returns:
    float: The strike price of the swaption.
    """
    # The strike price of the swaption is set at the call price of the bond
    return call_price
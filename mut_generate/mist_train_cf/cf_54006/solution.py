"""
QUESTION:
Write a function named `calculate_credit_risk_metrics` that calculates and returns CS01 (Credit Delta or Credit DV01) and RST 1% (Relative Spread Tightening by 1%) for a given credit derivative. The function should take in the current market value, credit spread, and the change in credit spread (in basis points) as input parameters. It should return a tuple containing the CS01 and RST 1% values. The function should assume that the change in market value is directly proportional to the change in credit spread.
"""

def calculate_credit_risk_metrics(current_market_value, credit_spread, change_in_credit_spread):
    """
    Calculate CS01 (Credit Delta or Credit DV01) and RST 1% (Relative Spread Tightening by 1%)
    for a given credit derivative.

    Args:
    - current_market_value (float): The current market value of the credit derivative.
    - credit_spread (float): The current credit spread.
    - change_in_credit_spread (float): The change in credit spread in basis points.

    Returns:
    - tuple: A tuple containing the CS01 and RST 1% values.
    """
    # Calculate CS01
    cs01 = (change_in_credit_spread / 100) * current_market_value
    
    # Calculate RST 1%
    rst_1_percent = (credit_spread / 100) * current_market_value
    
    return cs01, rst_1_percent
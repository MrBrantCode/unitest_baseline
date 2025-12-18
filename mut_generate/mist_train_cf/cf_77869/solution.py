"""
QUESTION:
Write a function `convert_treasury_price` that converts a given Treasury Bond price from its standard notation (e.g. '119'14.7') to its decimal equivalent. The standard notation represents a price as a whole number and a fraction, where the fraction is expressed in 32nds (e.g., the example '119'14.7' represents 119 + 14.7/32).
"""

def convert_treasury_price(price):
    """
    Converts a given Treasury Bond price from its standard notation to its decimal equivalent.

    Args:
        price (str): The Treasury Bond price in standard notation (e.g. '119'14.7').

    Returns:
        float: The decimal equivalent of the given Treasury Bond price.
    """
    whole, fraction = price.split("'")
    fraction, fraction_decimal = fraction.split(".")
    return int(whole) + int(fraction) / 32 + int(fraction_decimal) / (32 * 10)
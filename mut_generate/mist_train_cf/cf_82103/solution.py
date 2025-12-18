"""
QUESTION:
Estimate the product of two decimal numbers as the closest whole number by rounding each number to the nearest integer and multiplying them together. The function should be named `estimate_product` and take two decimal numbers as input. The output should be the estimated product as an integer.
"""

def estimate_product(a, b):
    """
    Estimate the product of two decimal numbers as the closest whole number by rounding each number to the nearest integer and multiplying them together.

    Args:
        a (float): The first decimal number.
        b (float): The second decimal number.

    Returns:
        int: The estimated product as an integer.
    """
    return round(a) * round(b)
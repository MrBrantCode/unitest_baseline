"""
QUESTION:
Convert a mixed number to an improper fraction and simplify it to its lowest terms. Create a function named `simplify_mixed_number` that takes three integers as parameters: `whole_number`, `numerator`, and `denominator`. The function should return a string representing the simplified improper fraction in the format 'numerator/denominator'.
"""

from math import gcd

def simplify_mixed_number(whole_number, numerator, denominator):
    """
    Convert a mixed number to an improper fraction and simplify it to its lowest terms.

    Parameters:
    whole_number (int): The whole number part of the mixed number.
    numerator (int): The numerator of the fractional part.
    denominator (int): The denominator of the fractional part.

    Returns:
    str: A string representing the simplified improper fraction in the format 'numerator/denominator'.
    """

    # Convert to improper fraction
    improper_numerator = whole_number * denominator + numerator

    # Simplify the improper fraction
    common_divisor = gcd(improper_numerator, denominator)
    simplified_numerator = improper_numerator // common_divisor
    simplified_denominator = denominator // common_divisor

    return f"{simplified_numerator}/{simplified_denominator}"
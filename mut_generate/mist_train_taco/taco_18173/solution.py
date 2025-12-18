"""
QUESTION:
Let's Start Simple Write a programe to Sum of two Decimal Value.

SAMPLE INPUT
12.25
3.60

SAMPLE OUTPUT
15.85
"""

def sum_two_decimals(decimal1: float, decimal2: float) -> str:
    """
    Sums two decimal values and returns the result formatted to two decimal places.

    Parameters:
    - decimal1 (float): The first decimal value.
    - decimal2 (float): The second decimal value.

    Returns:
    - str: The sum of the two decimal values, formatted to two decimal places.
    """
    result = decimal1 + decimal2
    return "{0:.2f}".format(result)
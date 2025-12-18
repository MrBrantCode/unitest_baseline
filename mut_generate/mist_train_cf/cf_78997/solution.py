"""
QUESTION:
Implement the `extract_integer` function that takes a float `number` and an integer `precision` as input, and returns the integer segment of the number while preserving the precision up to the specified decimal point. The function should handle both positive and negative numbers. The returned value should be a float, rounded to the specified precision.
"""

def extract_integer(number: float, precision: int) -> float:
    """
    Given a float, it can be broken down into an integer component (biggest integer less than or equal to the provided number) 
    and decimals (remaining portion always less than 1 and greater than -1).

    Provide the integer(segment) of the positive or negative number, while preserving the precision up to a specified decimal point.

    Args:
    number (float): The input float number.
    precision (int): The specified decimal point.

    Returns:
    float: The integer segment of the number, rounded to the specified precision.
    """
    int_part = int(number)
    dec_part = round(number - int_part, precision)

    return float(int_part) + dec_part
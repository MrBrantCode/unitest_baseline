"""
QUESTION:
Create a function `pentagon_perimeter(x)` that calculates the perimeter of a regular pentagon given the length of each side `x`. The function should accept a floating-point number `x` within the range `7 <= x <= 15` and return the perimeter as a floating-point number. If the input value `x` is outside the specified range, the function should return an error message.
"""

def pentagon_perimeter(x):
    """
    Calculate the perimeter of a regular pentagon given the length of each side.

    Args:
    x (float): The length of each side of the pentagon.

    Returns:
    float: The perimeter of the pentagon if x is within the range 7 <= x <= 15.
    str: An error message if x is outside the specified range.
    """
    if x < 7 or x > 15:
        return "Error: Input value is out of range."
    else:
        return 5 * x
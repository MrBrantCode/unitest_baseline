"""
QUESTION:
Write a function `convertFloatToInt` that takes a floating-point number as input and returns the integer part of the number. The function should be compatible with both positive and negative numbers, and round towards zero. Considerations should be made for performance and compatibility.
"""

def convertFloatToInt(n):
    """
    Converts a floating-point number to an integer by rounding towards zero.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The integer part of the input number.
    """
    return int(n)
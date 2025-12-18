"""
QUESTION:
Create a function `trailing_components` that takes an array of six unique elements as input and returns an array containing the trailing three components of the input array. The function should handle arrays of exactly six elements.
"""

def trailing_components(arr):
    """
    Returns the trailing three components of the input array.

    Args:
    arr (list): An array of exactly six unique elements.

    Returns:
    list: An array containing the trailing three components of the input array.
    """
    return arr[-3:]
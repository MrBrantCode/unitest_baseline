"""
QUESTION:
Create a function `arithmetic_mean` that takes an array of numbers as input and returns the arithmetic mean of the array. The function should handle the case where the input array is empty, avoiding a division by zero error.
"""

def arithmetic_mean(array):
    """
    This function calculates the arithmetic mean of an array of numbers.

    Args:
        array (list): A list of numbers.

    Returns:
        float: The arithmetic mean of the input array, or None if the array is empty.
    """
    return sum(array) / len(array) if array else None
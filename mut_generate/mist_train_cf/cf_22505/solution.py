"""
QUESTION:
Create a function called `find_max_value` that takes an array of numbers as input and returns the maximum value without using any built-in functions or methods that directly find the maximum value. The input array is guaranteed to have at least one element.
"""

def find_max_value(numbers):
    """
    Find the maximum value in an array of numbers without using built-in max functions.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum value in the list.
    """
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
    return max_value
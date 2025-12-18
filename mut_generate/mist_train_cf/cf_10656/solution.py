"""
QUESTION:
Create a function called `add` that takes an array of numbers and/or nested arrays of numbers as input. The function should recursively traverse the nested arrays, add all the numbers together, and return the sum.
"""

def add(arr):
    """
    Recursively traverse the nested arrays and add all the numbers together.

    Args:
        arr (list): A list of numbers and/or nested lists of numbers.

    Returns:
        int: The sum of all numbers in the array.
    """
    total = 0
    for num in arr:
        if isinstance(num, list):
            total += add(num)
        else:
            total += num
    return total
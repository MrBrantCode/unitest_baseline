"""
QUESTION:
Create a function to replace all odd integers in a list of numbers with their respective square root values, while keeping the even integers unchanged. The function should accept a list of integers as input and return a new list with the odd integers replaced. The list comprehension should be used to achieve this functionality.
"""

def replace_odd_with_square_root(numbers):
    """
    This function replaces all odd integers in a list of numbers with their respective square root values,
    while keeping the even integers unchanged.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list with the odd integers replaced by their square roots.
    """
    return [(n ** 0.5) if n % 2 != 0 else n for n in numbers]
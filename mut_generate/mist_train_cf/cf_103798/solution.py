"""
QUESTION:
Write a function `convert_list` that takes a list of integers as input and returns a new list where all odd numbers are converted to strings and all even numbers are converted to floats. The order of the numbers in the original list must be preserved.
"""

def convert_list(lst):
    """
    This function takes a list of integers and returns a new list where all odd numbers are converted to strings and all even numbers are converted to floats.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list with odd numbers as strings and even numbers as floats.
    """
    return [str(num) if num % 2 != 0 else float(num) for num in lst]
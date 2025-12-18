"""
QUESTION:
Write a function `sort_complex_numbers` that takes a list of complex numbers as input and returns the list sorted in descending order by their absolute values. The function should use the built-in `abs` function to compute the absolute value of each complex number.
"""

def sort_complex_numbers(complex_nums):
    """
    Sorts a list of complex numbers in descending order by their absolute values.

    Args:
    complex_nums (list): A list of complex numbers.

    Returns:
    list: The sorted list of complex numbers.
    """
    return sorted(complex_nums, key=abs, reverse=True)
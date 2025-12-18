"""
QUESTION:
Implement a function to sort a list of complex numbers in ascending order based on their absolute values. The function should take a list of complex numbers as input and return the sorted list. Note: The input list can be modified.
"""

def sort_complex_numbers(complex_numbers):
    """
    Sorts a list of complex numbers in ascending order based on their absolute values.

    Args:
        complex_numbers (list): A list of complex numbers.

    Returns:
        list: The sorted list of complex numbers.
    """
    complex_numbers.sort(key=abs)
    return complex_numbers
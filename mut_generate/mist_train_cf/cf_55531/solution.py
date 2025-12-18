"""
QUESTION:
Create a function called `sum_odd_elements` that takes a list of integers as input and returns the sum of all odd elements in the list. The function should only consider odd elements and ignore even elements.
"""

def sum_odd_elements(lst):
    """
    This function calculates the sum of all odd elements in a given list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of all odd elements in the list.
    """
    total = 0
    for i in lst:
        if i % 2 != 0:  # check if an element is odd
            total += i
    return total
"""
QUESTION:
Construct a function named `print_and_sum_greater_than_10` that takes a list of integers as input. The function should iterate over the list in reverse order, print each element that is greater than 10, and return the sum of these elements.
"""

def print_and_sum_greater_than_10(lst):
    """
    This function takes a list of integers, iterates over it in reverse order, 
    prints each element greater than 10, and returns their sum.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of elements greater than 10.
    """
    return sum(element for element in reversed(lst) if element > 10 and (print(element) or True))
"""
QUESTION:
Create a function `multiply_list` that calculates the product of all numbers in a given list. The function should take a list of integers as input, and return the product of all elements in the list. The list may contain any non-negative integers.
"""

def multiply_list(input_list):
    """
    This function calculates the product of all numbers in a given list.

    Args:
    input_list (list): A list of non-negative integers.

    Returns:
    int: The product of all elements in the list.
    """
    result = 1
    for elem in input_list:
        result *= elem
    return result
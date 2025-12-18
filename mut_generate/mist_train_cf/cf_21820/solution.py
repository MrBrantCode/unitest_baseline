"""
QUESTION:
Write a function named `sum_and_multiply` that takes a list of numbers as input and returns the sum of the 3rd and 5th elements multiplied by the 2nd element, then subtract the 4th element from the result. The input list will have at least 5 elements.
"""

def sum_and_multiply(lst):
    """
    This function takes a list of numbers as input and returns the sum of the 3rd and 5th elements 
    multiplied by the 2nd element, then subtract the 4th element from the result.

    Args:
        lst (list): A list of numbers with at least 5 elements.

    Returns:
        int: The result of the calculation.
    """
    return (lst[2] + lst[4]) * lst[1] - lst[3]
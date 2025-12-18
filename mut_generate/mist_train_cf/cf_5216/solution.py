"""
QUESTION:
Write a function `sum_integers` that takes a 2D list of integers and non-integer elements, sums up all integers greater than or equal to 10, ignores non-integer elements, and returns the rounded sum. The 2D list should have at least 5 nested lists, each containing at least 5 elements.
"""

def sum_integers(array):
    """
    This function takes a 2D list of integers and non-integer elements, 
    sums up all integers greater than or equal to 10, ignores non-integer elements, 
    and returns the rounded sum.

    Args:
    array (list): A 2D list of integers and non-integer elements.

    Returns:
    int: The rounded sum of integers greater than or equal to 10.
    """
    total_sum = sum(element for sublist in array for element in sublist if isinstance(element, int) and element >= 10)
    return round(total_sum)
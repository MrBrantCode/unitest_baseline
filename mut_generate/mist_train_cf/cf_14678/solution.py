"""
QUESTION:
Write a function `calculate_sum` that takes a two-dimensional array as input and returns the sum of all its elements. The array can be of any size, and the function should be able to handle it without any prior knowledge of its dimensions.
"""

def calculate_sum(arr):
    """
    Calculate the sum of all elements in a two-dimensional array.

    Args:
    arr (list): A two-dimensional array of integers.

    Returns:
    int: The sum of all elements in the array.
    """
    total_sum = 0
    for row in arr:
        for element in row:
            total_sum += element
    return total_sum
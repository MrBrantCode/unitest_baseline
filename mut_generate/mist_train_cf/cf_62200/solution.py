"""
QUESTION:
Write a function named calcSum that calculates the sum of elements in a 2x5 two-dimensional array. The function should take a 2x5 integer array as input and return the sum of all integers in the array.
"""

def calcSum(arr):
    """
    Calculates the sum of elements in a 2x5 two-dimensional array.

    Args:
        arr (list): A 2x5 integer array.

    Returns:
        int: The sum of all integers in the array.
    """
    return sum(num for row in arr for num in row)
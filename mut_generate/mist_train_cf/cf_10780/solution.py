"""
QUESTION:
Write a function named `sum_odd_numbers` that calculates the sum of all odd numbers in a given multi-dimensional array. The function should be able to handle multi-dimensional arrays of any size and should return the sum of all odd numbers.
"""

def sum_odd_numbers(arr):
    """
    Calculates the sum of all odd numbers in a given multi-dimensional array.
    
    Args:
        arr (list): A multi-dimensional array of integers.
    
    Returns:
        int: The sum of all odd numbers in the array.
    """
    return sum(element for row in arr for element in row if element % 2 != 0)
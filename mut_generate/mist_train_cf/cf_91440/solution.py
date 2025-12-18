"""
QUESTION:
Create a function called `sort_descending` that takes an array of integers as input, where each number is greater than or equal to 10, and returns the array in descending order. The function should use the built-in sort method with the reverse parameter set to True.
"""

def sort_descending(arr):
    """
    This function takes an array of integers as input, 
    where each number is greater than or equal to 10, 
    and returns the array in descending order.

    Parameters:
    arr (list): A list of integers greater than or equal to 10.

    Returns:
    list: The input list in descending order.
    """
    arr.sort(reverse=True)
    return arr
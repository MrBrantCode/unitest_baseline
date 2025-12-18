"""
QUESTION:
Create a function named 'square_descending' that takes an array of integers as input and returns a new array containing the squared values of the input array in descending order. The input array must contain at least 5 elements.
"""

def square_descending(arr):
    """
    This function takes an array of integers, squares each number, 
    and returns the squared values in descending order.

    Args:
        arr (list): A list of integers with at least 5 elements.

    Returns:
        list: A new list containing the squared values in descending order.
    """
    return sorted([num**2 for num in arr], reverse=True)
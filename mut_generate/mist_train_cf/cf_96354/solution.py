"""
QUESTION:
Create a function called `square_odd_elements` that takes an array of at least 10 positive integers as input and returns a new array containing the squared values of all odd elements in ascending order.
"""

def square_odd_elements(arr):
    """
    This function takes an array of at least 10 positive integers as input, 
    squares the odd elements, and returns them in ascending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of squared odd elements in ascending order.
    """
    odd_elements = [num**2 for num in arr if num % 2 != 0]
    return sorted(odd_elements)
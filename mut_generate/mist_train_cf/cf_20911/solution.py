"""
QUESTION:
Create a function `square_odd_elements(arr)` that takes an array of at least 10 positive integers and returns a new array containing the squared values of all odd elements from the input array in ascending order.
"""

def square_odd_elements(arr):
    """
    Returns a new array containing the squared values of all odd elements from the input array in ascending order.

    Args:
        arr (list): An array of at least 10 positive integers.

    Returns:
        list: A new array containing the squared values of all odd elements in ascending order.
    """
    odd_elements = [num**2 for num in arr if num % 2 != 0]
    return sorted(odd_elements)
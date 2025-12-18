"""
QUESTION:
Implement a function named `odd_count` that takes a list of integers as input and returns a tuple containing the count of odd integers in the list and a boolean indicating whether the count is odd.
"""

def odd_count(lst):
    """
    Returns a tuple containing the count of odd integers in the list and a boolean indicating whether the count is odd.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the count of odd integers and a boolean value representing whether the count is odd.
    """
    odd_count = sum(1 for num in lst if num % 2 != 0)
    return odd_count, odd_count % 2 != 0
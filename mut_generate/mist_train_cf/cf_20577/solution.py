"""
QUESTION:
Write a function named `double_and_filter` that takes a list of integers as input, doubles each unique element, removes any duplicates, and returns a new sorted list in descending order containing only the elements that are divisible by 3. The original list should remain unchanged.
"""

def double_and_filter(lst):
    """
    This function takes a list of integers, doubles each unique element, 
    removes any duplicates, and returns a new sorted list in descending 
    order containing only the elements that are divisible by 3.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new sorted list in descending order containing only the 
        elements that are divisible by 3.
    """
    return sorted([x*2 for x in set(lst) if x % 3 == 0], reverse=True)
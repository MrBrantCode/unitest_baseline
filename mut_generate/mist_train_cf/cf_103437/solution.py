"""
QUESTION:
Create a function `reverse_populate_list` to populate a list with integers from 0 to n in reverse order. The function should take an integer `n` as input and return the populated list. The function must run efficiently even for large inputs.
"""

def reverse_populate_list(n):
    """
    Populate a list with integers from 0 to n in reverse order.
    
    Args:
        n (int): The upper limit of the range of integers.
    
    Returns:
        list: A list of integers from 0 to n in reverse order.
    """
    # Initialize a list with a predefined length to avoid repeated insertions or appends
    populated_list = [None] * (n + 1)
    
    # Populate the list in reverse order using negative indices
    for i in range(n + 1):
        populated_list[-(i+1)] = i
    
    return populated_list
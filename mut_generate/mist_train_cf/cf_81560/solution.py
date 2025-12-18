"""
QUESTION:
Create a function `filter_even_reverse` that takes a list of integers as input, returns a new list containing only the even numbers from the original list, and in reverse order of their appearance.
"""

def filter_even_reverse(nums):
    """
    This function filters a list of integers to only include even numbers 
    and returns them in reverse order of their appearance.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of even integers in reverse order.
    """
    return [x for x in nums[::-1] if x % 2 == 0]
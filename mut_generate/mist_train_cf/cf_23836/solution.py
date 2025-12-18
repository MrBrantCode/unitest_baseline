"""
QUESTION:
Create a function named `increment_list` that takes a list of integers as input and returns a new list where each element is one more than the corresponding element in the input list. The function should be optimized for efficiency and readability, and should not modify the original input list.
"""

def increment_list(nums):
    """
    Returns a new list where each element is one more than the corresponding element in the input list.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A new list with each element incremented by 1.
    """
    return [num + 1 for num in nums]
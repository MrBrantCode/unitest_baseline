"""
QUESTION:
Implement a function named `store_zero_positions` that takes a list of integers as input and returns a list of indices where the input list contains zero.
"""

def store_zero_positions(nums):
    """
    Returns a list of indices where the input list contains zero.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of indices where the input list contains zero.
    """
    output = []
    for i, num in enumerate(nums):
        if num == 0:
            output.append(i)
    return output
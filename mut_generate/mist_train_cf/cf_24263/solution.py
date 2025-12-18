"""
QUESTION:
Write a function `find_sum` that takes an integer `n` as input and returns the sum of all positive integers up to `n`. The input `n` is a positive integer.
"""

def find_sum(n):
    """
    This function calculates the sum of all positive integers up to n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of all positive integers up to n.
    """
    # Initialize sum 
    total_sum = 0
    
    # Find sum of all numbers
    for i in range(1, n+1):
        total_sum = total_sum + i
    
    return total_sum
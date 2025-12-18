"""
QUESTION:
Implement a recursive function `factorial(n)` that calculates the factorial of a given integer `n`. The function should handle cases where `n` is a negative number and return `None` in such cases. The solution should have a time complexity of O(n).
"""

def factorial(n):
    """
    Calculate the factorial of a given integer n.
    
    If n is negative, return None.
    
    Time complexity: O(n)
    
    Parameters:
    n (int): The input number.
    
    Returns:
    int or None: The factorial of n or None if n is negative.
    """
    # Base case: factorial of 0 or 1 is always 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: calculate factorial using recursion
    if n < 0:
        # if n is negative, return None
        return None
    else:
        return n * factorial(n-1)
"""
QUESTION:
Create a function named 'factorial' that calculates the factorial of a given input 'n' using recursion, with a time complexity of O(n). The function should return the factorial of 'n' if 'n' is a non-negative integer, otherwise it should print an error message and return None.
"""

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer 'n' using recursion.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of 'n' if 'n' is a non-negative integer, otherwise None.
    """
    # Base cases
    if n == 0:
        return 1
    elif n < 0 or isinstance(n, float):
        print("Error: Input must be a non-negative integer")
        return None
    
    # Recursive call
    return n * factorial(n - 1)
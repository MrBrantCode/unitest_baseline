"""
QUESTION:
Analyze the time and space complexity of a recursive function with the given signature: `fibonacci(n)`. The input "n" is a positive integer. The code must be implemented recursively and should have a time complexity of O(2^n) or better and a space complexity of O(n) or better.
"""

def fibonacci(n):
    """
    This function calculates the n-th Fibonacci number recursively.

    Args:
    n (int): A positive integer.

    Returns:
    int: The n-th Fibonacci number.

    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
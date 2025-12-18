"""
QUESTION:
Write a recursive function `fibonacci(n)` that calculates the nth Fibonacci number, where `n` is a non-negative integer. The function should use the recursive formula `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` and base cases `fibonacci(0) = 0` and `fibonacci(1) = 1`.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    else:
        # Recursive case: Calculate fibonacci(n) as fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)
"""
QUESTION:
Develop a function called `fibonacci` that takes an integer `n` as input and returns the `n`-th Fibonacci sequence value. The function should handle cases where `n` is less than or equal to 0, and return an error message in such cases. The function should also handle cases where `n` is 1 or 2, returning 0 and 1 respectively, and for values of `n` greater than 2, it should calculate the `n`-th Fibonacci sequence value using a loop.
"""

def fibonacci(n):
    """
    Returns the n-th Fibonacci sequence value.
    
    Args:
    n (int): The position of the Fibonacci sequence value to be returned.
    
    Returns:
    int: The n-th Fibonacci sequence value if n is a positive integer, otherwise an error message.
    """
    if n <= 0:
        return "Invalid input. Must be greater than 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1, fib2 = 0, 1
        for _ in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2
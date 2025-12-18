"""
QUESTION:
Write a function `fibonacci(n)` to calculate the nth Fibonacci number using recurrence relation. The function should take an integer `n` as input and return the nth Fibonacci number. The Fibonacci sequence is defined by the recurrence relation F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recurrence relation.
    
    Args:
        n (int): The position of the Fibonacci number to calculate.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
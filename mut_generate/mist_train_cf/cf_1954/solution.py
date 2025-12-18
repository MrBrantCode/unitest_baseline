"""
QUESTION:
Implement a function named `fibonacci(n)` to calculate the nth term of the Fibonacci sequence using recursion, without loops or iterative constructs. The result should be returned modulo 10^9+7.
"""

def fibonacci(n):
    """
    Calculate the nth term of the Fibonacci sequence using recursion.

    Args:
    n (int): The term number in the Fibonacci sequence.

    Returns:
    int: The nth term of the Fibonacci sequence modulo 10^9+7.
    """
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (fib(n-1) + fib(n-2)) % (10**9 + 7)

    return fib(n)
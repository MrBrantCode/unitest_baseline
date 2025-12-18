"""
QUESTION:
Create a function `fibonacci(n)` that generates the first `n` Fibonacci numbers in O(n) time complexity. The function should use a recursive approach to calculate the Fibonacci numbers.
"""

def fibonacci(n):
    """
    Generate the first n Fibonacci numbers in O(n) time complexity.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n-1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
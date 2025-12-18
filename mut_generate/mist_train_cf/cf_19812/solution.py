"""
QUESTION:
Write a function `fibonacci_sequence(n)` that generates the Fibonacci sequence up to the nth number, where n must be a prime number greater than 100. The function should return a list of Fibonacci numbers.
"""

def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number, where n must be a prime number greater than 100.

    Args:
        n (int): A prime number greater than 100.

    Returns:
        list: A list of Fibonacci numbers.
    """
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
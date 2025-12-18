"""
QUESTION:
Write a function named `generate_fibonacci` to generate the Fibonacci sequence up to the nth number in the sequence. The sequence should start from 0 and 1. Implement the function to return a list of Fibonacci numbers up to the nth number. The input number is assumed to be a non-negative integer.
"""

def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth number.

    Args:
    n (int): A non-negative integer.

    Returns:
    list: A list of Fibonacci numbers up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
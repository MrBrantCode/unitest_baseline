"""
QUESTION:
Write a function called `generate_odd_fibonacci_numbers` that generates an array of the first n odd Fibonacci numbers within a given range (1000, 10000).
"""

def generate_odd_fibonacci_numbers(n, min_val, max_val):
    """
    Generates an array of the first n odd Fibonacci numbers within a given range.

    Args:
        n (int): The number of odd Fibonacci numbers to generate.
        min_val (int): The minimum value of the range (inclusive).
        max_val (int): The maximum value of the range (inclusive).

    Returns:
        list: An array of the first n odd Fibonacci numbers within the given range.
    """
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        a, b = b, a + b
        if a > max_val:
            break
        if a > min_val and a % 2 != 0:
            fib_sequence.append(a)
    return fib_sequence
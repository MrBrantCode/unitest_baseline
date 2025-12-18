"""
QUESTION:
Generate a function named `fibonacci_even_sum` that takes an integer `n` as input, representing the number of Fibonacci numbers to generate. Calculate the Fibonacci sequence up to the nth number and return the sum of the even numbers in the sequence.
"""

def fibonacci_even_sum(n):
    """
    Calculate the sum of even numbers in the Fibonacci sequence up to the nth number.

    Args:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    int: The sum of even numbers in the Fibonacci sequence.
    """
    a, b = 0, 1
    even_sum = 0

    for _ in range(n):
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum
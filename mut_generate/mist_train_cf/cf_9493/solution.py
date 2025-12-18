"""
QUESTION:
Create a function named `generate_fibonacci` that generates the first n Fibonacci numbers. The function should take an integer n as input and return a list of the first n Fibonacci numbers. Note that the Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def generate_fibonacci(n):
    """
    Generates the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    fibonacci_numbers = [0, 1]
    [fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2]) for _ in range(n - 2)]
    return fibonacci_numbers[:n]
"""
QUESTION:
Generate a function named `generate_fibonacci` that creates a list of the first n Fibonacci numbers, where n is a given integer. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def generate_fibonacci(n):
    """
    Generates a list of the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    fibonacci_list = [0, 1]  # initialize list with first two Fibonacci numbers
    
    while len(fibonacci_list) < n:  # continue adding Fibonacci numbers until desired length is reached
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)
    
    return fibonacci_list
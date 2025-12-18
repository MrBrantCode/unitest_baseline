"""
QUESTION:
Write a function `fibonacci(x)` that generates and prints Fibonacci numbers up to the given number `x`, excluding those divisible by both 4 and 7, and also returns the sum of the generated Fibonacci numbers.
"""

def fibonacci(x):
    """
    Generates and prints Fibonacci numbers up to the given number x, 
    excluding those divisible by both 4 and 7, and returns the sum of the generated Fibonacci numbers.

    Args:
        x (int): The upper limit for generating Fibonacci numbers.

    Returns:
        int: The sum of the generated Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    sum_fibonacci = 0
    while fib_sequence[-1] <= x:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        if fib_sequence[-1] % 4 != 0 or fib_sequence[-1] % 7 != 0:
            print(fib_sequence[-1])
            sum_fibonacci += fib_sequence[-1]
    return sum_fibonacci
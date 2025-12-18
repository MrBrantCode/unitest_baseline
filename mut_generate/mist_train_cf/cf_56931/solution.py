"""
QUESTION:
Create a function called `fibonacci` to generate Fibonacci numbers and `is_prime` to check if a number is prime. Using these functions, print all Fibonacci prime numbers less than 100. The `fibonacci` function should be recursive.
"""

def fibonacci(n):
    """Generate the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True
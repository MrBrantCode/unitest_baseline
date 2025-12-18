"""
QUESTION:
Create a function `generate_fibonacci(n)` that prints the Fibonacci sequence of length `n`, where `n` is a prime number between 10 and 100 (inclusive), and the sum of all the prime numbers in the Fibonacci sequence is greater than 100.
"""

def generate_fibonacci(n):
    """Generate the Fibonacci sequence of length n."""
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence
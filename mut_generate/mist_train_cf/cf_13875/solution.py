"""
QUESTION:
Generate a function called `generate_fibonacci_sequence(n)` that generates the Fibonacci sequence up to a given number `n`. The function should return a list of numbers in the Fibonacci sequence where the last number is less than or equal to `n`.
"""

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # start with the first two numbers of the sequence

    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence
"""
QUESTION:
Create a function `calculate_fibonacci_sequence(n)` to calculate the first `n` numbers of the Fibonacci sequence iteratively using a loop. The function should take a positive integer `n` as input and return a list of the first `n` Fibonacci numbers.
"""

def calculate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # The first two numbers of the Fibonacci sequence

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence
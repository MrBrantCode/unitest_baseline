"""
QUESTION:
Write a function called `fibonacci_sequence(N)` that generates a Fibonacci sequence up to a given number `N`, where `N` is a positive integer less than or equal to 1000. The function should return a list of Fibonacci numbers that do not exceed `N`.
"""

def fibonacci_sequence(N):
    # Check if N is less than or equal to 0
    if N <= 0:
        return []

    # Initialize the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence
    while sequence[-1] + sequence[-2] <= N:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence
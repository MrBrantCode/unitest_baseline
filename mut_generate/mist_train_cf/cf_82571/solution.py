"""
QUESTION:
Write a function named `generate_fibonacci` that takes an integer `n` as input and returns the first `n` Fibonacci numbers along with their positions in the sequence as tuples. The function should validate that `n` is a positive integer and return an error message if it is not. The function should be optimized to handle large values of `n` efficiently.
"""

def generate_fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: The input should be a positive integer."

    fibonacci_sequence = [(0,0), (1,1)]
    if n <= 2:
        return fibonacci_sequence[:n]

    for i in range (2, n):
        next_value = fibonacci_sequence[i-1][1] + fibonacci_sequence[i-2][1]
        fibonacci_sequence.append((i, next_value))

    return fibonacci_sequence
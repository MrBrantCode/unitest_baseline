"""
QUESTION:
Create a function `generate_fibonacci(n)` that generates a Fibonacci sequence of length `n` iteratively using a loop, with a time complexity of O(n) and a space complexity of O(1). The function should return a list containing the Fibonacci sequence, where the sequence starts with 0.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0] * n
    fibonacci_sequence[0] = 0

    if n > 1:
        fibonacci_sequence[1] = 1

    for i in range(2, n):
        fibonacci_sequence[i] = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]

    return fibonacci_sequence
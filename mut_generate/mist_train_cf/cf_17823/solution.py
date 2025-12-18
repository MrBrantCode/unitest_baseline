"""
QUESTION:
Create a function named `generate_fibonacci` that generates a Fibonacci sequence iteratively using a loop. The function should take an integer `n` as input, representing the desired length of the Fibonacci sequence. The function should have a time complexity of O(n) and a space complexity of O(1). The Fibonacci sequence should start with 0, as per the traditional definition.
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
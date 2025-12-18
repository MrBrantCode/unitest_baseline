"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates the first `n` Fibonacci numbers and returns them in reverse order. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should return a list of integers representing the first `n` Fibonacci numbers in reverse order.
"""

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  

    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    return fibonacci_sequence[::-1]  
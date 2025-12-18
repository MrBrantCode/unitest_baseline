"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates a list of Fibonacci numbers up to the nth number in the sequence. The time complexity of the function should be O(n).
"""

def generate_fibonacci(n):
    fibonacci_numbers = []
    if n >= 1:
        fibonacci_numbers.append(0)
    if n >= 2:
        fibonacci_numbers.append(1)
    if n > 2:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fibonacci_numbers.append(b)
    return fibonacci_numbers
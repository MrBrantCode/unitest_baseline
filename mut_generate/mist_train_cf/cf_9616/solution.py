"""
QUESTION:
Create a function `generate_fibonacci(n)` that generates the Fibonacci sequence up to the nth term. The function should have a time complexity of O(n) or better, use constant space, and handle edge cases (negative values of n or zero) gracefully.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        fibonacci_sequence.append(c)
        a, b = b, c

    return fibonacci_sequence
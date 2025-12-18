"""
QUESTION:
Write a function named `generate_fibonacci` that generates the Fibonacci sequence up to the nth term. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence. The function should not use recursion and should not use any additional data structures apart from the output list.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            fibonacci_sequence.append(a + b)
            a, b = b, a + b
        return fibonacci_sequence
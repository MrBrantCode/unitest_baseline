"""
QUESTION:
Design a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where `n` is a non-negative integer. The function should use a multi-step computational process to calculate each term as the sum of the two preceding terms. The function should return a list of Fibonacci numbers. The function should handle cases where `n` is 0, 1, or 2, and return an empty list, a list with one element, or a list with two elements, respectively.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_values = [0, 1]
    for i in range(2, n):
        fibonacci_values.append(fibonacci_values[-1] + fibonacci_values[-2])

    return fibonacci_values
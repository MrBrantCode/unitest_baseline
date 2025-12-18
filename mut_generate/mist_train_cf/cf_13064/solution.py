"""
QUESTION:
Design a function named `fibonacci` that takes an integer `n` as input and returns the n-th Fibonacci number. The function should have a time complexity of O(n) and a space complexity of O(1), and it should return an error message if `n` is negative.
"""

def fibonacci(n):
    if n < 0:
        return "Error: Input value must be non-negative."

    def fibonacci_helper(n, a, b):
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return fibonacci_helper(n - 1, b, a + b)

    return fibonacci_helper(n, 0, 1)
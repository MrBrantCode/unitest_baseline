"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should use a recursive approach with memoization to optimize performance, have a time complexity of O(n) and a space complexity of O(n), and raise a custom exception if the input value is negative.
"""

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def fibonacci(n, memo={}):
    if n < 0:
        raise CustomException("Input value cannot be negative.")

    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]
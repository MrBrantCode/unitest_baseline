"""
QUESTION:
Create a function named `fibonacci` that calculates the nth Fibonacci number using a recursive approach with memoization. The function should raise a custom exception if the input value `n` is negative. The function's time complexity should be O(1) (amortized) and its space complexity should be O(n).
"""

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def fib(n, memo={}):
    if n < 0:
        raise CustomException("Input value cannot be negative.")

    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]
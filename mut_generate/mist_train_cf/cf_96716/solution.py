"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a non-negative integer `n` using recursion. The function should handle the base case where `n` equals 0 and return 1 in this case. For any other value of `n`, the function should call itself with the argument `n - 1` and multiply the result with `n`. Analyze the time and space complexity of the solution, which should be O(n) for both.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
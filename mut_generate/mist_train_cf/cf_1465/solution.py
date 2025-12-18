"""
QUESTION:
Write a function called `factorial(n)` that calculates the factorial of a given number `n` using tail recursion. The function should handle cases where the input size is greater than 10,000 without causing a stack overflow error.
"""

def factorial(n):
    def factorial_helper(n, result):
        while n > 1:
            result *= n
            n -= 1
        return result
    return factorial_helper(n, 1)
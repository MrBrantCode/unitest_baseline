"""
QUESTION:
Write a recursive function `factorial` to calculate the factorial of a given number `n`. The function should have a time complexity of O(n) and a space complexity of O(n), handle negative input numbers by returning an error message, and only use recursion without any loops or iterative constructs.
"""

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
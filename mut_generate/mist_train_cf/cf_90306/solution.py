"""
QUESTION:
Write a recursive function called `factorial` that calculates the factorial of a given integer `n` using a single line of code, with a time complexity of O(n) and space complexity of O(n). The function should return `1` if `n` is `0`.
"""

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
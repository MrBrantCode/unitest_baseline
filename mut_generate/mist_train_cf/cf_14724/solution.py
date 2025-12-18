"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given positive integer using recursion. The function should have a time complexity of O(n) and a space complexity of O(n). The input to the function is a positive integer `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
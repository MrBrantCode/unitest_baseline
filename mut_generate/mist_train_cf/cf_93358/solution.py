"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given positive integer using recursion. The function should have a time complexity of O(n) and a space complexity of O(n). The function should only take one integer parameter `n` and return the factorial of `n`.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: multiply n with factorial of n-1
    return n * factorial(n - 1)
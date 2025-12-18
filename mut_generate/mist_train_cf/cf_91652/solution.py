"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given positive integer `n` using recursion. The function should have a time complexity of O(n) and the input integer `n` will be between 1 and 10.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial of n is n multiplied by factorial of (n-1)
        return n * factorial(n-1)
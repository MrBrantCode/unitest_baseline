"""
QUESTION:
Implement a recursive function named `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should handle edge cases where `n` is zero or a negative number, returning an error message. The function should not use any built-in functions or libraries, and it should have a time complexity of O(n) and a space complexity of O(n).
"""

def factorial(n):
    if n < 0:
        return "Error: Input cannot be a negative number."
    elif n == 0:
        return "Error: Input cannot be zero."
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
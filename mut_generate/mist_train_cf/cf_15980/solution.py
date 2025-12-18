"""
QUESTION:
Write a function called "factorial" that calculates the factorial of a given integer "n" using recursion, with a time complexity of O(n) and a space complexity of O(n). The function should also handle negative input numbers and return an error message if encountered.
"""

def factorial(n):
    if n < 0:
        return "Error: Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
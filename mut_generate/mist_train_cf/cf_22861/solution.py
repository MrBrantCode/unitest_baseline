"""
QUESTION:
Write a program that includes a function named `factorial(n)` to calculate the factorial of a given number `n` using recursion. The function should handle the case when `n` is 0 or 1, and for any other positive integer `n`, it should return `n` multiplied by the factorial of `n-1`. Also, include a function named `get_valid_input()` that prompts the user to enter a positive integer and validates the input to ensure it is a positive integer.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    else:
        return n * factorial(n-1)
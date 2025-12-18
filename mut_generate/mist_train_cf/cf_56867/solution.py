"""
QUESTION:
Write a recursive function called `fibonacci` that takes an integer `n` as input and returns the nth number in the Fibonacci series, where each number is the sum of the two preceding ones, starting with 0 and 1. Ensure the function handles invalid inputs (non-positive integers) and returns an error message in such cases.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
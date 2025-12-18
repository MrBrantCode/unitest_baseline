"""
QUESTION:
Write a function named `factorial` that takes an integer `n` as input and returns its factorial. Use a `for` loop to iterate over a list of numbers from 1 to 5, calculate the factorial of each even number in the list using the `factorial` function, and print the result. The function `factorial` must handle the case where `n` is 0.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
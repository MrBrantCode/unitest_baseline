"""
QUESTION:
Design a function called `factorial` that takes an integer `n` as input and returns the factorial of `n`. The function should use recursion and handle the base case where `n` equals 0.
"""

def factorial(n):
    # base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # recursive case: n! = n * (n-1)!
        return n * factorial(n-1)
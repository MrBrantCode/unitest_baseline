"""
QUESTION:
Write a function named `factorial_` that calculates the factorial of a given non-negative integer using a recursive multi-step process, returning the result. The function should handle base cases for 0 and 1, and should not include error checking for negative inputs.
"""

def factorial_(num):
    """Find the factorial of a given number"""
    # base case: factorial of 0 & 1 is 1
    if num == 0 or num == 1:
        return 1
    else:
        # recursive case: n! = n * (n-1)!
        return num * factorial_(num - 1)
"""
QUESTION:
Create a function named `lucas(n)` that calculates the nth number in the Lucas series, a sequence where each number is the sum of the two preceding ones, starting with 0 and 1. The function should use recursion and handle base cases for `n = 0` and `n = 1` where the corresponding Lucas numbers are 2 and 1, respectively.
"""

def lucas(n):
    if n == 0:
        return 2  # Base case: the 0th number is 2
    elif n == 1:
        return 1  # Base case: the 1st number is 1
    else:
        return lucas(n - 1) + lucas(n - 2)  # Recursive case
"""
QUESTION:
Create a recursive function named `lucas(n)` that takes an integer `n` as input and returns the `n`th number in the Lucas series, where the series starts with 2 and 1, and each subsequent number is the sum of the two preceding ones. The function should handle base cases where `n` is 0 or 1.
"""

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)
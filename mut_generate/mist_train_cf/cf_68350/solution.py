"""
QUESTION:
Implement a recursive function named `recursive_func` that calculates the factorial of a given number `n`. The function should correctly handle the base case and recursive case, and return the calculated factorial. Ensure that the function returns a value for each recursive call.
"""

def recursive_func(n):
    if n == 1:
        return 1
    else:
        return n * recursive_func(n-1)
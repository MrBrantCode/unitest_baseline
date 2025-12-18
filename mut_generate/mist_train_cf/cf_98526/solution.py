"""
QUESTION:
Write a function `factorial(n)` that takes a positive integer `n` and returns its factorial using recursion. The function must not exceed a maximum recursion depth of 1000. It should also handle non-integer input values and values greater than 1000, returning an informative error message in these cases.
"""

def entance(n):
    if not isinstance(n, int):
        return "Error: Input value must be an integer."
    elif n < 0:
        return "Error: Input value must be positive."
    elif n > 1000:
        return "Error: Input value must be less than or equal to 1000."
    elif n == 0:
        return 1
    else:
        try:
            return n * entance(n-1)
        except RecursionError:
            return "Error: Maximum recursion depth exceeded."
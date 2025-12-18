"""
QUESTION:
Create a function named `lucas_series(n)` that returns the nth number in the Lucas series, where the series starts with 2 and 1, and each subsequent number is the sum of the previous two. The function should use 0-based indexing.
"""

def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b    # generate next number in series
    return a